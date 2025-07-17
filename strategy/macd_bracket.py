import pandas as pd
import numpy as np

def macd_bracket_strategy(df):
    """
    MACD Bracket Order Strategy

    Signal Logic:
    - Long: MACD crosses above Signal
    - Short: MACD crosses below Signal

    Returns:
    - df with ['MACD', 'Signal', 'Position']
    """
    df["MACD"] = df["close"].ewm(span=12).mean() - df["close"].ewm(span=26).mean()
    df["Signal"] = df["MACD"].ewm(span=9).mean()

    df["Position"] = np.where(
        (df["MACD"] > df["Signal"]) & (df["MACD"].shift(1) <= df["Signal"].shift(1)), 1,
        np.where((df["MACD"] < df["Signal"]) & (df["MACD"].shift(1) >= df["Signal"].shift(1)), -1, 0)
    )
    return df
