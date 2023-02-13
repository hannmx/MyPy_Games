import game_process
import os

os.system('cls')

candies = 2021
max_count = 28

type_game_process = input('Введите 1, если хотите режим игры "игрок vs игрок", и любой другой символ, если режим игры "игрок vs бот"')
if type_game_process == '1':
    game_process.player_vs_player(candies, max_count)
else:
    while True:
        bot_choice = input('Два режима игры с ботом: 0 - легкий, 9 - тяжелый\n')
        print('Вы выбираете режим: ')
    
        if bot_choice == '0':
            game_process.player_vs_stupid_bot(candies, max_count)
            False
        elif bot_choice == '9':
            game_process.player_vs_smart_bot(candies, max_count)
            False
        else:
            print('Введите 0 или 9, чтобы выбрать нужный режим игры с ботом!')
