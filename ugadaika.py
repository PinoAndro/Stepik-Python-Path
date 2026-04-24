import random

def random_num(edge):
    b = random.randint(1, edge)
    return b

def get_right_edge():
    print("Выберите правую границу диапазона выбора числа")
    a = int(input())
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
        
def try_again():
    try_again = input()
    if try_again == "Да":
        print("Играем дальше! Введите число :)")
        return False
    else:
        return True

count = 0
print("Добро пожаловать в числовую угадайку")
right_edge = get_right_edge()
num = random_num(right_edge)
while True:
    n = is_valid(right_edge)
    count += 1
    if is_in_range(n, num):
        print("Вы угадали, поздравляем!")
        print(f"Количество попыток: {count}")
        print("Хотите сыграть ещё? Просто напишите 'Да'")
        if input() == "Да":
            print("Добро пожаловать в числовую угадайку")
            right_edge = get_right_edge()
            num = random_num(right_edge)
            count = 0
            continue
        else:
            print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
            break
