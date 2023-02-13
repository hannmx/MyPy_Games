from random import randint

def player_move(name_player, candies, max_count):
    check = False
    while not check:
        move = input(f'{name_player}, твой ход!\nКоличество конфет: ')
        try:
            move = int(move)
            if move > 0 and move <= max_count and move <= candies:
                print(f'Ты забрал {move} конфет')
                candies -= move
                print(f'Осталось {candies} конфет')
                check = True
            else:
                print(f'Количество взятых конфет не должно быть меньше 1 или больше {max_count} и не больше оставшегося количества конфет!')
        except:
            print('Вводите только целые числа!')
        return candies

def stupid_bot_move(candies, max_count):
    if candies >= max_count:
        move = randint(1, max_count)
        print(f'Бот забрал {move} конфет')
        candies -= move
        print(f'Осталось {candies} конфет')
    else:
        move = randint(1, candies)
        print(f'Бот забрал {move} конфет')
        candies -= move
        print(f'Осталось {candies} конфет')
    return candies

def smart_bot_move(candies, max_count):
    if candies >= max_count:
        move = candies % (max_count + 1)
        print(f'Бот забрал {move} конфет')
        candies -= move
        print(f'Осталось {candies} конфет')
    else:
        move = candies
        print(f'Бот забрал {move} конфет')
        candies -= move
        print(f'Осталось {candies} конфет')
    return candies

def check_win(candies, determing_moves, first_name, second_name):
    if candies == 0:
        if determing_moves % 2 == 0: 
            return first_name
        else: 
            return second_name
    else:
        return False