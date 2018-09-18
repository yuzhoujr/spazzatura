from collections import namedtuple
from typing import Any


_URLTuple = namedtuple(
    '_URLTuple',
    ['scheme', 'netloc', 'path', 'query', 'fragment']
)


class BaseURL(_URLTuple):
    def replace(self, **kwargs): ...
    @property
    def host(self): ...
    @property
    def ascii_host(self): ...
    @property
    def port(self): ...
    @property
    def auth(self): ...
    @property
    def username(self): ...
    @property
    def raw_username(self): ...
    @property
    def password(self): ...
    @property
    def raw_password(self): ...
    def decode_query(self, *args, **kwargs): ...
    def join(self, *args, **kwargs): ...
    def to_url(self): ...
    def decode_netloc(self): ...
    def to_uri_tuple(self): ...
    def to_iri_tuple(self): ...
    def get_file_location(self, pathformat=None): ...

class URL(BaseURL):
    def encode_netloc(self): ...
    def encode(self, charset='', errors=''): ...

class BytesURL(BaseURL):
    def encode_netloc(self): ...
    def decode(self, charset='', errors=''): ...

def url_parse(url, scheme=None, allow_fragments=True): ...
def url_quote(string, charset='', errors='', safe='', unsafe=''): ...
def url_quote_plus(string, charset='', errors='', safe=''): ...
def url_unparse(components): ...
def url_unquote(string, charset='', errors='', unsafe=''): ...
def url_unquote_plus(s, charset='', errors=''): ...
def url_fix(s, charset=''): ...
def uri_to_iri(uri, charset='', errors=''): ...
def iri_to_uri(iri, charset='', errors='', safe_conversion=False): ...
def url_decode(s, charset='', decode_keys=False, include_empty=True, errors='', separator='', cls=None): ...
def url_decode_stream(stream, charset='', decode_keys=False, include_empty=True, errors='', separator='', cls=None, limit=None, return_iterator=False): ...
def url_encode(obj, charset='', encode_keys=False, sort=False, key=None, separator=b''): ...
def url_encode_stream(obj, stream=None, charset='', encode_keys=False, sort=False, key=None, separator=b''): ...
def url_join(base, url, allow_fragments=True): ...

class Href:
    base = ...  # type: Any
    charset = ...  # type: Any
    sort = ...  # type: Any
    key = ...  # type: Any
    def __init__(self, base='', charset='', sort=False, key=None): ...
    def __getattr__(self, name): ...
    def __call__(self, *path, **query): ...
