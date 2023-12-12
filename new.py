from math import sqrt
from typing import Optional


def add_numbers(num1: int, num2: int) -> int:
    return num1 + num2


def calculate_square_root(number: float) -> float:
    return sqrt(number)


def calc(your_number: float) -> Optional[str]:
    if your_number >= 0:
        result = calculate_square_root(your_number)
        return (
            f'Мы вычислили квадратный корень из введённого '
            f'вами числа. Это будет: {result}'
        )
    else:
        return 'Корень из отрицательного числа не извлекается'


num1: int = 10
num2: int = 5

print('Сумма чисел: ', add_numbers(num1, num2))

print(calc(25.5))
