import random

def generate_code_code_boys(phone_number, chars_of_code):
    code = ''
    for i in phone_number:
        if i == '-':
            continue
        i = int(i)
        code += chars_of_code[i]
    return code

print("Введи номер, пацан")
phone_number = input()
chars_of_code = '5987604321'
print('Стрингер получит сообщение. Красава!')
print(generate_code_code_boys(phone_number, chars_of_code))
