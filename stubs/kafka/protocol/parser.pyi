from kafka.protocol.api import RequestHeader as RequestHeader
from kafka.protocol.commit import GroupCoordinatorResponse as GroupCoordinatorResponse
from kafka.protocol.frame import KafkaBytes as KafkaBytes
from kafka.protocol.types import Int32 as Int32
from typing import Any, Optional

log: Any

class KafkaProtocol:
    in_flight_requests: Any = ...
    bytes_to_send: Any = ...
    def __init__(self, client_id: Optional[Any] = ..., api_version: Optional[Any] = ...) -> None: ...
    def send_request(self, request: Any, correlation_id: Optional[Any] = ...): ...
    def send_bytes(self): ...
    def receive_bytes(self, data: Any): ...
