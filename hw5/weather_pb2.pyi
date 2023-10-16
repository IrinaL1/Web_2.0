from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Weather(_message.Message):
    __slots__ = ["deg", "defin"]
    DEG_FIELD_NUMBER: _ClassVar[int]
    DEFIN_FIELD_NUMBER: _ClassVar[int]
    deg: int
    defin: str
    def __init__(self, deg: _Optional[int] = ..., defin: _Optional[str] = ...) -> None: ...
