import pandas as pd
import numpy as np

def rsi_divergence_strategy(df, rsi_period=14, lookback=2):
    """
    RSI Divergence Strategy (Enhanced)

    Detects hidden bullish/bearish divergences between price and RSI.

    Signal Logic:
    - Long: Price makes lower low, RSI makes higher low
    - Short: Price makes higher high, RSI makes lower high

    Parameters:
    - rsi_period (int): RSI calculation period
    - lookback (int): Number of bars to compare for divergence

    Returns:
    - df with ['RSI', 'Position']
    """
    df["RSI"] = ta.rsi(df["close"], length=rsi_period)

    # Bullish divergence: price lower low, RSI higher low
    price_ll = df["close"] < df["close"].shift(lookback)
    rsi_hl = df["RSI"] > df["RSI"].shift(lookback)
    df["Bull_Div"] = price_ll & rsi_hl

    # Bearish divergence: price higher high, RSI lower high
    price_hh = df["close"] > df["close"].shift(lookback)
    rsi_lh = df["RSI"] < df["RSI"].shift(lookback)
    df["Bear_Div"] = price_hh & rsi_lh

    df["Position"] = np.where(df["Bull_Div"], 1,
                              np.where(df["Bear_Div"], -1, 0))

    return df
