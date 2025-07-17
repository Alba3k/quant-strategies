import pandas as pd
import numpy as np

def rsi_divergence_strategy(df, rsi_period=14):
    """
    RSI Divergence Strategy (simplified)

    Signal Logic:
    - Long: Price makes lower low, RSI makes higher low
    - Short: Price makes higher high, RSI makes lower high

    Returns:
    - df with ['RSI', 'Position']
    """
    df["RSI"] = ta.rsi(df["close"], length=rsi_period)

    df["Price_LL"] = df["close"] < df["close"].shift(1)
    df["RSI_HL"] = df["RSI"] > df["RSI"].shift(1)
    df["Bull_Div"] = df["Price_LL"] & df["RSI_HL"]

    df["Price_HH"] = df["close"] > df["close"].shift(1)
    df["RSI_LH"] = df["RSI"] < df["RSI"].shift(1)
    df["Bear_Div"] = df["Price_HH"] & df["RSI_LH"]

    df["Position"] = np.where(df["Bull_Div"], 1, np.where(df["Bear_Div"], -1, 0))
    return df
