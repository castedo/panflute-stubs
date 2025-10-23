from _typeshed import SupportsRead, SupportsWrite
from typing import Any, AnyStr, Callable, Iterable, Protocol

from .base import Element
from .elements import Doc


def load(input_stream: SupportsRead[AnyStr] | None = None) -> Doc: ...


def dump(doc: Doc, output_stream: SupportsWrite[str] | None = None) -> None: ...


class _Action(Protocol):
    def __call__(self, element: Element, doc: Doc, /, **kwags: Any) -> None: ...


def run_filters(
    actions: Iterable[_Action],
    prepare: Callable[[Element], None] | None = None,
    finalize: Callable[[Element], None] | None = None,
    input_stream: SupportsRead[AnyStr] | None = None,
    output_stream: SupportsWrite[str] | None = None,
    doc: Doc | None = None,
    stop_if: Callable[[Element], bool] | None = None,
    **kwargs: Any,
): ...


def run_filter(
    action: _Action,
    prepare: Callable[[Element], None] | None = None,
    finalize: Callable[[Element], None] | None = None,
    input_stream: SupportsRead[AnyStr] | None = None,
    output_stream: SupportsWrite[str] | None = None,
    doc: Doc | None = None,
    stop_if: Callable[[Element], bool] | None = None,
    **kwargs: Any,
): ...
