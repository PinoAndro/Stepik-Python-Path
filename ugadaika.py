import random

def the_game():
    count = 0
    print("Добро пожаловать в числовую угадайку")
    right_edge = get_right_edge()
    num = random_num(right_edge)
    return count, right_edge, num

def random_num(edge): # Получаем загаданное число
    b = random.randint(1, edge)
    return b

def get_right_edge(): # Получаем правую границу диапазона
    print("Выберите правую границу диапазона выбора числа")
    incorrect = True
    while incorrect:
        a = input()
        try:
            a = int(a)
            incorrect = False
        except ValueError:
            print(f"Давай все-таки введем целое число :)")
    print(f"Теперь пробуем угадать число от 1 до {a}?")
    return a

def is_valid(edge): # Проверяем корректность ввода
    while True:
        u_input = input()
        try:
            n = int(u_input)
            if 1 <= n <= edge:
                return n
            else:
                print(f"А может быть все-таки введем целое число от 1 до {edge}?")
        except ValueError:
            print(f"А может быть все-таки введем целое число от 1 до {edge}?")
            

def is_in_range(number, target): # Проверяем в допустимом ли диапазоне
    while True:
        if number < target:
            print("Ваше число меньше загаданного, попробуйте еще разок")
            return False
        if number > target:
            print("Ваше число больше загаданного, попробуйте еще разок")
            return False
        else:
            return True
        
def try_again(): # Проверяем, хотим ли заново сыграть
    try_again = input()
    if try_again == "Да":
        print("Играем дальше! Введите число :)")
        return False
    else:
        return True

game_is_done = False
while game_is_done == False:
    count, right_edge, num = the_game()
    while True:
        n = is_valid(right_edge)
        count += 1
        if is_in_range(n, num):
            print("Вы угадали, поздравляем!")
            print(f"Количество попыток: {count}")
            break
    print("Хотите сыграть ещё? Просто напишите 'Да'")
    if input() == "Да":
        count = 0
        continue
    else:
        print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
        game_is_done = True
        break
