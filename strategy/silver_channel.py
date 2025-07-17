import pandas as pd
import numpy as np

def silver_channel_strategy(df, period=20):
    """
    Silver Channel Strategy

    Signal Logic:
    - Long: Bounce from lower channel
    - Short: Bounce from upper channel

    Returns:
    - df with ['High_Channel', 'Low_Channel', 'Position']
    """
    df["High_Channel"] = df["high"].rolling(window=period).max()
    df["Low_Channel"] = df["low"].rolling(window=period).min()

    df["Position"] = np.where(df["close"] <= df["Low_Channel"], 1,
                              np.where(df["close"] >= df["High_Channel"], -1, 0))
    return df
