def handle(string):
	special = ["-","_"," "]
	for i in special:
		string = string.replace(i,"")
	return string

def is_isogram(string):
	return sum([sum([z.lower() == y for z in string]) > 1 for y in set(list(handle(string)))]) == 0
