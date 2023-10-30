#  игра с компьютером

# Задача
# Написать игру в “Крестики-нолики”. Можете использовать 
# любые парадигмы, которые посчитаете наиболее 
# подходящими. Можете реализовать доску как угодно - как 
# одномерный массив или двумерный массив (массив массивов). 
# Можете использовать как правила, так и хардкод, на своё 
# усмотрение. Главное, чтобы в игру можно было поиграть через 
# терминал с вашего компьютера.

import random

class Player:
    def __init__(self, player, name):
        self.player = player
        self.name = name


class Computer(Player):

    def __init__(self, player, name):
        super().__init__(player)
        name == "Computer"


    # def get_step():
    #     step = random.randint(1, 9)
    #     return step


class Human_pl(Player):

    def __init__(self, player):
        super().__init__(player)


    # def get_step():
    #     # step = Play.input_XO()
    #     return step
    

class Play():

    def start_choise():
        print('\n\033[1m\033[4m\033[37m\033[45m\033[3mКрестики-нолики\033[0m\n\
        \n\033[3mНеобходимо указать номер ячейки,\
        \n\033[3mв которую хотите поставить крестик/нолик\033[0m\n')

        Computer.name = "Computer"

        print('Меня зовут\033[0m  \033[1m\033[6m\033[32mComputer!\033[0m \nПоиграем вместе?\n')
        h_name = input('\033[3mВведите Ваше имя\033[0m ')
        Human_pl.name = h_name



    borders = list(range(1, 10))


    def print_map(borders):
        print('-  ' * 5)
        for i in range(3):
            print('|', borders[i * 3], '|', borders[i * 3 + 1], '|', borders[i * 3 + 2], '|')
            print('-  ' * 5)


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

        firstTurn = random.randint(1,2)
        if firstTurn == 1:
            currentTurn = Computer.name

        else:
            currentTurn = Human_pl.name
        print(f'\nПервый ход у игрока: \033[32m{currentTurn}\033[0m')



        count = 0
        win = False
        while not win:


            Play.print_map(borders)

            game_ch = False
            while not game_ch:
            
                if  currentTurn == Computer.name:
                    sign = 'X'
                    step = random.randint(1, 9)
                    if (str(Play.borders[step-1]) not in 'XO'):
                        Play.borders[step-1] = sign
                        game_ch = True
                        print(f'Компьютер сделал ход в ячейку: {step}\n')
                        currentTurn = Human_pl.name
                        print(f'Сейчас ход игрока - {currentTurn}\n')
                    else:
                        step = random.randint(1, 9)
                        # continue
                else:
                    sign = 'O'
                    step = input(f'\n\033[3mУкажите номер ячейки, в которую хотите поставить {sign}? \033[0m')
                    try:
                        step = int(step)
                    except:
                        print('\nНеверно указано значение. Укажите номер ячейки (от 1 до 9)!\n')
                        continue
                    if step >= 1 and step <= 9:
                        if (str(Play.borders[step-1]) not in 'XO'):
                            Play.borders[step-1] = sign
                            game_ch = True
                            currentTurn = Computer.name
                            print(f'\nСейчас ход игрока - {currentTurn}')
                        else:
                            print('\nЭта ячейка занята!\n')
                    else:
                        print('\nНеверно указано значение. Укажите номер свободной ячейки (от 1 до 9)!\n')
                        continue

            count += 1


            if count > 4:
                a = Play.win_ch(borders)
                if a:
                    print(f'\n\033[1m\033[4m\033[32m\033[3m{a} выиграл!\033[0m\n')
                    win = True
                    break
            if count == 9:
                print(f'\n\033[1m\033[4m\033[32m\033[3mНичья!\033[0m')
                break
        Play.print_map(borders)


if __name__ == "__main__":
    Play.start_choise()
    Play.game(Play.borders)