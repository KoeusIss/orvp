import pytest
import pandas as pd
import numpy as np

@pytest.fixture
def columns():
    return [
        'bid_price1', 'bid_price2', 'ask_price1', 'ask_price2',
        'bid_size1', 'bid_size2', 'ask_size1', 'ask_size2'
    ]


@pytest.fixture
def dataframe(columns):
    return pd.DataFrame(
        np.arange(80).reshape(10, 8),
        columns=columns
    )
