def convert(number):
	if not int(number): raise ValueError("The argument was not a number")
	values = {3:"Pling",5:"Plang",7:"Plong"}
	result = []
	number = int(number)
	for n in values:
		if number % n == 0 : result.append(values[n])
	return str(number) if not result else "".join(x for x in result)