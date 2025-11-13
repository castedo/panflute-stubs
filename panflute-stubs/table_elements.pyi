from __future__ import annotations

from collections.abc import Iterable, Mapping, MutableSequence
from typing import Literal, TypeAlias

from .base import Block, Element, Inline, _JsonData


_TableColSpec: TypeAlias = Iterable[tuple[_TableAlignment, _TableWidth]]


class Table(Block):
    identifier: str
    classes: list[str]
    attributes: dict[str, str]
    content: MutableSequence[TableBody]
    caption: Caption | None
    cols: int
    head: TableHead | None
    foot: TableFoot | None
    colspec: _TableColSpec

    def __init__(
        self,
        *args: TableBody,
        head: TableHead | None = None,
        foot: TableFoot | None = None,
        caption: Caption | None = None,
        colspec: _TableColSpec | None = None,
        identifier: str = '',
        classes: Iterable[str] = [],
        attributes: Mapping[str, str] = {},
    ): ...


class TableHead(Block):
    identifier: str
    classes: list[str]
    attributes: dict[str, str]
    content: MutableSequence[TableRow]

    def __init__(
        self,
        *args: TableRow,
        identifier: str = '',
        classes: Iterable[str] = [],
        attributes: Mapping[str, str] = {},
    ): ...


class TableFoot(Block):
    identifier: str
    classes: list[str]
    attributes: dict[str, str]
    content: MutableSequence[TableRow]

    def __init__(
        self,
        *args: TableRow,
        identifier: str = '',
        classes: Iterable[str] = [],
        attributes: Mapping[str, str] = {},
    ): ...


class TableBody(Block):
    identifier: str
    classes: list[str]
    attributes: dict[str, str]
    content: MutableSequence[TableRow]
    head: MutableSequence[TableRow]
    row_head_columns: int

    def __init__(
        self,
        *args: TableRow,
        head: Iterable[TableRow] | None = None,
        row_head_columns: int = 0,
        identifier: str = '',
        classes: Iterable[str] = [],
        attributes: Mapping[str, str] = {},
    ): ...


class TableRow(Element):
    identifier: str
    classes: list[str]
    attributes: dict[str, str]
    content: MutableSequence[TableCell]

    def __init__(
        self,
        *args: TableCell,
        identifier: str = '',
        classes: Iterable[str] = [],
        attributes: Mapping[str, str] = {},
    ): ...


class TableCell(Element):
    identifier: str
    classes: list[str]
    attributes: dict[str, str]
    content: MutableSequence[Block]
    alignment: _TableAlignment
    rowspan: int
    colspan: int

    def __init__(
        self,
        *args: Block,
        alignment: _TableAlignment = 'AlignDefault',
        rowspan: int = 1,
        colspan: int = 1,
        identifier: str = '',
        classes: Iterable[str] = [],
        attributes: Mapping[str, str] = {},
    ): ...


class Caption(Element):
    content: MutableSequence[Block]
    short_caption: MutableSequence[Inline] | None

    def __init__(self, *args: Block, short_caption: Iterable[Inline] | None = None): ...


def count_columns_in_row(row: TableRow) -> int: ...


def colspec_to_json(c: _JsonData) -> _JsonData: ...


def cell_from_json(c: _JsonData) -> TableCell: ...


def row_from_json(c: _JsonData) -> TableRow: ...


def body_from_json(c: _JsonData) -> TableBody: ...


def table_from_json(c: _JsonData) -> Table: ...


TABLE_ALIGNMENT: set[str]
_TableAlignment: TypeAlias = Literal[
    'AlignLeft', 'AlignRight', 'AlignCenter', 'AlignDefault'
]

TABLE_WIDTH: set[str]
_TableWidth: TypeAlias = Literal['ColWidthDefault']
