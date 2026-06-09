
import pytest

from app.service import calculate_difference, calculate_product, calculate_quotient, calculate_sum





def test_calculate_sum():

    assert calculate_sum(2, 3) == "sum: 5"





def test_calculate_difference():

    assert calculate_difference(7, 4) == "difference: 3"





def test_calculate_product():

    assert calculate_product(4, 5) == "product: 20"



def test_calculate_quotient():

    assert calculate_quotient(10, 2) == "quotient: 5.0"



def test_calculate_quotient_by_zero():

    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):

        calculate_quotient(5, 0)



def test_calculate_quotient_negative():

    assert calculate_quotient(-10, 2) == "quotient: -5.0"

    assert calculate_quotient(10, -2) == "quotient: -5.0"

    assert calculate_quotient(-10, -2) == "quotient: 5.0"

