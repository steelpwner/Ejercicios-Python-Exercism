def sum_of_multiples(limit, multiples):
    if (0 in multiples and len(multiples) == 1):
        return 0
    elif (0 in multiples):
        multiples.remove(0)

    def filtro(n):
        for i in multiples:
            if (n % i == 0):
                return True
        return False
    return sum(filter(filtro, [x for x in range(limit)]))
