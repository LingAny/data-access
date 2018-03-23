from abc import ABCMeta, abstractmethod
from asyncio import AbstractEventLoop, StreamWriter, StreamReader, sleep, wait_for
from typing import Callable


class BaseClient(metaclass=ABCMeta):

    def __init__(self, loop: AbstractEventLoop, on_data_received=None,
                 buffer_size: int = None) -> None:

        self._loop = loop
        self._on_data_received = on_data_received
        self._buffer_size = buffer_size

        self._buffer = b''
        self._writer: StreamWriter = None
        self._reader: StreamReader = None

        self._working = False
        self._writing = False

    async def start(self) -> None:
        self._initialize()
        await self._open_connection()
        self._working = True
        while self._working:
            await self._read()
        self._writer.close()
        self._cleanup()

    async def start_writer(self) -> None:
        while not self._working:
            await sleep(0.1)
        self._writing = True
        while self._working and self._writing:
            await self._write()
            await sleep(0.01)

    def stop_client(self) -> None:
        self._working = False

    async def send_data(self, data: bytes) -> None:
        self._buffer += data
        if not self._writing:
            await self.start_writer()

    def set_on_data_received_handler(self, handler: Callable[[bytes], None]) -> None:
        self._on_data_received = handler

    def on_data_received(self, data: bytes):
        if self._on_data_received:
            self._on_data_received(data)

    async def _read(self) -> None:
        try:
            data = await wait_for(self._reader.read(self._buffer_size), timeout=15)
            if not data:
                self._working = False
            self.on_data_received(data)
        except TimeoutError:
            pass

    async def _write(self) -> None:
        if self._buffer:
            self._writer.write(self._buffer)
            self._buffer = b''

    @abstractmethod
    async def _open_connection(self) -> None:
        raise NotImplementedError

    def _initialize(self) -> None:
        pass

    def _cleanup(self) -> None:
        pass
