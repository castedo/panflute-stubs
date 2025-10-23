from __future__ import annotations

from _typeshed import Incomplete
from collections.abc import Iterable, Iterator, Mapping, MutableMapping, MutableSequence
from typing import Literal, Never, NoReturn, TypeAlias, overload

# from .table_elements import Caption
Caption: TypeAlias = Incomplete

from .base import Block, Element, Inline, MetaValue, _JsonData


_BuiltinType: TypeAlias = _JsonData | Inline | Block

_ApiVersionTuple: TypeAlias = (
    tuple[int, int] | tuple[int, int, int] | tuple[int, int, int, int]
)


class Doc(Element):
    content: MutableSequence[Block]
    metadata: MetaMap
    format: str
    api_version: _ApiVersionTuple
    pandoc_version: tuple[int, int, int, int]
    pandoc_reader_options: _JsonData

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


class Space(Inline):
    def __init__(self, *args: Never): ...


class HorizontalRule(Block):
    def __init__(self, *args: Never): ...


class SoftBreak(Inline):
    def __init__(self, *args: Never): ...


class LineBreak(Inline):
    def __init__(self, *args: Never): ...


class Plain(Block):
    content: MutableSequence[Inline]

    def __init__(self, *args: Inline): ...


class Para(Block):
    content: MutableSequence[Inline]

    def __init__(self, *args: Inline): ...


class BlockQuote(Block):
    content: MutableSequence[Block]

    def __init__(self, *args: Block): ...


class Emph(Inline):
    content: MutableSequence[Inline]

    def __init__(self, *args: Inline): ...


class Strong(Inline):
    content: MutableSequence[Inline]

    def __init__(self, *args: Inline): ...


class Underline(Inline):
    content: MutableSequence[Inline]

    def __init__(self, *args: Inline): ...


class Strikeout(Inline):
    content: MutableSequence[Inline]

    def __init__(self, *args: Inline): ...


class Superscript(Inline):
    content: MutableSequence[Inline]

    def __init__(self, *args: Inline): ...


class Subscript(Inline):
    content: MutableSequence[Inline]

    def __init__(self, *args: Inline): ...


class SmallCaps(Inline):
    content: MutableSequence[Inline]

    def __init__(self, *args: Inline): ...


class Note(Inline):
    content: MutableSequence[Block]

    def __init__(self, *args: Block): ...


class Header(Block):
    content: MutableSequence[Inline]
    level: int
    identifier: str
    classes: list[str]
    attributes: dict[str, str]

    def __init__(
        self,
        *args: Inline,
        level: int = 1,
        identifier: str = '',
        classes: Iterable[str] = [],
        attributes: Mapping[str, str] = {},
    ): ...


class Div(Block):
    content: MutableSequence[Block]
    identifier: str
    classes: list[str]
    attributes: dict[str, str]

    def __init__(
        self,
        *args: Block,
        identifier: str = '',
        classes: Iterable[str] = [],
        attributes: Mapping[str, str] = {},
    ): ...


class Span(Inline):
    content: MutableSequence[Inline]
    identifier: str
    classes: list[str]
    attributes: dict[str, str]

    def __init__(
        self,
        *args: Inline,
        identifier: str = '',
        classes: Iterable[str] = [],
        attributes: Mapping[str, str] = {},
    ): ...


class Quoted(Inline):
    content: MutableSequence[Inline]
    quote_type: _QuoteTypes

    def __init__(self, *args: Inline, quote_type: _QuoteTypes = 'DoubleQuote'): ...


class Cite(Inline):
    citations: MutableSequence[Citation]

    def __init__(self, *args: Inline, citations: Iterable[Citation] = []) -> None: ...


class Citation(Element):
    id: str
    mode: _CitationMode
    hash: int
    note_num: int
    prefix: MutableSequence[Inline]
    suffix: MutableSequence[Inline]

    def __init__(
        self,
        id: str,
        mode: _CitationMode = 'NormalCitation',
        prefix: Iterator[Inline] | Literal[''] = '',
        suffix: Iterator[Inline] | Literal[''] = '',
        hash: int = 0,
        note_num: int = 0,
    ) -> None: ...

    def to_json_legacy(self) -> NoReturn: ...


class Link(Inline):
    content: MutableSequence[Inline]
    url: str
    title: str
    identifier: str
    classes: list[str]
    attributes: dict[str, str]

    def __init__(
        self,
        *args: Inline,
        url: str = '',
        title: str = '',
        identifier: str = '',
        classes: Iterable[str] = [],
        attributes: Mapping[str, str] = {},
    ): ...


class Image(Inline):
    content: MutableSequence[Inline]
    url: str
    title: str
    identifier: str
    classes: list[str]
    attributes: dict[str, str]

    def __init__(
        self,
        *args: Inline,
        url: str = '',
        title: str = '',
        identifier: str = '',
        classes: Iterable[str] = [],
        attributes: Mapping[str, str] = {},
    ): ...


class Str(Inline):
    text: str

    def __init__(self, text: str): ...


class CodeBlock(Block):
    text: str
    identifier: str
    classes: list[str]
    attributes: dict[str, str]

    def __init__(
        self,
        text: str,
        identifier: str = '',
        classes: Iterable[str] = [],
        attributes: Mapping[str, str] = {},
    ) -> None: ...


class RawBlock(Block):
    text: str
    format: _RawFormats

    def __init__(self, text: str, format: _RawFormats = 'html'): ...


class Code(Inline):
    text: str
    identifier: str
    classes: list[str]
    attributes: dict[str, str]

    def __init__(
        self,
        text: str,
        identifier: str = '',
        classes: Iterable[str] = [],
        attributes: Mapping[str, str] = {},
    ) -> None: ...


class Math(Inline):
    text: str
    format: _MathFormats

    def __init__(self, text: str, format: _MathFormats = 'DisplayMath'): ...


class RawInline(Inline):
    text: str
    format: _RawFormats

    def __init__(self, text: str, format: _RawFormats = 'html'): ...


class ListItem(Element):
    content: MutableSequence[Block]

    def __init__(self, *args: Block): ...


class BulletList(Block):
    content: MutableSequence[ListItem]

    def __init__(self, *args: ListItem): ...


class OrderedList(Block):
    content: MutableSequence[ListItem]
    start: int
    style: _ListNumberStyles
    delimiter: _ListNumberDelimiters

    def __init__(
        self,
        *args: ListItem,
        start: int = 1,
        style: _ListNumberStyles = 'Decimal',
        delimiter: _ListNumberDelimiters = 'Period',
    ): ...


class Definition(Element):
    content: MutableSequence[Block]

    def __init__(self, *args: Block): ...


class DefinitionItem(Element):
    term: MutableSequence[Inline]
    definitions: MutableSequence[Definition]

    def __init__(self, term: Iterable[Inline], definitions: Iterable[Definition]): ...


class DefinitionList(Block):
    content: MutableSequence[DefinitionItem]

    def __init__(self, *args: DefinitionItem): ...


class LineItem(Element):
    content: MutableSequence[Inline]

    def __init__(self, *args: Inline): ...


class LineBlock(Block):
    content: MutableSequence[LineItem]

    def __init__(self, *args: LineItem): ...


class Figure(Block):
    content: MutableSequence[Block]
    caption: Caption
    identifier: str
    classes: list[str]
    attributes: dict[str, str]

    def __init__(
        self,
        *args: Block,
        caption: Caption | None = None,
        identifier: str = '',
        classes: Iterable[str] = [],
        attributes: Mapping[str, str] = {},
    ): ...


class MetaList(MetaValue, MutableSequence):
    # MetaList inherits from both Element and MutableSequence.
    # Element.index is a property, but MutableSequence.index is a function.
    # So MetaList.index is given the type hint Never so that using it gives an error.
    # https://github.com/sergiocorreia/panflute/issues/258

    index: Never

    content: MutableSequence[MetaValue]

    def __init__(self, *args: MetaValue | _BuiltinType): ...

    def __len__(self) -> int: ...

    def insert(self, i: int, v: MetaValue | _BuiltinType) -> None: ...

    # NOTE: MetaList does not implement MutableSequence methods that accept slice,
    # so those method type hints return NoReturn.
    # https://github.com/sergiocorreia/panflute/issues/260

    @overload
    def __delitem__(self, i: int) -> None: ...

    @overload
    def __delitem__(self, s: slice[int, int, int]) -> NoReturn: ...

    @overload
    def __getitem__(self, i: int) -> MetaValue: ...

    @overload
    def __getitem__(self, s: slice[int, int, int]) -> NoReturn: ...

    @overload
    def __setitem__(self, i: int, v: MetaValue | _BuiltinType) -> None: ...

    @overload
    def __setitem__(
        self, s: slice[int, int, int], v: Iterable[MetaValue | _BuiltinType]
    ) -> NoReturn: ...


class MetaMap(MetaValue, MutableMapping):
    content: MutableMapping[str, MetaValue]

    def __init__(
        self,
        *args: tuple[str, MetaValue | _BuiltinType],
        **kwargs: MetaValue | _BuiltinType,
    ): ...

    def __delitem__(self, k: str) -> None: ...
    def __getitem__(self, k: str) -> MetaValue: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[str]: ...
    def __setitem__(self, k: str, v: MetaValue | _BuiltinType) -> None: ...


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
_ListNumberStyles: TypeAlias = Literal[
    'DefaultStyle',
    'Example',
    'Decimal',
    'LowerRoman',
    'UpperRoman',
    'LowerAlpha',
    'UpperAlpha',
]

LIST_NUMBER_DELIMITERS: set[str]
_ListNumberDelimiters: TypeAlias = Literal[
    'DefaultDelim', 'Period', 'OneParen', 'TwoParens'
]

QUOTE_TYPES: set[str]
_QuoteTypes: TypeAlias = Literal['SingleQuote', 'DoubleQuote']

CITATION_MODE: set[str]
_CitationMode: TypeAlias = Literal['AuthorInText', 'SuppressAuthor', 'NormalCitation']

MATH_FORMATS: set[str]
_MathFormats: TypeAlias = Literal['DisplayMath', 'InlineMath']

RAW_FORMATS: set[str]
_RawFormats: TypeAlias = Literal[
    'tex',
    'latex',
    'html',
    'context',
    'rtf',
    'opendocument',
    'noteref',
    'openxml',
    'icml',
    'commonmark',
    'creole',
    'docbook',
    'docx',
    'dokuwiki',
    'epub',
    'fb2',
    'gfm',
    'haddock',
    'ipynb',
    'jats',
    'json',
    'man',
    'markdown',
    'markdown_github',
    'markdown_mmd',
    'markdown_phpextra',
    'markdown_strict',
    'mediawiki',
    'muse',
    'native',
    'odt',
    'opml',
    'org',
    'rst',
    't2t',
    'textile',
    'tikiwiki',
    'twiki',
    'vimwiki',
]

SPECIAL_ELEMENTS: set[str]
EMPTY_ELEMENTS: set[Element]


def from_json(data: _JsonData) -> Incomplete: ...


def builtin2meta(val: _BuiltinType) -> MetaValue: ...
