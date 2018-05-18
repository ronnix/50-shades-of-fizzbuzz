# Add baz for multiples of 7

from functools import reduce

from hypothesis import given
from hypothesis.strategies import integers


def is_multiple_of(n, *args):
    return all((n % d) == 0 for d in args)


def is_not_multiple_of(n, *args):
    return all((n % d) != 0 for d in args)


def say(n: int) -> str:
    if is_multiple_of(n, 3, 5, 7):
        return "fizzbuzzbaz"
    if is_multiple_of(n, 5, 7):
        return "buzzbaz"
    if is_multiple_of(n, 3, 7):
        return "fizzbaz"
    if is_multiple_of(n, 3, 5):
        return "fizzbuzz"
    if is_multiple_of(n, 3):
        return "fizz"
    if is_multiple_of(n, 5):
        return "buzz"
    if is_multiple_of(n, 7):
        return "baz"
    return str(n)


def multiples_of(*n, but_not=()):
    """
    Hypothesis generation strategy

    Generate positive integers that are multiples of some integers,
    but not of others.
    """

    def product(*numbers):
        return reduce(lambda x, y: x * y, numbers, 1)

    return (
        integers(min_value=1)
        .map(lambda x: x * product(*n))
        .filter(lambda n: is_not_multiple_of(n, *but_not))
    )


@given(multiples_of(1, but_not=(3, 5, 7)))
def test_say_the_number(n):
    assert say(n) == str(n)


@given(multiples_of(3, but_not=(5, 7)))
def test_say_fizz_if_multiple_of_3(n):
    assert say(n) == "fizz"


@given(multiples_of(5, but_not=(3, 7)))
def test_say_buzz_if_multiple_of_5(n):
    assert say(n) == "buzz"


@given(multiples_of(7, but_not=(3, 5)))
def test_say_baz_if_multiple_of_7(n):
    assert say(n) == "baz"


@given(multiples_of(3, 5, but_not=(7,)))
def test_say_fizzbuzz_if_multiple_of_3_and_5(n):
    assert say(n) == "fizzbuzz"


@given(multiples_of(3, 7, but_not=(5,)))
def test_say_fizzbaz_if_multiple_of_3_and_7(n):
    assert say(n) == "fizzbaz"


@given(multiples_of(5, 7, but_not=(3,)))
def test_say_fizzbaz_if_multiple_of_5_and_7(n):
    assert say(n) == "buzzbaz"


@given(multiples_of(3, 5, 7))
def test_say_fizzbuzz_if_multiple_of_3_and_5_and_7(n):
    assert say(n) == "fizzbuzzbaz"


def test_is_multiple_of():
    assert is_multiple_of(3, 3)
    assert is_multiple_of(5, 5)
    assert is_multiple_of(15, 3, 5)
    assert not is_multiple_of(5, 3)


def test_is_not_multiple_of():
    assert is_not_multiple_of(13, 3, 5, 7)
