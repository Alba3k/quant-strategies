import pandas as pd
import numpy as np

def carry_trade_strategy(df, rate_diff_threshold=1.0):
    """
    Carry Trade Strategy

    Signal Logic:
    - Long if rate_diff > threshold
    - Short if rate_diff < -threshold

    Requires:
    - df['rate_diff']: difference in interest rates

    Returns:
    - df with ['rate_diff', 'Position']
    """
    df["Position"] = np.where(df["rate_diff"] > rate_diff_threshold, 1,
                              np.where(df["rate_diff"] < -rate_diff_threshold, -1, 0))
    return df
