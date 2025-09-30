from _typeshed import SupportsRead, SupportsWrite

from .elements import Doc


def load(input_stream: SupportsRead[str | bytes] | None = None) -> Doc: ...


def dump(doc: Doc, output_stream: SupportsWrite | None = None) -> None: ...
