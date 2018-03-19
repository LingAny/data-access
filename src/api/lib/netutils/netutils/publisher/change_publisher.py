from typing import Dict

from nameko.amqp import get_connection
from nameko.standalone.events import get_event_exchange

from netutils.publisher.dispatcher import Dispatcher


class ChangePublisher(object):

    def __init__(self, name: str, dispatcher: Dispatcher) -> None:
        self._name = name
        self._dispatcher = dispatcher
        self._create_exchange()

    def _create_exchange(self) -> None:
        with get_connection(self._dispatcher.amqp_uri) as connection:
            exchange = get_event_exchange(self._name)
            exchange.maybe_bind(connection)
            exchange.declare()

    def on_create(self, payload: Dict[str, object]) -> None:
        self._dispatcher.publish(self._name, 'create', payload)

    def on_update(self, payload: Dict[str, object]) -> None:
        self._dispatcher.publish(self._name, 'update', payload)

    def on_delete(self, payload: Dict[str, object]) -> None:
        self._dispatcher.publish(self._name, 'delete', payload)
