"""Testing financial utilities functions"""
import pytest
from src.utils import wap

@pytest.mark.parametrize("index", [1, 2])
def test_should_succeed_return_wap_values(dataframe, index):
    gotten = wap(dataframe, index)
    assert gotten.shape == (10,)
