
from app.calculator import add, subtract, multiply

from app.formatter import format_result





def calculate_sum(a: int, b: int) -> str:

    return format_result("sum", add(a, b))





def calculate_difference(a: int, b: int) -> str:

    return format_result("difference", subtract(a, b))





def calculate_product(a: int, b: int) -> str:

    return format_result("product", multiply(a, b))

