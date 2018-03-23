from asyncio import AbstractEventLoop, open_connection

from netutils.clients.base_client import BaseClient


class TcpClient(BaseClient):

    def __init__(self, host: str, port: int, loop: AbstractEventLoop,
                 on_data_received, buffer_size: int = None) -> None:
        super().__init__(loop, on_data_received, buffer_size)
        self._host = host
        self._port = port

    async def _open_connection(self) -> None:
        self._reader, self._writer = await open_connection(
            self._host,
            self._port,
            loop=self._loop
        )
