def classify(number):
	if (number < 1):
		raise ValueError("Number is less than 1")
	suma = sum(filter(lambda x: number % x == 0, [x for x in range(1,int(number/2)+1)]))
	return  "perfect" if suma == number else "abundant" if suma > number else "deficient"