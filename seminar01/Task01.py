# Контекст
# Предположим, что нам хочется для любого массива чисел array и любого числа target узнать содержится 
# ли target в array. Такую процедуру будем называть поиском.
# Задача
# Реализовать императивную функцию поиска элементов на языке Pytho

def search(array, target):
    for num in array:
        if num == target:
            return True
    return False


init_list = [1, 2, 3, 4, 5]
target = 11
print(search(init_list, target))


# декларативный

# my_arr = [1, 2, 3, 4]
def seardhElement(my_arr, targ):
    return any(i == targ for i in my_arr)
    # return target in my_arr

print(seardhElement([1, 2, 3, 4], 3))
# print(seardhElement(my_arr, 5))

