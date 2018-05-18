# Refactor tests to use property-based testing hypothesis

from hypothesis import assume, given
from hypothesis.strategies import integers


def say(n: int) -> str:
    if (n % 15) == 0:
        return "fizzbuzz"
    if (n % 3) == 0:
        return "fizz"
    if (n % 5) == 0:
        return "buzz"
    return str(n)


positive_integers = integers(min_value=1)


@given(positive_integers)
def test_say_the_number(n):
    assume(n % 3 != 0)
    assume(n % 5 != 0)
    assert say(n) == str(n)


@given(positive_integers.map(lambda n: n * 3))
def test_say_fizz_if_multiple_of_3(n):
    assume(n % 5 != 0)
    assert say(n) == "fizz"


@given(positive_integers.map(lambda n: n * 5))
def test_say_buzz_if_multiple_of_5(n):
    assume(n % 3 != 0)
    assert say(n) == "buzz"


@given(positive_integers.map(lambda n: n * 15))
def test_say_fizzbuzz_if_multiple_of_15(n):
    assert say(n) == "fizzbuzz"
