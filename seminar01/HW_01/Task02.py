# 💡 Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

def sort_descending_declarative_style(numbers):
    numbers.sort(reverse=True)
    return numbers


if __name__ == '__main__':
    lst = [1, 3, 5, 7, 4, 2, 6]
    print(sort_descending_declarative_style(lst))