import logging

from asyncio import AbstractEventLoop, sleep, Future, Task, wait_for
from asyncio.futures import InvalidStateError
from asynqp import connect, Queue, Channel, Connection, Exchange, Message, exceptions, Consumer
from typing import List, Tuple, Any, Dict


class AmqpController(object):

    def __init__(self, host: str, port: int, username: str, password: str,
                 loop: AbstractEventLoop, exchange_name: str,
                 queue_name: str, route_key: str, is_listener: bool,
                 on_message_received=None) -> None:
        self._host = host
        self._port = port
        self._loop = loop
        self._username = username
        self._password = password

        self._connection: Connection = None
        self._consumer: Future = None
        self._producer: Task = None
        self._channels: List[Channel] = []

        self._exchange: Exchange = None
        self._exchange_name = exchange_name
        self._queue_name = queue_name
        self._route_key = route_key
        self._is_listener = is_listener
        self._on_message_received = on_message_received

    def producer_ready(self) -> bool:
        return self._exchange is not None

    async def connect(self) -> None:
        self._connection = await connect(self._host, self._port,
                                         self._username, self._password)

    async def setup(self) -> Tuple[Exchange, Queue]:
        channel = await self._connection.open_channel()
        exchange = await channel.declare_exchange(self._exchange_name, 'topic', auto_delete=True)
        queue = await channel.declare_queue(self._queue_name,
                                            exclusive=(self._queue_name == ''))
        self._channels.append(channel)
        await queue.bind(exchange, self._route_key)
        return exchange, queue

    def on_message_received(self, msg: Message) -> None:
        if self._on_message_received:
            self._on_message_received(msg)

    async def setup_consumer(self) -> Consumer:
        _, queue = await self.setup()

        consumer = await queue.consume(self.on_message_received, no_ack=True)
        return consumer

    async def send_json(self, msg: Message, route: str, mandatory: bool = True) -> None:
        if self._exchange:
            self._exchange.publish(msg, route, mandatory=mandatory)

    async def setup_producer(self) -> None:
        self._exchange, _ = await self.setup()

    async def start(self) -> None:
        try:
            await self.connect()
            if self._is_listener:
                self._consumer = await self.setup_consumer()
            else:
                await self.setup_producer()
        except BaseException:
            logging.exception('failed to connect, trying again.')
            await sleep(1)
            self._loop.create_task(self.start())

    async def stop(self) -> None:
        if self._consumer:
            self._consumer.cancel()
            self._consumer = None
        if self._producer:
            self._producer.cancel()
            self._producer = None

        for channel in self._channels:
            await channel.close()

        self._channels = []
        self._exchange = None
        if self._connection:
            try:
                await self._connection.close()
            except InvalidStateError:
                pass
            self._connection = None

    def connection_lost_handler(self, loop: AbstractEventLoop, context: Dict[str, Any]) -> None:
        exception = context.get('exception')
        if isinstance(exception, exceptions.ConnectionLostError):
            logging.warning('Connection lost -- trying to reconnect')
            close_task = loop.create_task(self.stop())
            wait_for(close_task, None)
            loop.create_task(self.start())
        else:
            loop.default_exception_handler(context)

    def main(self) -> None:
        self._loop.set_exception_handler(self.connection_lost_handler)
        self._loop.create_task(self.start())
