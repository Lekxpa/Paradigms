# Задача №1
# Дан список целых чисел numbers. Необходимо написать 
# в императивном стиле процедуру для сортировки числа в списке 
# в порядке убывания. Можно использовать любой алгоритм сортировки.

def sort_descending_imperative_style(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] < numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

if __name__ == '__main__':
    lst = [1, 3, 5, 7, 4, 2, 6]
    print(sort_descending_imperative_style(lst))