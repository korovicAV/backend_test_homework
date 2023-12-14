from math import sqrt
from typing import Optional


def add_numbers(xa: int, ya: int) -> int:
    return xa + ya


def calculate_square_root(number: float) -> float:
    return sqrt(number)


def calc(your_number: float) -> Optional[str]:
    if not your_number < 0:
        root = calculate_square_root(your_number)
        return (
            f'Мы вычислили квадратный корень из введённого вами '
            f'числа. Это будет: {root}'
        )
    return None


xa: int = 10
ya: int = 5

print('Сумма чисел: ', add_numbers(xa, ya))
print(calc(25.5))
