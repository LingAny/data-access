from asyncio import AbstractEventLoop
from serial_asyncio import open_serial_connection

from netutils.clients.serial_ports.byte_size import ByteSize
from netutils.clients.serial_ports.stop_bits import StopBits
from netutils.clients.base_client import BaseClient
from netutils.clients.serial_ports.parity import Parity


class SerialClient(BaseClient):

    def __init__(self, port: str, rate: int, parity: Parity,
                 stop_bits: StopBits, byte_size: ByteSize,
                 loop: AbstractEventLoop, on_data_received, buffer_size: int = None) -> None:
        super().__init__(loop, on_data_received, buffer_size)
        self._port = port
        self._rate = rate
        self._parity = parity
        self._stop_bits = stop_bits
        self._byte_size = byte_size

    async def _open_connection(self) -> None:
        self._reader, self._writer = await open_serial_connection(
            url=self._port,
            parity=self._parity.value,
            baudrate=self._rate,
            stopbits=self._stop_bits.value,
            bytesize=self._byte_size.value,
            loop=self._loop)
