#!/usr/bin/env -S just --justfile

# https://just.systems

default:
    just --list

test:
    # stubtest installed with mypy
    PYTHONPATH=. stubtest --allowlist stubtest-ignore.txt panflute
