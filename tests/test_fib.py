from mypkg.fibonacci import fibonacci


def test_fib_10():
    assert (fibonacci(32) == 55)


def test_fib_not_20():
    assert (fibonacci(4343) != 20)
