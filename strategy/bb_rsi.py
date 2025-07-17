import pandas as pd
import numpy as np

def bb_rsi_strategy(df):
    """
    Bollinger Bands + RSI Strategy

    This strategy combines Bollinger Band breakout signals with RSI confirmation
    to filter impulsive moves and avoid overbought/oversold traps.

    Signal Logic:
    - Long (BUY): Price breaks above upper Bollinger Band AND RSI < 70
    - Short (SELL): Price breaks below lower Bollinger Band AND RSI > 30

    Parameters:
    - df (pd.DataFrame): OHLCV data with 'close' column

    Returns:
    - pd.DataFrame: Original DataFrame with added columns:
        ['MA20', 'STD', 'Upper', 'Lower', 'RSI', 'BB_Signal', 'RSI_Confirm']
    """

    # Bollinger Bands (20-period SMA ± 2*STD)
    df['MA20'] = df['close'].rolling(window=20).mean()
    df['STD'] = df['close'].rolling(window=20).std()
    df['Upper'] = df['MA20'] + 2 * df['STD']
    df['Lower'] = df['MA20'] - 2 * df['STD']

    # RSI Calculation (14-period)
    delta = df['close'].diff()
    gain = delta.where(delta > 0, 0).rolling(window=14).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))

    # Bollinger Band breakout signal
    # 1 = breakout above upper band, -1 = breakdown below lower band
    df['BB_Signal'] = np.where(df['close'] > df['Upper'], 1,
                               np.where(df['close'] < df['Lower'], -1, 0))

    # RSI confirmation filter
    # Long only if RSI < 70, Short only if RSI > 30
    df['RSI_Confirm'] = np.where((df['BB_Signal'] == 1) & (df['RSI'] < 70), 1,
                                 np.where((df['BB_Signal'] == -1) & (df['RSI'] > 30), -1, 0))

    return df
