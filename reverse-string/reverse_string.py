def reverse(text):
    return ''.join([text[-x] for x in range(1, len(text)+1)])
