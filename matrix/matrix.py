class Matrix:
    def __init__(self, matrix_string):
       	cad = matrix_string.split("\n")
       	self.matrix = [[int(x) for x in y.split()] for y in cad]

    def row(self, index):
    	index = index - 1
    	if (index < 0 or index > len(self.matrix)):
    		raise ValueError("Index out of Bounds")
    	return self.matrix[index]

    def column(self, index):
    	index = index - 1
    	if (index < 0 or index > len(self.matrix)):
    		raise ValueError("Index out of Bounds")
    	return [x[index] for x in self.matrix]

obj = Matrix("1 2 3\n4 5 6\n7 8 9")
print(obj.column(1))