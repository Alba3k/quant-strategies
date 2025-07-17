import pandas as pd
import numpy as np

def stocha_price_strategy(df):
    """
    Stochastic + Price Action Strategy

    Combines momentum signals from the Stochastic oscillator with trend confirmation
    from the 50-period SMA.

    Signal Logic:
    - Buy (LONG): Price > SMA50 AND %K crosses above %D near oversold (≤ 20)
    - Sell (SHORT): Price < SMA50 AND %K crosses below %D near overbought (≥ 80)

    Parameters:
    - df (pd.DataFrame): OHLCV data with 'high', 'low', 'close'

    Returns:
    - pd.DataFrame: Original DataFrame with added columns:
        ['%K', '%D', 'SMA50', 'Stoch_Buy', 'Stoch_Sell', 'Price_Buy', 'Price_Sell', 'Position']
    """

    # Stochastic Oscillator
    high_14 = df['high'].rolling(window=14).max()
    low_14 = df['low'].rolling(window=14).min()
    df['%K'] = (df['close'] - low_14) / (high_14 - low_14) * 100
    df['%D'] = df['%K'].rolling(window=3).mean()

    # 50-period SMA
    df['SMA50'] = df['close'].rolling(window=50).mean()

    # Entry conditions
    df['Stoch_Buy'] = (df['%K'] > df['%D']) & (df['%K'].shift(1) <= 20)
    df['Stoch_Sell'] = (df['%K'] < df['%D']) & (df['%K'].shift(1) >= 80)
    df['Price_Buy'] = df['close'] > df['SMA50']
    df['Price_Sell'] = df['close'] < df['SMA50']

    # Final position
    df['Position'] = np.where(df['Stoch_Buy'] & df['Price_Buy'], 1,
                              np.where(df['Stoch_Sell'] & df['Price_Sell'], -1, 0))

    return df
