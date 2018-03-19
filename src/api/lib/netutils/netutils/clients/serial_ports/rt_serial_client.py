from asyncio import sleep

from netutils.clients.serial_ports.serial_client import SerialClient


class RTSerialClient(SerialClient):

    def _initialize(self) -> None:
        import RPi.GPIO as GPIO  # pylint: disable=import-error

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)

    def _cleanup(self) -> None:
        import RPi.GPIO as GPIO  # pylint: disable=import-error

        GPIO.cleanup()

    async def _write(self):
        import RPi.GPIO as GPIO  # pylint: disable=import-error

        if self._buffer:
            GPIO.output(18, True)
            self._writer.write(self._buffer)
            self._buffer = b''
            await sleep(0.02)
            GPIO.output(18, False)
