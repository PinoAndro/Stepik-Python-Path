import random

num = random.randint(1, 100)

while True:
    n = int(input())
    if num > n:
        print("Слишком мало, попробуйте еще раз")
        continue
    elif num < n:
        print("Слишком много, попробуйте еще раз")
        continue
    else:
        print("Вы угадали, поздравляем!")
        break
