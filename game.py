from random import randint
from datetime import datetime

class ScoreBoard():
    def __init__(self):
        self.win_counter = {'bot': 0, 'user': 0}

    def cleen_score(self):
        self.win_counter['bot'] = 0
        self.win_counter['user'] = 0

    def update_score(self, is_user_win: bool):
        if is_user_win:
            self.win_counter['user'] += 1
        else:
            self.win_counter['bot'] += 1

    def print_score(self):
        if self.win_counter['user'] == self.win_counter['bot']:
            print('Вам не удалось победить, но вы и не проиграли! Попробуйте еще ;-)', end=' ')
        elif self.win_counter['user'] > self.win_counter['bot']:
            print(f"Поздравляю! Вы победили со счетом", end=' ')
        else:
            print(f"Поражение со счетом:", end=' ')
        print(f"{self.win_counter['user']}:{self.win_counter['bot']}", end='\n\n')

    def save_score(self, file_name='score_log.txt'):
        text = f"{datetime.now()} СЧЕТ: Вы = {self.win_counter['user']}, "\
        f"Бот = {self.win_counter['bot']}, раундов сыграно: {number_rounds}\n"
        try:
            with open(file_name, 'a',  encoding='utf-8') as file:
                file.write(text)
        except IOError as err:
            print(_('Ошибка при сохранении файла:'), err)

sb = ScoreBoard()
global number_rounds
number_rounds = 3
choice = {1: 'Камень', 2: 'Ножницы', 3: 'Бумага'}

def next_bot_move():
    bot_move = randint(1, 3)
    print(f'Соперник выбрал: {choice[bot_move]}')
    return bot_move

def next_user_move():
    print('Камень, ножницы, бумага. 1, 2, 3...')
    
    while True:
        try:
            user_move = int(input('1 - Камень\n2 - Ножницы\n3 - Бумага\nВаш выбор:'))
            if 3 >= user_move >= 1:
                print(f'Вы выбрали: {choice[user_move]}')
                return user_move
            else: 
                print('Ошибка: доступны только 3 варианта (1, 2 или 3)', end='\n\n')
        except ValueError as e:
            print('Ошибка: введите число (1, 2 или 3)', end='\n\n')

def get_winner(bot_move: int, user_move: int):
    win_conditions = {
        1: [2, 'Камень не уязвим перед ножницами.'],
        2: [3,  'Ваши ножницы легко разрезают бумагу соперника.'],
        3: [1, 'Бумага накрывает камень соперника.']
    }
    loss_conditions = {
        2: [1, 'Ваши ножницы сломались о камень.'],
        3: [2, 'Ваша бумага разрезана ножницами соперника.'],
        1: [3, 'Соперник накрывает ваш камень бумагой.']
    }
    if user_move == bot_move:
        print('Ничья', end='\n\n')
    elif win_conditions[user_move][0] == bot_move:
        print(win_conditions[user_move][1], 'Ваша победа в раунде!', end='\n\n')
        sb.update_score(is_user_win=True)
    elif loss_conditions[user_move][0] == bot_move:
        print(loss_conditions[user_move][1], 'Раунд в пользу соперника...', end='\n\n')
        sb.update_score(is_user_win=False)
    else:
        print('Если вы это видите, значит разработчик что-то не учел в этой игре. '\
              'Пожалуйста сообщите ему об этом!')

def game_menu():
    menu = f"""
1 - Начать новую игру
2 - Изменить количество раундов (текущее значение: {number_rounds})
3 - Покинуть игру
Укажите цифру: """
    while True:
        try:
            choice_menu = int(input(menu))
            if 3 >= choice_menu >= 1:
                return choice_menu
            else:
                print('Ошибка: доступны только 3 варианта (1, 2 или 3)', end='\n\n')
        except ValueError as e:
            print('Ошибка: введите число (1, 2 или 3)', end='\n\n')

def start_game():
    print('Начало игры')
    # Чтобы предыдущая игра не влияла на результат - обнуляем счет игры
    sb.cleen_score()
    for round in range(number_rounds):
        # Для корректного отображения номера раунда 
        print(f'Раунд {round + 1}:')
        user = next_user_move()
        bot = next_bot_move()
        get_winner(bot_move=bot, user_move=user)
    sb.print_score()
    sb.save_score()

def set_number_rounds():
    while True:
        try:
            answer = int(input('Укажите количество раундов:'))
            if answer > 0:
                return answer
            else:
                print('Укажите число больше 0', end='\n\n')
        except ValueError as e:
            print('Ошибка: введите число', end='\n\n')

if __name__ == "__main__":
    print('Игра "Камень, ножницы, бумага"')
    while True:
        menu = f"""Меню:
1 - Начать новую игру
2 - Изменить количество раундов (текущее значение: {number_rounds})
3 - Покинуть игру
Укажите цифру: """
        try:
            choice_menu = int(input(menu))
            if 3 >= choice_menu >= 1:
                match choice_menu:
                    case 1:
                        start_game()
                    case 2:
                        number_rounds = set_number_rounds()
                    case 3:
                        print('До новых встречь!')
                        break
            else:
                print('Ошибка: доступны только 3 варианта (1, 2 или 3)', end='\n\n')
        except ValueError as e:
            print('Ошибка: введите число (1, 2 или 3)', end='\n\n')
