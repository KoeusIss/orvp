"""Feature Engineering"""
import numpy as np
import pandas as pd
import src.utils as UT


def set_book_features(df, window_size=100):
    """Sets statistic features to the book DataFrame

    Arguments:
        df {pd.DataFrame} -- The given DataFrame

    Keyword Arguments:
        window_size {int} -- The window size per seconds (default: {100})

    Returns:
        pd.DataFrame -- Return the newly generated DataFrame
    """
    # First level aggregation
    df["wap_1"] = UT.wap(df, 1)
    df["wap_2"] = UT.wap(df, 2)
    df["log_return_1"] = df.groupby("time_id")["wap_1"].apply(UT.log_return)
    df["log_return_2"] = df.groupby("time_id")["wap_2"].apply(UT.log_return)
    df["bid_size_spread"] = UT.spread_size(df, "bid")
    df["bid_price_spread"] = UT.spread_price(df, "bid")
    df["ask_size_spread"] = UT.spread_size(df, "ask")
    df["ask_price_spread"] = UT.spread_price(df, "ask")
    df["price_spread_1"] = UT.price_spread(df, 1)
    df["price_spread_2"] = UT.price_spread(df, 2)
    df['wap_balance'] = np.abs(df['wap_1'] - df['wap_2'])
    df["bid_ask_price_spread"] = np.abs(
        df["ask_price_spread"] - df["bid_price_spread"])
    df["bid_ask_size_spread"] = np.abs(
        df["ask_size_spread"] - df["bid_size_spread"])
    df["total_volume"] = UT.total_volume(df)
    df["imbalance_volume"] = UT.imbalance_volume(df)

    # Second level aggregation
    aggregation_dict = {
        "log_return_1": [UT.realized_volatility, np.mean],
        "log_return_2": [UT.realized_volatility, np.mean],
        "wap_1": [np.mean, np.std],
        "wap_2": [np.mean, np.std],
        "bid_price1": [np.mean, np.max],
        "bid_price2": [np.mean, np.max],
        "ask_price1": [np.mean, np.min],
        "ask_price2": [np.mean, np.min],
        "bid_size1": [np.mean, np.sum],
        "bid_size2": [np.mean, np.sum],
        "ask_size1": [np.mean, np.sum],
        "ask_size2": [np.mean, np.sum],
        "bid_size_spread": [np.mean, np.std],
        "bid_price_spread": [np.mean, np.std],
        "ask_size_spread": [np.mean, np.std],
        "ask_price_spread": [np.mean, np.std],
        "price_spread_1": [np.mean, np.std],
        "price_spread_2": [np.mean, np.std],
        "wap_balance": [np.mean, np.std],
        "bid_ask_price_spread": [np.mean, np.std],
        "bid_ask_size_spread": [np.mean, np.std],
        "total_volume": [np.mean, np.std],
        "imbalance_volume": [np.mean, np.std]
    }
    features_lst = []
    for second in range(0, 600, window_size):
        df_feature = df[df['seconds_in_bucket'] >= second]\
            .groupby("time_id")\
            .agg(aggregation_dict)
        df_feature.columns = [
            '_'.join(col) + f"_s{600 - second}" for col in df_feature.columns
        ]
        features_lst.append(df_feature)
    return pd.concat(features_lst, axis=1)


def set_trade_features(df, window_size=100):
    """Sets trade features

    Arguments:
        df {pd.DataFrame} -- The given trade DataFrame

    Keyword Arguments:
        window_size {int} -- The window size on seconds (default: {100})

    Returns:
        pd.DataFrame -- The Newly genereated DataFrame
    """
    # First level aggregation
    df["log_return"] = df.groupby("time_id")["price"].apply(UT.log_return)
    df['amount'] = df['price'] * df['size']

    # Second level aggregation
    aggregation_dict = {
        "log_return": [UT.realized_volatility, np.mean],
        "size": [np.mean, np.sum],
        "amount": [np.mean, np.sum],
        "order_count": [np.mean, np.sum],
    }
    features_lst = []
    for second in range(0, 600, window_size):
        df_feature = df[df['seconds_in_bucket'] >= second]\
            .groupby("time_id")\
            .agg(aggregation_dict)
        df_feature.columns = [
            '_'.join(col) + f"_s{600 - second}" for col in df_feature.columns
        ]
        features_lst.append(df_feature)
    return pd.concat(features_lst, axis=1)
