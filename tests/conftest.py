import os as _os
import sys as _sys

# Make this conftest.py importable as a top-level `conftest` module so test
# modules can do `from conftest import ts`. Without this, the empty
# tests/__init__.py turns the dir into a package and shadows the bare import.
_HERE = _os.path.dirname(_os.path.abspath(__file__))
if _HERE not in _sys.path:
    _sys.path.insert(0, _HERE)

import pandas as pd


def ts(s: str) -> pd.Timestamp:
    return pd.Timestamp(s, tz="UTC")
