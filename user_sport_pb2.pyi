from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserName(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class Sports(_message.Message):
    __slots__ = ["user", "tr", "sp", "st"]
    class Trener(_message.Message):
        __slots__ = ["fio"]
        FIO_FIELD_NUMBER: _ClassVar[int]
        fio: str
        def __init__(self, fio: _Optional[str] = ...) -> None: ...
    class StEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Sports.Trener
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Sports.Trener, _Mapping]] = ...) -> None: ...
    USER_FIELD_NUMBER: _ClassVar[int]
    TR_FIELD_NUMBER: _ClassVar[int]
    SP_FIELD_NUMBER: _ClassVar[int]
    ST_FIELD_NUMBER: _ClassVar[int]
    user: str
    tr: Sports.Trener
    sp: str
    st: _containers.MessageMap[str, Sports.Trener]
    def __init__(self, user: _Optional[str] = ..., tr: _Optional[_Union[Sports.Trener, _Mapping]] = ..., sp: _Optional[str] = ..., st: _Optional[_Mapping[str, Sports.Trener]] = ...) -> None: ...

class MaxRequest(_message.Message):
    __slots__ = ["c"]
    C_FIELD_NUMBER: _ClassVar[int]
    c: int
    def __init__(self, c: _Optional[int] = ...) -> None: ...

class AllSport(_message.Message):
    __slots__ = ["spt"]
    SPT_FIELD_NUMBER: _ClassVar[int]
    spt: _containers.RepeatedCompositeFieldContainer[Sports]
    def __init__(self, spt: _Optional[_Iterable[_Union[Sports, _Mapping]]] = ...) -> None: ...
