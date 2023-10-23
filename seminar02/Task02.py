# Условие
# На вход подается число в десятичной системе счисления
# ● Задача
# Написать скрипт в любой парадигме, который возвращает 
# полученное число переведенное в двоичную 
# систему счисления. Обоснуйте сделанный выбор парадигм.


# from string import ascii_uppercase as au 
# from string import ascii_uppercase, digits

# print(au)
# print(ascii_uppercase, digits)


from string import ascii_uppercase, digits

DIGITS = digits + ascii_uppercase


def bin_octa(num, prod):
    result = []
    while num > 0:
        temp = num % prod
        # if temp > 9:
        #     result.append(ascii_uppercase[temp - 10])
        # else:
        #     result.append(str(temp))
        # num //= prod
    # return "".join(result[::-1])
        result.append(DIGITS[temp])
        num //= prod
    return "".join(result[::-1])


number = int(input("Введите число: "))
res = bin_octa(number, 16)
print(res)