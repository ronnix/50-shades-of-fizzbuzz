# Initial version: TDD-style, pair programming with a zombie

import pytest


def fizzbuzz(n: int) -> str:
    if (n % 15) == 0:
        return "fizzbuzz"
    if (n % 3) == 0:
        return "fizz"
    if (n % 5) == 0:
        return "buzz"
    return str(n)


@pytest.mark.parametrize('n,out', [
    (1, "1"),
    (2, "2"),
    (3, "fizz"),
    (5, "buzz"),
    (6, "fizz"),
    (10, "buzz"),
    (15, "fizzbuzz"),
    (30, "fizzbuzz"),
])
def test_fizzbuzz(n, out):
    assert fizzbuzz(n) == out
