def is_pangram(sentence):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return sum([0 if sentence.upper().count(x) > 0 else 1 for x in letters]) == 0
