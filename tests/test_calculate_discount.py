import pytest
from pages.discount_caculator import calculate_discount


# @pytest.fixture
# def base_price():
#     return 100


@pytest.mark.parametrize("discount_percent, expected", [
    (30, 70),
    (25, 75),
    (10, 90)
])
def test_calculate(base_price, discount_percent, expected):
    assert calculate_discount(base_price, discount_percent) == expected
