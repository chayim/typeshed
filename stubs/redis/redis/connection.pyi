from redis.backoff import NoBackoff as NoBackoff
from redis.exceptions import (
    AuthenticationError as AuthenticationError,
    AuthenticationWrongNumberOfArgsError as AuthenticationWrongNumberOfArgsError,
    BusyLoadingError as BusyLoadingError,
    ChildDeadlockedError as ChildDeadlockedError,
    ConnectionError as ConnectionError,
    DataError as DataError,
    ExecAbortError as ExecAbortError,
    InvalidResponse as InvalidResponse,
    ModuleError as ModuleError,
    NoPermissionError as NoPermissionError,
    NoScriptError as NoScriptError,
    ReadOnlyError as ReadOnlyError,
    RedisError as RedisError,
    ResponseError as ResponseError,
    TimeoutError as TimeoutError,
)
from redis.retry import Retry as Retry
from redis.utils import HIREDIS_AVAILABLE as HIREDIS_AVAILABLE, str_if_bytes as str_if_bytes
from typing import Any

ssl_available: bool
NONBLOCKING_EXCEPTION_ERROR_NUMBERS: Any
NONBLOCKING_EXCEPTIONS: Any
hiredis_version: Any
HIREDIS_SUPPORTS_CALLABLE_ERRORS: Any
HIREDIS_SUPPORTS_BYTE_BUFFER: Any
HIREDIS_SUPPORTS_ENCODING_ERRORS: Any
HIREDIS_USE_BYTE_BUFFER: bool
msg: str
SYM_STAR: bytes
SYM_DOLLAR: bytes
SYM_CRLF: bytes
SYM_EMPTY: bytes
SERVER_CLOSED_CONNECTION_ERROR: str
SENTINEL: Any
MODULE_LOAD_ERROR: str
NO_SUCH_MODULE_ERROR: str
MODULE_UNLOAD_NOT_POSSIBLE_ERROR: str
MODULE_EXPORTS_DATA_TYPES_ERROR: str

class Encoder:
    encoding: Any
    encoding_errors: Any
    decode_responses: Any
    def __init__(self, encoding, encoding_errors, decode_responses) -> None: ...
    def encode(self, value): ...
    def decode(self, value, force: bool = ...): ...

class BaseParser:
    EXCEPTION_CLASSES: Any
    def parse_error(self, response): ...

class SocketBuffer:
    socket_read_size: Any
    socket_timeout: Any
    bytes_written: int
    bytes_read: int
    def __init__(self, socket, socket_read_size, socket_timeout) -> None: ...
    @property
    def length(self): ...
    def can_read(self, timeout): ...
    def read(self, length): ...
    def readline(self): ...
    def purge(self) -> None: ...
    def close(self) -> None: ...

class PythonParser(BaseParser):
    socket_read_size: Any
    encoder: Any
    def __init__(self, socket_read_size) -> None: ...
    def __del__(self) -> None: ...
    def on_connect(self, connection) -> None: ...
    def on_disconnect(self) -> None: ...
    def can_read(self, timeout): ...
    def read_response(self): ...

class HiredisParser(BaseParser):
    socket_read_size: Any
    def __init__(self, socket_read_size) -> None: ...
    def __del__(self) -> None: ...
    def on_connect(self, connection) -> None: ...
    def on_disconnect(self) -> None: ...
    def can_read(self, timeout): ...
    def read_from_socket(self, timeout=..., raise_on_timeout: bool = ...): ...
    def read_response(self): ...

DefaultParser = HiredisParser
DefaultParser = PythonParser

class Connection:
    pid: Any
    host: Any
    port: Any
    db: Any
    username: Any
    client_name: Any
    password: Any
    socket_timeout: Any
    socket_connect_timeout: Any
    socket_keepalive: Any
    socket_keepalive_options: Any
    socket_type: Any
    retry_on_timeout: Any
    retry: Any
    health_check_interval: Any
    next_health_check: int
    encoder: Any
    def __init__(
        self,
        host: str = ...,
        port: int = ...,
        db: int = ...,
        password: Any | None = ...,
        socket_timeout: Any | None = ...,
        socket_connect_timeout: Any | None = ...,
        socket_keepalive: bool = ...,
        socket_keepalive_options: Any | None = ...,
        socket_type: int = ...,
        retry_on_timeout: bool = ...,
        encoding: str = ...,
        encoding_errors: str = ...,
        decode_responses: bool = ...,
        parser_class=...,
        socket_read_size: int = ...,
        health_check_interval: int = ...,
        client_name: Any | None = ...,
        username: Any | None = ...,
        retry: Any | None = ...,
    ) -> None: ...
    def repr_pieces(self): ...
    def __del__(self) -> None: ...
    def register_connect_callback(self, callback) -> None: ...
    def clear_connect_callbacks(self) -> None: ...
    def connect(self) -> None: ...
    def on_connect(self) -> None: ...
    def disconnect(self) -> None: ...
    def check_health(self) -> None: ...
    def send_packed_command(self, command, check_health: bool = ...) -> None: ...
    def send_command(self, *args, **kwargs) -> None: ...
    def can_read(self, timeout: int = ...): ...
    def read_response(self): ...
    def pack_command(self, *args): ...
    def pack_commands(self, commands): ...

class SSLConnection(Connection):
    keyfile: Any
    certfile: Any
    cert_reqs: Any
    ca_certs: Any
    check_hostname: Any
    def __init__(
        self,
        ssl_keyfile: Any | None = ...,
        ssl_certfile: Any | None = ...,
        ssl_cert_reqs: str = ...,
        ssl_ca_certs: Any | None = ...,
        ssl_check_hostname: bool = ...,
        **kwargs,
    ) -> None: ...

class UnixDomainSocketConnection(Connection):
    pid: Any
    path: Any
    db: Any
    username: Any
    client_name: Any
    password: Any
    socket_timeout: Any
    retry_on_timeout: Any
    retry: Any
    health_check_interval: Any
    next_health_check: int
    encoder: Any
    def __init__(
        self,
        path: str = ...,
        db: int = ...,
        username: Any | None = ...,
        password: Any | None = ...,
        socket_timeout: Any | None = ...,
        encoding: str = ...,
        encoding_errors: str = ...,
        decode_responses: bool = ...,
        retry_on_timeout: bool = ...,
        parser_class=...,
        socket_read_size: int = ...,
        health_check_interval: int = ...,
        client_name: Any | None = ...,
        retry: Any | None = ...,
    ) -> None: ...
    def repr_pieces(self): ...

FALSE_STRINGS: Any

def to_bool(value): ...

URL_QUERY_ARGUMENT_PARSERS: Any

def parse_url(url): ...

class ConnectionPool:
    @classmethod
    def from_url(cls, url, **kwargs): ...
    connection_class: Any
    connection_kwargs: Any
    max_connections: Any
    def __init__(self, connection_class=..., max_connections: Any | None = ..., **connection_kwargs) -> None: ...
    pid: Any
    def reset(self) -> None: ...
    def get_connection(self, command_name, *keys, **options): ...
    def get_encoder(self): ...
    def make_connection(self): ...
    def release(self, connection) -> None: ...
    def owns_connection(self, connection): ...
    def disconnect(self, inuse_connections: bool = ...) -> None: ...

class BlockingConnectionPool(ConnectionPool):
    queue_class: Any
    timeout: Any
    def __init__(
        self, max_connections: int = ..., timeout: int = ..., connection_class=..., queue_class=..., **connection_kwargs
    ) -> None: ...
    pool: Any
    pid: Any
    def reset(self) -> None: ...
    def make_connection(self): ...
    def get_connection(self, command_name, *keys, **options): ...
    def release(self, connection) -> None: ...
    def disconnect(self) -> None: ...
