def handle(string):
    special = ["-", "_", " "]
    for i in special:
        string = string.replace(i, "")
    return string


def is_isogram(string):
    string = handle(string).lower()
    return sum([string.count(y) > 1 for y in set(list(string))]) == 0
