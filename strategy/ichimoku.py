def ichimoku_strategy(df):
    """
    Ichimoku Cloud Strategy

    Signal Logic:
    - Long: Price above cloud and Tenkan > Kijun

    Returns:
    - df with ['Tenkan', 'Kijun', 'SpanA', 'SpanB', 'Position']
    """
    ichimoku = ta.ichimoku(df["high"], df["low"], df["close"])
    df["Tenkan"] = ichimoku["ITS_9"]
    df["Kijun"] = ichimoku["IKS_26"]
    df["SpanA"] = ichimoku["ISA_9"]
    df["SpanB"] = ichimoku["ISB_52"]

    df["Position"] = np.where((df["close"] > df["SpanA"]) & (df["Tenkan"] > df["Kijun"]), 1, 0)
    return df
