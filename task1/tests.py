import pytest
from solution import strict


@strict
def func1(a: int, b: int, c: str, d: str, e: bool):
    return a, b, c, d, e


@strict
def func2():
    return


@strict
def func3(a: float, b: int):
    return int(a) + b


@strict
def func4(a: str):
    return 2 * a


@strict
def func5(a: bool, b: bool, c: int):
    return a or b ^ c


func1(1, 2, "", "a", True)
func2()
func3(1., 2)
func4("a")
func5(True, False, 0)
try:
    func5(1, False, 0)
    raise AssertionError("failed test")
except TypeError:
    print("test OK")

try:
    func4(1)
    raise AssertionError("failed test")
except TypeError:
    print("test OK")

func5(True, False, 1)

try:
    func2(2)
    raise AssertionError("failed test")
except TypeError:
    print("test OK")

try:
    func5(True, 1, 0)
    raise AssertionError("failed test")
except TypeError:
    print("test OK")

try:
    func5(True, False, 0.)
except TypeError:
    print("test OK")
