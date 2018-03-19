from abc import ABCMeta
from asyncio import AbstractEventLoop
from typing import Any, Tuple, List

from netutils.clients.base_client import BaseClient
from netutils.controllers.controller import Controller


class SimpleController(Controller, metaclass=ABCMeta):

    def __init__(self, client: BaseClient, loop: AbstractEventLoop) -> None:
        super().__init__(client, loop)
        self._msg_counter = 0

    def _get_message_id_for(self, data: bytes) -> Any:
        return sorted(self._wait_message_id_set).pop()

    def _get_request_id_for(self, data: bytes) -> Any:
        self._msg_counter += 1
        return self._msg_counter

    def _on_event_received(self, data: bytes) -> None:
        pass

    def _split_messages(self, data: bytes) -> Tuple[List[bytes], bytes]:
        pass
