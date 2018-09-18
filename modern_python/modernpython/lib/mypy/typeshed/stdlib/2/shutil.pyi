from typing import List, Iterable, Callable, IO, AnyStr, Any, Optional, Tuple, Sequence

class Error(EnvironmentError): ...
class SpecialFileError(EnvironmentError): ...
class ExecError(EnvironmentError): ...

def copyfileobj(fsrc: IO[AnyStr], fdst: IO[AnyStr], length: int = ...) -> None: ...
def copyfile(src: unicode, dst: unicode) -> None: ...
def copymode(src: unicode, dst: unicode) -> None: ...
def copystat(src: unicode, dst: unicode) -> None: ...
def copy(src: unicode, dst: unicode) -> None: ...
def copy2(src: unicode, dst: unicode) -> None: ...
def ignore_patterns(*patterns: AnyStr) -> Callable[[AnyStr, List[AnyStr]], Iterable[AnyStr]]: ...
def copytree(src: AnyStr, dst: AnyStr, symlinks: bool = ...,
             ignore: Optional[Callable[[AnyStr, List[AnyStr]], Iterable[AnyStr]]] = ...) -> None: ...
def rmtree(path: AnyStr, ignore_errors: bool = ...,
           onerror: Callable[[Any, AnyStr, Any], None] = ...) -> None: ...
def move(src: unicode, dst: unicode) -> None: ...
def get_archive_formats() -> List[Tuple[str, str]]: ...
def register_archive_format(name: str, function: Callable[..., Any],
                            extra_args: Sequence[Tuple[str, Any]] = ...,
                            description: str = ...) -> None: ...
def unregister_archive_format(name: str) -> None: ...
def make_archive(base_name: AnyStr, format: str, root_dir: unicode = ...,
                 base_dir: unicode = ..., verbose: int = ..., dry_run: int = ...,
                 owner: str = ..., group: str = ..., logger: Any = ...) -> AnyStr: ...
