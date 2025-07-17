def bb_mean_reversion_strategy(df):
    """
    Bollinger Bands Mean Reversion Strategy

    Signal Logic:
    - Long: Price touches lower band
    - Short: Price touches upper band

    Returns:
    - df with ['BBL', 'BBU', 'Position']
    """
    bb = ta.bbands(df["close"], length=20, std=2)
    df["BBL"] = bb["BBL_20_2.0"]
    df["BBU"] = bb["BBU_20_2.0"]

    df["Position"] = np.where(df["close"] <= df["BBL"], 1,
                              np.where(df["close"] >= df["BBU"], -1, 0))
    return df
