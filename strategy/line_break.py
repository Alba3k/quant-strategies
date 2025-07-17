def line_break_strategy(df):
    """
    Line Break Breakout Strategy

    Signal Logic:
    - Long on breakout above recent highs
    - Short on breakdown below recent lows

    Returns:
    - df with ['High_3', 'Low_3', 'Position']
    """
    df["High_3"] = df["high"].rolling(window=3).max()
    df["Low_3"] = df["low"].rolling(window=3).min()

    df["Position"] = np.where(df["close"] > df["High_3"].shift(1), 1,
                              np.where(df["close"] < df["Low_3"].shift(1), -1, 0))
    return df
