def abbreviate(words):
	punctuations = '''!()-[]{};:\,<>./?@#$%^&*_~'''
	for i in punctuations:
		words = words.replace(i," ")
	return ''.join([x.capitalize()[0] for x in words.split()])
