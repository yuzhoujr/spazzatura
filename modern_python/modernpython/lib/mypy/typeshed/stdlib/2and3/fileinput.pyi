from typing import Iterable, Callable, IO, AnyStr, Generic, Any, Text, Union, Iterator, Optional

import os
import sys

if sys.version_info >= (3, 6):
    _Path = Union[Text, bytes, os.PathLike[Any]]
else:
    _Path = Union[Text, bytes]


def input(
    files: Union[_Path, Iterable[_Path], None] = ...,
    inplace: bool = ...,
    backup: str = ...,
    bufsize: int = ...,
    mode: str = ...,
    openhook: Callable[[_Path, str], IO[AnyStr]] = ...) -> Iterable[AnyStr]: ...


def close() -> None: ...
def nextfile() -> None: ...
def filename() -> str: ...
def lineno() -> int: ...
def filelineno() -> int: ...
def fileno() -> int: ...
def isfirstline() -> bool: ...
def isstdin() -> bool: ...

class FileInput(Iterable[AnyStr], Generic[AnyStr]):
    def __init__(
        self,
        files: Union[None, _Path, Iterable[_Path]] = ...,
        inplace: bool = ...,
        backup: str = ...,
        bufsize: int = ...,
        mode: str = ...,
        openhook: Callable[[_Path, str], IO[AnyStr]] = ...
    ) -> None: ...

    def __del__(self) -> None: ...
    def close(self) -> None: ...
    if sys.version_info >= (3, 2):
        def __enter__(self) -> FileInput[AnyStr]: ...
        def __exit__(self, type: Any, value: Any, traceback: Any) -> None: ...
    def __iter__(self) -> Iterator[AnyStr]: ...
    def __next__(self) -> AnyStr: ...
    def __getitem__(self, i: int) -> AnyStr: ...
    def nextfile(self) -> None: ...
    def readline(self) -> AnyStr: ...
    def filename(self) -> str: ...
    def lineno(self) -> int: ...
    def filelineno(self) -> int: ...
    def fileno(self) -> int: ...
    def isfirstline(self) -> bool: ...
    def isstdin(self) -> bool: ...

def hook_compressed(filename: _Path, mode: str) -> IO[Any]: ...
if sys.version_info >= (3, 6):
    def hook_encoded(encoding: str, errors: Optional[str] = ...) -> Callable[[_Path, str], IO[Any]]: ...
else:
    def hook_encoded(encoding: str) -> Callable[[_Path, str], IO[Any]]: ...
