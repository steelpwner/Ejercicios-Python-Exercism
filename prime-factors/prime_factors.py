def factors(value):
    result = []
    comp = value
    i = 2
    while comp != 1:
    	if (comp % i == 0) :
    		result.append(i)
    		comp = comp / i
    		i = 1
    	i=i+1
    return result