def mse(lst1:list[int], lst2: list[int]):
    if not len(lst1) or len(lst2) != len(lst1):
        raise ValueError('slkjfklsjf')
    return sum(map(lambda x, y: (x - y) ** 2, lst1, lst2)) / len(lst1)


lst1 = [1, 2, 3, 4, 5]
lst2 = [1, 3, 4, 5, 6]

print(mse(lst1, lst2))