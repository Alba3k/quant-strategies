import pandas_ta as ta

def parabolic_sar_strategy(df):
    """
    Parabolic SAR Trend Following Strategy

    This strategy uses the Parabolic SAR indicator to follow trends and manage stop-loss logic.

    Signal Logic:
    - Long: SAR is below the current price
    - Short: SAR is above the current price

    Parameters:
    - df (pd.DataFrame): OHLCV data with 'high', 'low', 'close'

    Returns:
    - pd.DataFrame: Original DataFrame with added columns:
        ['SAR', 'Position']
    """

    # Calculate Parabolic SAR
    df["SAR"] = ta.psar(df["high"], df["low"], df["close"])["PSARl_0.02_0.2"]

    # Generate position signals
    df["Position"] = np.where(df["SAR"] < df["close"], 1,
                              np.where(df["SAR"] > df["close"], -1, 0))

    return df
