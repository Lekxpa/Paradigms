#  Доля чисел: императивный вариант

# Условие
# На вход подается: список целых чисел arr
# ● Задача
# Реализовать императивную функцию, которая возвращает три числа:
# ○ Долю позитивных чисел
# ○ Долю нулей
# ○ Долю отрицательных чисел

def ratios_array(arr: list[int]):
    lst_len = len(arr)
    if not lst_len: # массив пустой
        raise ValueError('empty list')
    pos, neg, zero = 0, 0, 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1

    pos_ratio = pos / lst_len
    neg_ratio = neg / lst_len
    zero_ratio = 1 - (pos_ratio + neg_ratio)

    return pos_ratio, neg_ratio, zero_ratio

if __name__ == "__main__":
    init_list = [1, 2, -3, -4, 0]
    print(ratios_array(init_list))


# декларативный вариант 

def ratios_array(lst):
    pos = len(list(filter(lambda x: x > 0, lst)))
    neg = len(list(filter(lambda x: x < 0, lst)))
    zero = len(list(filter(lambda x: x == 0, lst)))

    lst_len = len(lst)
    pos_ratio = pos / lst_len
    neg_ratio = neg / lst_len
    zero_ratio = zero / lst_len

    return pos_ratio, neg_ratio, zero_ratio


init_list = [1, 2, -3, -4, 0]
print(ratios_array(init_list))

def ratios_array1(arr):
    total = len(arr)
    if total == 0:
        raise ValueError('Array is empty')
    
    positive = sum(num > 0 for num in arr)
    zero = sum(num == 0 for num in arr)
    negative = sum(num < 0 for num in arr)

    return positive/total, zero/total, negative/total