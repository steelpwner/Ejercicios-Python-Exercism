def is_pangram(sentence):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return sum([sentence.upper().count(x) == 0 for x in letters]) == 0
