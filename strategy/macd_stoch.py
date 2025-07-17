import pandas as pd
import numpy as np

def macd_stoch_strategy(df):
    """
    MACD + Stochastic Strategy

    This strategy combines MACD crossover with Stochastic oscillator signals
    to identify potential trend reversals with momentum confirmation.

    Signal Logic:
    - Buy (LONG): MACD > Signal AND %K crosses above %D in oversold zone (<20)
    - Sell (SHORT): MACD < Signal AND %K crosses below %D in overbought zone (>80)

    Parameters:
    - df (pd.DataFrame): OHLCV data with 'close', 'high', 'low' columns

    Returns:
    - pd.DataFrame: Original DataFrame with added columns:
        ['MACD', 'Signal', '%K', '%D', 'MACD_Signal', 'Stoch_Signal', 'Position']
    """

    # MACD Calculation (standard: 12, 26, 9)
    df['MACD'] = df['close'].ewm(span=12).mean() - df['close'].ewm(span=26).mean()
    df['Signal'] = df['MACD'].ewm(span=9).mean()

    # Stochastic Oscillator (%K and %D)
    high_14 = df['high'].rolling(window=14).max()
    low_14 = df['low'].rolling(window=14).min()
    df['%K'] = (df['close'] - low_14) / (high_14 - low_14) * 100
    df['%D'] = df['%K'].rolling(window=3).mean()

    # MACD Signal: 1 if MACD > Signal line, else -1
    df['MACD_Signal'] = np.where(df['MACD'] > df['Signal'], 1, -1)

    # Stochastic Signal:
    # Buy if %K > %D and %K < 20 (oversold)
    # Sell if %K < %D and %K > 80 (overbought)
    df['Stoch_Signal'] = np.where(
        (df['%K'] > df['%D']) & (df['%K'] < 20), 1,
        np.where((df['%K'] < df['%D']) & (df['%K'] > 80), -1, 0)
    )

    # Final Position: only when both signals align
    df['Position'] = df['MACD_Signal'] & df['Stoch_Signal']

    return df
