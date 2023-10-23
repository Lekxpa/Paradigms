# Условие
# На вход подается число n.
# ● Задача
# Написать скрипт в любой парадигме, который выводит на экран 
# таблицу умножения всех чисел от 1 до n. 
# Обоснуйте выбор парадигм.
# ● Пример вывода:
# 1 * 1 = 1
# 1 * 2 = 2
# 1 * 3 = 3
# 1 * 4 = 4
# 1 * 5 = 5
# 1 * 6 = 6
# ..
# 1 * 9 = 9

START_NUM1 = 1
max_num1 = int(input("Введите значение n: "))
MAX_NUM2 = 10

def multiplication_table(START_NUM1, max_num1, MAX_NUM2):

    for i in range(START_NUM1, max_num1+1):
        for j in range(START_NUM1, MAX_NUM2):
            for k in range(i, i + 1):
                print(f'{k}  * {j:>2} = {j * k:>2}', end = ' '*3)
            print()
        print()


# n = int(input("Введите значение n: "))
multiplication_table(START_NUM1, max_num1, MAX_NUM2)