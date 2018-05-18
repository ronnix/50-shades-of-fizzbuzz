# Refactor tests to better express the different categories


def say(n: int) -> str:
    if (n % 15) == 0:
        return "fizzbuzz"
    if (n % 3) == 0:
        return "fizz"
    if (n % 5) == 0:
        return "buzz"
    return str(n)


def test_say_the_number():
    assert say(1) == "1"


def test_say_fizz_if_multiple_of_3():
    assert say(3) == "fizz"


def test_say_buzz_if_multiple_of_5():
    assert say(5) == "buzz"


def test_say_fizzbuzz_if_multiple_of_15():
    assert say(15) == "fizzbuzz"
