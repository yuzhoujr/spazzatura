from typing import Any
from .. import exceptions
from .. import packages

ConnectTimeoutError = exceptions.ConnectTimeoutError
MaxRetryError = exceptions.MaxRetryError
ProtocolError = exceptions.ProtocolError
ReadTimeoutError = exceptions.ReadTimeoutError
ResponseError = exceptions.ResponseError

log = ...  # type: Any

class Retry:
    DEFAULT_METHOD_WHITELIST = ...  # type: Any
    BACKOFF_MAX = ...  # type: Any
    total = ...  # type: Any
    connect = ...  # type: Any
    read = ...  # type: Any
    redirect = ...  # type: Any
    status_forcelist = ...  # type: Any
    method_whitelist = ...  # type: Any
    backoff_factor = ...  # type: Any
    raise_on_redirect = ...  # type: Any
    def __init__(self, total=..., connect=..., read=..., redirect=..., method_whitelist=..., status_forcelist=..., backoff_factor=..., raise_on_redirect=..., _observed_errors=...) -> None: ...
    def new(self, **kw): ...
    @classmethod
    def from_int(cls, retries, redirect=..., default=...): ...
    def get_backoff_time(self): ...
    def sleep(self): ...
    def is_forced_retry(self, method, status_code): ...
    def is_exhausted(self): ...
    def increment(self, method=..., url=..., response=..., error=..., _pool=..., _stacktrace=...): ...
