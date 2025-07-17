import pandas as pd
import numpy as np

def triple_ema_strategy(df):
    """
    Triple EMA Momentum Strategy

    Identifies strong directional trends using three exponential moving averages.

    Signal Logic:
    - Buy (LONG): EMA7 > EMA21 > EMA50 (strong uptrend)
    - Sell (SHORT): EMA7 < EMA21 < EMA50 (strong downtrend)

    Parameters:
    - df (pd.DataFrame): OHLCV data with 'close'

    Returns:
    - pd.DataFrame: Original DataFrame with added columns:
        ['EMA7', 'EMA21', 'EMA50', 'Uptrend', 'Downtrend', 'Position']
    """

    # EMA calculations
    df['EMA7'] = df['close'].ewm(span=7).mean()
    df['EMA21'] = df['close'].ewm(span=21).mean()
    df['EMA50'] = df['close'].ewm(span=50).mean()

    # Trend signals
    df['Uptrend'] = (df['EMA7'] > df['EMA21']) & (df['EMA21'] > df['EMA50'])
    df['Downtrend'] = (df['EMA7'] < df['EMA21']) & (df['EMA21'] < df['EMA50'])

    # Final position
    df['Position'] = np.where(df['Uptrend'], 1, np.where(df['Downtrend'], -1, 0))

    return df
