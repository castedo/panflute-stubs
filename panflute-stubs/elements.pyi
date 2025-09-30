from collections.abc import MutableSequence
from typing import Any, TypeAlias

from .base import Block, Element, Inline, _JSONType


_ApiVersionTuple: TypeAlias = (
    tuple[int, int] | tuple[int, int, int] | tuple[int, int, int, int]
)


class Doc(Element):
    format: str
    api_version: _ApiVersionTuple
    pandoc_version: tuple[int, int, int, int]
    pandoc_reader_options: _JSONType

    def __init__(
        self,
        *args: Block,
        metadata: dict[str, Any] = {},
        format: str = 'html',
        api_version: _ApiVersionTuple = (1, 23),
    ): ...

    @property
    def metadata(self) -> dict[str, Any]: ...

    def get_metadata(
        self, key: str = '', default: Any = None, builtin: bool = True
    ) -> Any: ...

    @property
    def content(self) -> MutableSequence[Block]: ...


class Space(Inline):
    ...


class Para(Block):
    def __init__(self, *args: Inline): ...

    @property
    def content(self) -> MutableSequence[Inline]: ...


class Emph(Inline):
    def __init__(self, *args: Inline): ...

    @property
    def content(self) -> MutableSequence[Inline]: ...


class Strong(Inline):
    def __init__(self, *args: Inline): ...

    @property
    def content(self) -> MutableSequence[Inline]: ...


class Str(Inline):
    text: str

    def __init__(self, text: str): ...
