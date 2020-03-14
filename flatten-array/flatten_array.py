def flatten(iterable):
    def flat(it):
        a = []
        for i in it:
            if isinstance(i, list):
                for x in flat(i):
                    a.append(x)
            else:
                a.append(i)
        return list(filter(lambda x: x is not None, a))
    return flat(iterable)
