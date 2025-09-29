from __future__ import annotations

from typing import Any, Callable, Never, NoReturn


from _typeshed import (
    Incomplete as DictContainer,
    Incomplete as Doc,
    Incomplete as ListContainer,
)


class Element:
    def __new__(cls, *args: Never, **kwargs: Never): ...

    @property
    def tag(self) -> str: ...

    def to_json(self) -> dict[str, Any]: ...

    @property
    def parent(self) -> Element | None: ...

    @property
    def location(self) -> str | None: ...

    @property
    def doc(self) -> Doc | None: ...

    def walk(
        self,
        action: Callable[[Element, Doc], Element],
        doc: Doc | None = None,
        stop_if: Callable[[Element], bool] | None = None,
    ) -> Element | list[Never] | None: ...

    @property
    def content(self) -> NoReturn: ...

    @property
    def index(self) -> int | None: ...

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
