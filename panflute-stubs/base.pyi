from __future__ import annotations
from collections.abc import Mapping, Sequence

from typing import Callable, Never, TYPE_CHECKING, TypeAlias

from _typeshed import (
    Incomplete as DictContainer,
    Incomplete as ListContainer,
)

if TYPE_CHECKING:
    from .elements import Doc


_JsonData: TypeAlias = (
    None | str | int | float | list['_JsonData'] | dict[str, '_JsonData']
)


class Element:
    parent: Element | None
    location: str | None
    index: int | None

    def __new__(cls, *args: Never, **kwargs: Never): ...

    @property
    def tag(self) -> str: ...

    def to_json(self) -> dict[str, _JsonData]: ...

    @property
    def doc(self) -> Doc | None: ...

    def walk(
        self,
        action: Callable[[Element, Doc], Element],
        doc: Doc | None = None,
        stop_if: Callable[[Element], bool] | None = None,
    ) -> Element | list[Never] | None: ...

    @property
    def content(self) -> Sequence[Element] | Mapping[str, MetaValue]: ...

    def ancestor(self, n: int) -> Element | None: ...

    def offset(self, n: int) -> Element | None: ...

    @property
    def prev(self) -> Element | None: ...

    @property
    def next(self) -> Element | None: ...

    def replace_keyword(
        self, keyword: str, replacement: Element, count: int = 0
    ) -> None: ...

    @property
    def container(self) -> ListContainer | DictContainer | None: ...


class Inline(Element): ...


class Block(Element): ...


class MetaValue(Element): ...
