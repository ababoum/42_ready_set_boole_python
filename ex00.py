def adder(a: int, b: int) -> int:
    if type(a) != int or type(b) != int:
        return None
    if a < 0 or b < 0:
        return None
    while b != 0:
        a_p = a ^ b
        b_p = (a & b) << 1
        a = a_p
        b = b_p
    return a


if __name__ == "__main__":
    print(adder(1, 2))
    print(adder(0, 2147483647))
    print(adder(2147483647, 2147483647))
    print(adder(5, 3))
