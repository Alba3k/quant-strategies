import pandas as pd
import pandas_ta as ta
import numpy as np

def ema_rsi_strategy(df, ema_fast=13, ema_slow=30, rsi_period=14, rsi_threshold=50):
    """
    EMA + RSI Strategy

    This strategy combines two exponential moving averages (EMA13 and EMA30)
    with the Relative Strength Index (RSI) to generate directional signals.

    Signal Logic:
    - Long: EMA13 > EMA30 and RSI > 50
    - Short: EMA13 < EMA30 and RSI < 50

    Parameters:
    - df (pd.DataFrame): OHLCV data with 'close' column
    - ema_fast (int): Fast EMA period (default: 13)
    - ema_slow (int): Slow EMA period (default: 30)
    - rsi_period (int): RSI calculation period (default: 14)
    - rsi_threshold (float): RSI threshold for signal (default: 50)

    Returns:
    - pd.DataFrame: Original DataFrame with added columns:
        ['EMA13', 'EMA30', 'RSI', 'EMA_Signal', 'RSI_Signal', 'Position']
    """

    # Calculate EMAs
    df["EMA13"] = df["close"].ewm(span=ema_fast).mean()
    df["EMA30"] = df["close"].ewm(span=ema_slow).mean()

    # Calculate RSI
    df["RSI"] = ta.rsi(df["close"], length=rsi_period)

    # Generate signals
    df["EMA_Signal"] = np.where(df["EMA13"] > df["EMA30"], 1, -1)
    df["RSI_Signal"] = np.where(df["RSI"] > rsi_threshold, 1, -1)
    df["Position"] = df["EMA_Signal"] & df["RSI_Signal"]

    return df