"""
Financial utilities
-- Financial functions to compute different values and relations between
    features
"""
import numpy as np


def wap(df, index):
    """
    Compute the Waighted Avergae Price
    """
    bid_price = df[f"bid_price{index}"]
    bid_size = df[f"bid_size{index}"]
    ask_price = df[f"ask_price{index}"]
    ask_size = df[f"ask_size{index}"]
    return bid_price * ask_size + ask_price * bid_size / (bid_size + ask_size)


def log_return(series):
    """
    Compute the log_return of WAP
    """
    return np.log(series).diff()


def realized_volatility(series):
    """
    Compute the realized volatility
    """
    return np.sqrt(np.sum(series**2))


def total_volume(df):
    """
    Compute the total volume between asks and bids
    """
    ask_size_1 = df["ask_size1"]
    ask_size_2 = df["ask_size2"]
    bid_size_1 = df["bid_size1"]
    bid_size_2 = df["bid_size2"]
    return ask_size_1 + ask_size_2 + bid_size_1 + bid_size_2


def imbalance_volume(df):
    """
    Computes the imbalance volume
    """
    ask_size_1 = df["ask_size1"]
    ask_size_2 = df["ask_size2"]
    bid_size_1 = df["bid_size1"]
    bid_size_2 = df["bid_size2"]
    return np.abs(ask_size_1 + ask_size_2 - bid_size_1 - bid_size_2)


def spread(df, type):
    """
    Compute the spread
    """
    size_1 = df[f"{type}_size1"]
    size_2 = df[f"{type}_size2"]
    return size_1 - size_2
