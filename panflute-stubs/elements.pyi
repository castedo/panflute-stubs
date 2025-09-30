from __future__ import annotations

from _typeshed import Incomplete
from collections.abc import Iterable, Mapping, MutableMapping, MutableSequence
from typing import TypeAlias

from .base import Block, Element, Inline, MetaValue, _JSONType


_BuiltinType: TypeAlias = _JSONType | Inline | Block

_ApiVersionTuple: TypeAlias = (
    tuple[int, int] | tuple[int, int, int] | tuple[int, int, int, int]
)


class Doc(Element):
    content: MutableSequence[Block]
    metadata: MetaMap
    format: str
    api_version: _ApiVersionTuple
    pandoc_version: tuple[int, int, int, int]
    pandoc_reader_options: _JSONType

    def __init__(
        self,
        *args: Block,
        metadata: Mapping[str, MetaValue] | MetaMap = {},
        format: str = 'html',
        api_version: _ApiVersionTuple = (1, 23),
    ): ...

    def get_metadata(
        self,
        key: str = '',
        default: _BuiltinType | MetaValue | None = None,
        builtin: bool = True,
    ) -> _BuiltinType | MetaValue: ...


class Space(Inline): ...


class Para(Block):
    content: MutableSequence[Inline]

    def __init__(self, *args: Inline): ...


class Emph(Inline):
    content: MutableSequence[Inline]

    def __init__(self, *args: Inline): ...


class Strong(Inline):
    content: MutableSequence[Inline]

    def __init__(self, *args: Inline): ...


class Header(Block):
    content: MutableSequence[Inline]
    level: int
    identifier: str
    classes: list[str]
    attributes: dict[str, str]

    def __init__(
        self,
        *args: Iterable[Inline],
        level: int = 1,
        identifier: str = '',
        classes: Iterable[str] = [],
        attributes: Mapping[str, str] = {},
    ): ...


class Str(Inline):
    text: str

    def __init__(self, text: str): ...


class MetaList(MetaValue):
    content: MutableSequence[MetaValue]

    def __init__(self, *args: MetaValue | _BuiltinType): ...


class MetaMap(MetaValue):
    content: MutableMapping[str, MetaValue]

    def __init__(
        self,
        *args: tuple[str, MetaValue | _BuiltinType],
        **kwargs: tuple[str, MetaValue | _BuiltinType],
    ): ...


class MetaInlines(MetaValue):
    content: MutableSequence[Inline]

    def __init__(self, *args: Inline) -> None: ...


class MetaBlocks(MetaValue):
    content: MutableSequence[Block]

    def __init__(self, *args: Block) -> None: ...


class MetaString(MetaValue):
    text: str

    def __init__(self, text: str): ...


class MetaBool(MetaValue):
    boolean: bool

    def __init__(self, boolean: bool): ...


LIST_NUMBER_STYLES: set[str]
LIST_NUMBER_DELIMITERS: set[str]
QUOTE_TYPES: set[str]
CITATION_MODE: set[str]
MATH_FORMATS: set[str]
RAW_FORMATS: set[str]
SPECIAL_ELEMENTS: set[str]
EMPTY_ELEMENTS: set[Element]


def from_json(data: _JSONType) -> Incomplete: ...


def builtin2meta(val: _BuiltinType) -> MetaValue: ...
