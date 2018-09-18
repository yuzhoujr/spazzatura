from typing import Any

def default_stream_factory(total_content_length, filename, content_type, content_length=None): ...
def parse_form_data(environ, stream_factory=None, charset='', errors='', max_form_memory_size=None, max_content_length=None, cls=None, silent=True): ...
def exhaust_stream(f): ...

class FormDataParser:
    stream_factory = ...  # type: Any
    charset = ...  # type: Any
    errors = ...  # type: Any
    max_form_memory_size = ...  # type: Any
    max_content_length = ...  # type: Any
    cls = ...  # type: Any
    silent = ...  # type: Any
    def __init__(self, stream_factory=None, charset='', errors='', max_form_memory_size=None, max_content_length=None, cls=None, silent=True): ...
    def get_parse_func(self, mimetype, options): ...
    def parse_from_environ(self, environ): ...
    def parse(self, stream, mimetype, content_length, options=None): ...
    parse_functions = ...  # type: Any

def is_valid_multipart_boundary(boundary): ...
def parse_multipart_headers(iterable): ...

class MultiPartParser:
    stream_factory = ...  # type: Any
    charset = ...  # type: Any
    errors = ...  # type: Any
    max_form_memory_size = ...  # type: Any
    cls = ...  # type: Any
    buffer_size = ...  # type: Any
    def __init__(self, stream_factory=None, charset='', errors='', max_form_memory_size=None, cls=None, buffer_size=...): ...
    def fail(self, message): ...
    def get_part_encoding(self, headers): ...
    def get_part_charset(self, headers): ...
    def start_file_streaming(self, filename, headers, total_content_length): ...
    def in_memory_threshold_reached(self, bytes): ...
    def validate_boundary(self, boundary): ...
    def parse_lines(self, file, boundary, content_length): ...
    def parse_parts(self, file, boundary, content_length): ...
    def parse(self, file, boundary, content_length): ...
