import pandas as pd
import numpy as np

def atr_strategy(df):
    """
    ATR Trailing Stop Strategy

    Uses Average True Range (ATR) to define dynamic stop-loss levels
    after breakout entries.

    Signal Logic:
    - Long: Price breaks above previous 20-period high
    - Short: Price breaks below previous 20-period low
    - Stop-loss: 2 × ATR from entry price

    Parameters:
    - df (pd.DataFrame): OHLCV data with 'high', 'low', 'close'

    Returns:
    - pd.DataFrame: Original DataFrame with added columns:
        ['ATR', 'High_20', 'Low_20', 'Long', 'Short', 'Stop_Long', 'Stop_Short']
    """

    # ATR Calculation (14-period)
    high_low = df['high'] - df['low']
    high_close = np.abs(df['high'] - df['close'].shift(1))
    low_close = np.abs(df['low'] - df['close'].shift(1))
    tr = np.maximum(high_low, np.maximum(high_close, low_close))
    df['ATR'] = tr.rolling(window=14).mean()

    # Breakout levels
    df['High_20'] = df['high'].rolling(window=20).max()
    df['Low_20'] = df['low'].rolling(window=20).min()

    # Entry signals
    df['Long'] = df['close'] > df['High_20'].shift(1)
    df['Short'] = df['close'] < df['Low_20'].shift(1)

    # Stop-loss levels
    df['Stop_Long'] = df['close'] - 2 * df['ATR']
    df['Stop_Short'] = df['close'] + 2 * df['ATR']

    return df
