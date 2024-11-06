def intersection(a, b):
    set_b = set(b)
    return [item for item in a if item in set_b]


print(intersection([4,2,1,6], [3,6,9,2,10])) # -> [2,6]
