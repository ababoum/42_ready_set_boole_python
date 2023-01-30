from ex00 import adder


def multiplier(a: int, b: int) -> int:
    if (type(a) != int or type(b) != int):
        return None
    if (a < 0 or b < 0):
        return None

    res = 0
    mult = b
    index = 0

    while mult != 0:
        if mult & 1 == 1:
            res = adder(res, a << index)
        mult >>= 1
        index += 1
    return res


if __name__ == "__main__":
    print(multiplier(1, 2))
    print(multiplier(0, 2147483647))
    print(multiplier(100, 100))
    print(multiplier(5, 3))
    
    assert multiplier(1, 2) == 2
    assert multiplier(0, 2147483647) == 0
    assert multiplier(100, 100) == 10000
    assert multiplier(5, 3) == 15
