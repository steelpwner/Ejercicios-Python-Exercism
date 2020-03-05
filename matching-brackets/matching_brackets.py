def is_paired(input_string):
    ver = [x for x in input_string]
    ver2 = []
    opened = ["{","[","("]
    closed = ["}","]",")"]
    for i in ver:
    	if i in opened:
    		ver2.append(i)
    	if i in closed:
    		if ((len(ver2) > 0 and ver2[-1]) == opened[closed.index(i)]):
    			ver2.pop()
    		else:
    			return False
    return len(ver2) == 0
print(is_paired("([{}({}[])])"))

