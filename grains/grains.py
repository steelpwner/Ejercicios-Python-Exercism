def square(number):
    if (number > 64 or number < 1):
        raise ValueError("Number not in range")
    return 2 ** (number - 1)


def total():
    return sum([2 ** (x-1) for x in range(1, 65)])
