# объявление функции
def is_password_good(password):
    lst = []
    if len(password) > 7:
            lst.append(3)
    for char in password:
        if char.islower():
            lst.append(1)
        if char.isupper():
            lst.append(2)
        if char.isdigit():
            lst.append(4)
    for j in range(1, 5):
        if j in lst:
            continue
        else:
            return False
    return True
    

# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))
