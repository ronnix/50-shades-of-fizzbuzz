# Refactor to use a list comprehension

from functools import reduce

from hypothesis import given
from hypothesis.strategies import integers


SPECIAL_NUMBERS = {
    3: 'fizz',
    5: 'buzz',
    7: 'baz',
}


def say(n: int) -> str:
    found = [
        SPECIAL_NUMBERS[s]
        for s in SPECIAL_NUMBERS
        if (n % s) == 0
    ]
    return ''.join(found) if found else str(n)


def multiples_of(*n, but_not=()):
    """
    Hypothesis generation strategy

    Generate positive integers that are multiples of some integers,
    but not of others.
    """

    def product(*numbers):
        return reduce(lambda x, y: x * y, numbers, 1)

    def is_not_multiple_of(n, *args):
        return all((n % d) != 0 for d in args)

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
