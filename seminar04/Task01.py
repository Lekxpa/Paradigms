# Контекст
# Есть такая операция в статистике - “нормализация”. Это операция принимающая на вход вектор и 
# возвращающая другой вектор. Смысл этой операции в том, чтобы данные из разных шкал загнать в 
# единый диапазон, как правило - от 0 до 1, тогда с данными становится проще работать.
# ● Ваша задача
# Реализовать с использованием функциональной парадигмы процедуру normalization, которая выполняет 
# нормализацию полученного массива по приведенной формуле нормализованного значения элемента, где
# ○ x_norm - нормализованное значение элемента
# ○ x - исходное значение элемента
# ○ x_max, x_min - максимальное и минимальное значение в массиве

# X norm = (x - x min) / (x max - x min)


def normalization(my_array: list) -> list:
    num_max = max(my_array)
    num_min = min(my_array)
    if num_max == num_min:
        raise ValueError('Zero division error')

    def normalize_number(num):
        return (num - num_min) / (num_max - num_min)

    return list(map(normalize_number, my_array))


array = [1, 5, 3, 7, 2]
normalized_arr = normalization(array)
print(f'Normalized array: {normalized_arr}')



# Контекст
# Предположим, что есть какой-то массив содержащий данные о разных людях и их возрасте и вас 
# попросили ответить на следующий вопрос: “сколько в массиве людей возраста > 30?”. Для этого, вы 
# хотите написать программу для фильтрации наблюдений по возрастному признаку.
# ● Ваша задача
# Написать скрипт принимающий на вход массив с данными о людях и число - возраст, а возвращающий 
# число - количество людей старше указанного возраста.


def get_people_over_flag_age(people_list: list, age: int) -> int:
    return sum(1 for man in people_list if man[1] > age)


people = [('Alex', 31), ('Bob', 30), ('Den', 29), ('Evan', 20), ('Frank', 40)]
flag_age = 30
selection = get_people_over_flag_age(people, flag_age)
print(f'Found {selection} people over {flag_age}')



def filter_data(lst, value):
    return sum(map(lambda x: x[1] >= value, lst))
    # return len(list(filter(lambda x: x[1] >= 30, lst))) 


init_list = ([('Max', 41), ('Andrey', 25), ('Victor', 42), ('Ivan', 35)])
print(filter_data(init_list, 30))



# Контекст
# Важнейшая задача в анализе данных - поиск дубликатов. Дубликат - это наблюдение, встречающееся в 
# данных больше одного раза. Такие наблюдения не просто не улучшают результат анализа или 
# полученных моделей, но и замедляют весь процесс в целом, поэтому аналитики и разработчики 
# предпочитают избавляться от них перед тем как приступить к анализу.
# ● Ваша задача
# Реализовать с использованием функциональной парадигмы процедуру для поиска дубликатов. На вход 
# подается массив, где могут присутствовать дубликаты (а могут и не присутствовать). При применении к 
# массиву, дубликаты должны быть выведены на экран в виде списка.

my_list = [1, 2, 3, 2, 4, 1, 5, 2]

first = set()
result = set()

for item in my_list:
    if item in first:
        result.add(item)
    else:
        first.add(item)

print("Дубликаты: ", result)

my_list = [1, 2, 3, 2, 4, 1, 5, 2]
duplicates = []

for item in my_list:
    if my_list.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print("Дубликаты:", duplicates)


def get_duplicates(my_array: list) -> list:
    return list(set([x for x in my_array if my_array.count(x) > 1]))


array = [1, 2, 3, 4, 5, 6, 1, 2, 3]
duplicates_array = get_duplicates(array)
print(f'Duplicates found: {duplicates_array}')