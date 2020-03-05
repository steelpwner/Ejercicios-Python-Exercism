def commands(number):
    binary = bin(number)[2::]
    arr = []
    if (binary[-1] == "1"):
        arr.append("wink")
    if (len(binary) >= 2 and binary[-2] == "1"):
        arr.append("double blink")
    if (len(binary) >= 3 and binary[-3] == "1"):
        arr.append("close your eyes")
    if (len(binary) >= 4 and binary[-4] == "1"):
        arr.append("jump")
    if (len(binary) >= 5 and binary[-5] == "1"):
        arr.reverse()
    return arr
