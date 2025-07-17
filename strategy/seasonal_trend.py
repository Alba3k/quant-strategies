import pandas as pd
import numpy as np

def seasonal_trend_strategy(df, month_signal_map):
    """
    Seasonal Trend Strategy

    Signal Logic:
    - Long/Short based on predefined seasonal map

    Parameters:
    - month_signal_map: dict {month: signal}, e.g. {1: 1, 7: -1}

    Returns:
    - df with ['Month', 'Position']
    """
    df["Month"] = df.index.month
    df["Position"] = df["Month"].map(month_signal_map).fillna(0)
    return df
