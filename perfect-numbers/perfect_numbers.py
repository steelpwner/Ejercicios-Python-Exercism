def classify(number):
    if (number < 1):
        raise ValueError("Number is less than 1")
    numbers = [x for x in range(1, int(number/2)+1)]
    suma = sum(filter(lambda x: number % x == 0, numbers))
    out = ""
    if suma == number:
        out = "perfect"
    elif suma > number:
        out = "abundant"
    else:
        out = "deficient"
    return out
