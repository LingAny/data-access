from typing import Callable, Dict, Any

from nameko.rpc import rpc
from nameko.standalone.events import event_dispatcher


class Dispatcher(object):

    def __init__(self, amqp_uri: str) -> None:
        config = {'AMQP_URI': amqp_uri}
        self._amqp_uri = amqp_uri
        self._dispatch: Callable[[str, str, Dict[str, Any]], None] = event_dispatcher(config)

    @property
    def amqp_uri(self) -> str:
        return self._amqp_uri

    @rpc
    def publish(self, name: str, event_type: str, payload: Dict[str, object]) -> None:
        self._dispatch(name, event_type, payload)
