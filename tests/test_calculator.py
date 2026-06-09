
import pytest

from app.calculator import add, divide, multiply, subtract





def test_add():

    assert add(2, 3) == 5





def test_subtract():

    assert subtract(7, 4) == 3





def test_multiply():

    assert multiply(4, 5) == 20



def test_divide():

    assert divide(10, 2) == 5.0

    assert divide(7, 3) == 7 / 3



def test_divide_by_zero():

    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):

        divide(5, 0)

