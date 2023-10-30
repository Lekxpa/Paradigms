# Задача
# Написать игру в “Крестики-нолики”. Можете использовать 
# любые парадигмы, которые посчитаете наиболее 
# подходящими. Можете реализовать доску как угодно - как 
# одномерный массив или двумерный массив (массив массивов). 
# Можете использовать как правила, так и хардкод, на своё 
# усмотрение. Главное, чтобы в игру можно было поиграть через 
# терминал с вашего компьютера.


# игра за обоих игроков


print('\n\033[1m\033[4m\033[37m\033[45m\033[3mКрестики-нолики\033[0m\n\
    \n\033[3mНеобходимо указать номер ячейки,\
    \n\033[3mв которую хотите поставить крестик/нолик\033[0m\n')

borders = list(range(1, 10))

def print_map(borders):
    print('-  ' * 5)
    for i in range(3):
        print('|', borders[i * 3], '|', borders[i * 3 + 1], '|', borders[i * 3 + 2], '|')
        print('-  ' * 5)

def input_XO(sign):
    gamech = False
    while not gamech:
        step = input(f'\n\033[3mУкажите номер ячейки, в которую хотите поставить {sign}? \033[0m')
        try:
            step = int(step)
        except:
            print('\nНеверно указано значение. Укажите номер ячейки (от 1 до 9)!\n')
            continue
        if step >= 1 and step <= 9:
            if (str(borders[step-1]) not in 'XO'):
                borders[step-1] = sign
                gamech = True
            else:
                print('\nЭта ячейка занята!\n')
        else:
            print('\nНеверно указано значение. Укажите номер свободной ячейки (от 1 до 9)!\n')

def win_ch(borders):
    winline = [[0,1,2],
                [3,4,5],
                [6,7,8],
                [0,3,6],
                [1,4,7],
                [2,5,8],
                [0,4,8],
                [2,4,6]]
    for i in winline:
        if borders[i[0]] == borders[i[1]] == borders[i[2]]:
            return borders[i[0]]
    return False

def game(borders):
    count = 0
    win = False
    while not win:
        print_map(borders)
        if count % 2 == 0:
            input_XO('X')
        else:
            input_XO('O')
        count += 1
        if count > 4:
            a = win_ch(borders)
            if a:
                print(f'\n\033[1m\033[4m\033[32m\033[3m{a} выиграл!\033[0m')
                win = True
                break
        if count == 9:
            print(f'\n\033[1m\033[4m\033[32m\033[3mНичья!\033[0m')
            break
    print_map(borders)

game(borders)