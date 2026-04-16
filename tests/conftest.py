import pandas as pd

def ts(s: str) -> pd.Timestamp:
    return pd.Timestamp(s, tz="UTC")
