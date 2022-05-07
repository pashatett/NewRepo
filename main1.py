# игра крестики нолики
# 1)создать игровое поле
# 2)проверка победителя после каждого хода
# 3)ход каждого игрока
# 4)условие победы

# -------
# |_|_|_|
# |_|_|_|
# |_|_|_|
# -------

board_list = [i for i in range(1,10)]
c = 0
player_list1 = []
player_list2 = []

# отображение игровой доски
def board():
    print('-'*7)
    for i in range(3):
        print('|{}|{}|{}|'.format(board_list[0+i*3], board_list[1+i*3], board_list[2+i*3]))
    print('-'*7)

# ход каждого игрока
def check_player(a):
    global c
        print('игрок, куда поставить {}?'.format(a))
        player_one_check = int(input('число от 1 до 9: '))
        if board_list[player_one_check-1]!='X' and /
            board_list[player_one_check-1]!='O':
            board_list[player_one_check-1] = a
        else:
            print('выберете другую клетку')
        board()
        c+=1


# условие выигрыша
def win():
    win_list = ((1,2,3),(4,5,6),
    (7,8,9),(1,4,7),(2,5,8),
    (3,6,9),(1,5,9),(3,5,7))


check_player()
while True:
    if c%2 == 0:
        check_player('X')
    else:
        check_player('O')
    c = 0



