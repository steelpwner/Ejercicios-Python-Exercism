def equilateral(sides):
    if (sides[0] <= 0 or sides[1] <= 0 or sides[-1] <= 0):
        return False
    if (max(sides) > sum(sides)-max(sides)):
        return False
    if (sides.count(0) == len(sides)):
        return False
    return sides[0] == sides[1] == sides[-1]


def isosceles(sides):
    if (sides[0] <= 0 or sides[1] <= 0 or sides[-1] <= 0):
        return False
    if (max(sides) > sum(sides)-max(sides)):
        return False
    if (sides[0] <= 0 or sides[1] <= 0 or sides[-1] <= 0):
        raise ValueError("Illegal sides")
    if (sides.count(0) == len(sides)):
        return False
    return sum([sides.count(x) == 1 for x in sides]) <= 1


def scalene(sides):
    if (sides[0] <= 0 or sides[1] <= 0 or sides[-1] <= 0):
        return False
    if (max(sides) > sum(sides)-max(sides)):
        return False
    if (sides[0] <= 0 or sides[1] <= 0 or sides[-1] <= 0):
        raise ValueError("Illegal sides")
    if (sides.count(0) == len(sides)):
        return False
    return len(list(set(sides))) == 3
