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
    """Load datasets and either  for testing or training for both, book and
    Trade data.

    Arguments:
        stock_id {int} -- The stock_id referenece.

    Keyword Arguments:
        type {str} -- The type of data <book> or <trade> (default: {"book"})
        mode {str} -- The load mode <train> or <test> (default: {"train"})

    Raises:
        ValueError: If the type isn't <book> or <trade>
        ValueError: If the mode isn't <train> or <test>

    Returns:
        pd.DataFrame -- pandas DataFrame.
    """
    if type not in ["book", "trade"]:
        raise ValueError("WRONG: wrong type!")

    if mode not in ["train", "test"]:
        raise ValueError("WRONG: wrong mode!")

    types = f"{type.upper()}_TYPES"
    file_path = f"{BASE_PATH + type}_{mode}.parquet/stock_id={stock_id}"
    df = pd.read_parquet(file_path)

    return df.astype(dtype=eval(types))
