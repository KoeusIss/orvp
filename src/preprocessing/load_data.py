"""
Load data from the provider
"""
import pandas as pd

BASE_PATH = "data/"

BOOK_TYPES = {
    'time_id': 'int16',
    'seconds_in_bucket': 'int16',
    'bid_price1': 'float32',
    'ask_price1': 'float32',
    'bid_price2': 'float32',
    'ask_price2': 'float32',
    'bid_size1': 'int16',
    'ask_size1': 'float32',
    'bid_size2': 'int16',
    'ask_size2': 'int16',
}

TRADE_TYPES = {
    'time_id': 'int16',
    'seconds_in_bucket': 'int16',
    'price': 'float32',
    'size': 'int16',
    'stock_id': 'int8',
}


def get_df(stock_id, type="book", mode="train"):
    if type not in ["book", "trade"]:
        raise TypeError("WRONG: wrong type!")

    if mode not in ["train", "test"]:
        raise TypeError("WRONG: wrong mode!")

    types = f"{type.upper()}_TYPES"
    file_path = f"{BASE_PATH + type}_{mode}.parquet/stock_id={stock_id}"
    df = pd.read_parquet(file_path)

    return df.astype(dtype=eval(types))
