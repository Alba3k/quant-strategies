import pandas as pd
import numpy as np

def silver_channel_strategy(df, period=20, buffer=0.001):
    """
    Silver Channel Strategy

    This strategy identifies price bounces from dynamic support/resistance levels
    based on recent highs and lows.

    Parameters:
    - df (pd.DataFrame): OHLCV data with 'high', 'low', 'close'
    - period (int): Lookback period for channel construction (default: 20)
    - buffer (float): Optional buffer zone to reduce false signals (default: 0.1%)

    Signal Logic:
    - Long: Price touches or dips below lower channel
    - Short: Price touches or exceeds upper channel

    Returns:
    - pd.DataFrame with ['High_Channel', 'Low_Channel', 'Position']
    """

    # Construct dynamic channel
    df["High_Channel"] = df["high"].rolling(window=period).max()
    df["Low_Channel"] = df["low"].rolling(window=period).min()

    # Apply buffer zone
    lower_threshold = df["Low_Channel"] * (1 - buffer)
    upper_threshold = df["High_Channel"] * (1 + buffer)

    # Generate signals
    df["Position"] = np.where(df["close"] <= lower_threshold, 1,
                              np.where(df["close"] >= upper_threshold, -1, 0))

    return df
