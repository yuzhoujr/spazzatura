from Queue import Queue
from typing import Any, List, Optional, Tuple, Type

__all__ = ...  # type: List[str]
families = ...  # type: List[None]

class Connection(object):
    _in = ...  # type: Any
    _out = ...  # type: Any
    recv = ...  # type: Any
    recv_bytes = ...  # type: Any
    send = ...  # type: Any
    send_bytes = ...  # type: Any
    def __init__(self, _in, _out) -> None: ...
    def close(self) -> None: ...
    def poll(self, timeout=...) -> Any: ...

class Listener(object):
    _backlog_queue = ...  # type: Optional[Queue]
    address = ...  # type: Any
    def __init__(self, address=..., family=..., backlog=...) -> None: ...
    def accept(self) -> Connection: ...
    def close(self) -> None: ...


def Client(address) -> Connection: ...
def Pipe(duplex=...) -> Tuple[Connection, Connection]: ...
