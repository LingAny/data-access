import asyncio
import logging

from abc import abstractmethod, ABCMeta
from typing import Any, List, Tuple, Dict, Set, Optional

from netutils.clients.base_client import BaseClient


class Controller(metaclass=ABCMeta):

    def __init__(self, client: BaseClient, loop: asyncio.AbstractEventLoop) -> None:
        self._client = client
        self._client.set_on_data_received_handler(self._on_data_received)
        self._loop = loop

        self._working = False
        self._buffer = b''
        self._messages: Dict[bytes, bytes] = {}
        self._wait_message_id_set: Set[bytes] = set()

    @abstractmethod
    def _get_message_id_for(self, data: bytes) -> Any:
        raise NotImplementedError

    @abstractmethod
    def _get_request_id_for(self, data: bytes) -> Any:
        raise NotImplementedError

    @abstractmethod
    def _split_messages(self, data: bytes) -> Tuple[List[bytes], bytes]:
        raise NotImplementedError

    @abstractmethod
    def _on_event_received(self, data: bytes) -> None:
        raise NotImplementedError

    def _on_data_received(self, data: bytes) -> None:
        self._buffer += data
        messages, buffer = self._split_messages(self._buffer)

        for message in messages:
            msg_id = self._get_message_id_for(message)

            if not msg_id:
                return

            if msg_id in self._wait_message_id_set:
                self._messages[msg_id] = self._buffer.strip(b'\n')
            else:
                self._on_event_received(message)

        self._buffer = buffer

    async def _wait_message(self, msg_id: Any) -> bytes:
        while True:
            if msg_id in self._messages:
                msg = self._messages[msg_id]
                del self._messages[msg_id]
                self._wait_message_id_set.remove(msg_id)
                return msg
            await asyncio.sleep(0.1)

    async def send_request(self, data: bytes) -> Optional[bytes]:
        logging.debug(f'>>> {data}')
        await self._client.send_data(data)
        try:
            msg_id = self._get_request_id_for(data)
            self._wait_message_id_set.add(msg_id)
            msg = await asyncio.wait_for(self._wait_message(msg_id), timeout=3)
            if not msg:
                self._working = False
            else:
                logging.debug(f'<<< {msg}')
            return msg
        except asyncio.TimeoutError:
            return None

    async def send_message(self, data: bytes) -> None:
        logging.debug(f'>>> {data}')
        await self._client.send_data(data)

    def stop(self) -> None:
        logging.info('stopping TCP client')
        self._client.stop_client()

    async def start_writer(self) -> None:
        await self._client.start_writer()

    async def start(self) -> None:
        logging.info('start TCP client')
        try:
            await self._client.start()
        except BaseException:
            print("can't connect to TCP server")
            await asyncio.sleep(1)
            self._loop.create_task(self.start())
