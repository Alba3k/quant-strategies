import pandas as pd
import numpy as np

def ema_regular_strategy(df, ema_fast=4, ema_slow=9):
    """
    EMA Regular Order Strategy

    Signal Logic:
    - Long: EMA(4) crosses above EMA(9)
    - Short: EMA(4) crosses below EMA(9)

    Returns:
    - df with ['EMA4', 'EMA9', 'Position']
    """
    df["EMA4"] = df["close"].ewm(span=ema_fast).mean()
    df["EMA9"] = df["close"].ewm(span=ema_slow).mean()

    df["Position"] = np.where(
        (df["EMA4"] > df["EMA9"]) & (df["EMA4"].shift(1) <= df["EMA9"].shift(1)), 1,
        np.where((df["EMA4"] < df["EMA9"]) & (df["EMA4"].shift(1) >= df["EMA9"].shift(1)), -1, 0)
    )
    return df
