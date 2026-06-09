
from app.service import calculate_sum, calculate_difference, calculate_product





def test_calculate_sum():

    assert calculate_sum(2, 3) == "sum: 5"





def test_calculate_difference():

    assert calculate_difference(7, 4) == "difference: 3"





def test_calculate_product():

    assert calculate_product(4, 5) == "product: 20"

