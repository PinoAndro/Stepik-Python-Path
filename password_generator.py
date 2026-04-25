import random

def generate_password(length, chars, true_chars):
    count = 0
    password = ''
    chars_to_cut = "il1Lo0O"
    if true_chars:
        for char in chars_to_cut:
                chars = chars.replace(char, "")
    while count != length:
        count += 1
        password += random.choice(chars)
    return password

digits = '0123456789'
lowercase_letters =  'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

print('Приветствую! Сколько паролей сгенерировать?')
count_of_passwords = int(input())
print('Длина пароля?')
length = int(input())
print('Цифры включать?')
if input() == 'Да':
    chars += digits
print('Прописные буквы включать?')
if input() == 'Да':
    chars += lowercase_letters
print('Строчные буквы включать?')
if input() == 'Да':
    chars += uppercase_letters
print('Символы включать?')
if input() == 'Да':
    chars += punctuation
true_chars = False
print('Исключать неоднозначные символы "il1Lo0O"?')
if input() == "Да":
    true_chars = True
for _ in range(count_of_passwords):
    print(generate_password(length, chars, true_chars))
