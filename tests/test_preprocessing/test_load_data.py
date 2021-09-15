import pytest
from src.preprocessing.load_data import get_df


def test_should_succeed_loading_test_data():
    df = get_df(0, mode="test")
    assert df.shape == (3, 10)


@pytest.mark.parametrize("type, mode", [
    ('book', 'validation'),
    ('trade', 'validation'),
    ('price', 'test'),
    ('price', 'train')
])
@pytest.mark.xfail(raises=ValueError)
def test_should_fail_passing_wrong_type_or_mode(type, mode):
    df = get_df(0, type=type, mode=mode)
    assert df.shape == (3, 10)
