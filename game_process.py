from random import randint

import defsCandies

def player_vs_stupid_bot (candies, max_count):
    name_player = input('Введите свое имя: ')
    count_for_check_win = candies // max_count
    determing_moves = randint(0, 1)
    win = False
    while not win:
        if determing_moves % 2 == 0:
            candies = defsCandies.player_move(name_player, candies, max_count)
        else:
            candies = defsCandies.stupid_bot_move(candies, max_count)
        if determing_moves >= count_for_check_win - 1:
            temp = defsCandies.check_win(candies, determing_moves, name_player, 'Бот')
            if temp:
                print(f'{temp} выиграл')
                win = True
        determing_moves += 1

def player_vs_smart_bot (candies, max_count):
    name_player = input('Введите свое имя: ')
    count_for_check_win = candies // max_count
    determing_moves = randint(0, 1)
    win = False
    while not win:
        if determing_moves % 2 == 0:
            candies = defsCandies.player_move(name_player, candies, max_count)
        else:
            candies = defsCandies.smart_bot_move(candies, max_count)
        if determing_moves >= count_for_check_win - 1:
            temp = defsCandies.check_win(candies, determing_moves, name_player, 'Бот')
            if temp:
                print(f'{temp} выиграл')
                win = True
        determing_moves += 1

def player_vs_player (candies, max_count):
    name_first_player = input('Как зовут первого игрока: ')
    name_second_player = input('Как зовут второго игрока: ')
    count_for_check_win = candies // max_count
    determing_moves = randint(0, 1)
    win = False
    while not win:
        if determing_moves % 2 == 0:
            candies = defsCandies.player_move(name_first_player, candies, max_count)
        else:
            candies = defsCandies.player_move(name_second_player, candies, max_count)
        if determing_moves >= count_for_check_win - 1:
            temp = defsCandies.check_win(candies, determing_moves, name_first_player, name_second_player)
            if temp:
                print(f'{temp} выиграл(а)')
                win = True
        determing_moves += 1