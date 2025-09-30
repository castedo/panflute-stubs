Python typing stub files for the panflute package
=================================================

Add this directory to `PYTHONPATH` when you run a type checker like
[mypy](https://mypy-lang.org/) to type check your code that calls
[panflute](https://scorreia.com/software/panflute/).

For example:
```
git clone git@github.com:castedo/panflute-stubs.git ~/repos/panflute-stubs
PYTHONPATH=~/repos/panflute-stubs mypy --strict myproject
```

Mypy (and others) will find and use the module `panflute-stubs` in this directory as
type hints for the Python panflute package.


Status
------

As of September 2025, these stub files do not yet type most of the classes and methods of
panflute.

The file <stubtest-ignore.txt> provides a good summary of what is not currently typed.

Pull requests are welcome for adding more type hints.
