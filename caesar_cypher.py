def get_cypher(txt, lang, rot, route): # Получаем шифр
    newtext = ''
    a = 1
    b = 26
    if lang == 1:
          b = 32
    if route == 2:
         a = -1
    for char in txt:
        if char.isalpha():
            if char.isupper():
                newtext += list_of_languages[lang][(list_of_languages[lang].find(char.lower()) + rot * a) % b].upper()
            else:
                newtext += list_of_languages[lang][(list_of_languages[lang].find(char) + rot * a) % b]          
        else:
            newtext += char
    return newtext

eng = 'abcdefghijklmnopqrstuvwxyz'
rus = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
list_of_languages = ["abcdefghijklmnopqrstuvwxyz", "абвгдежзийклмнопрстуфхцчшщъыьэюя"]
print("Введите текст")
text = input()
print("Шифруем(введите 1) или дешифруем(введите 2)? ")
route_of_cypher = int(input())
print("Выберите язык: Английский - 0, Русский - 1")
language = int(input())
print("Шаг сдвига?")
rotate = int(input())
print(get_cypher(text, language, rotate, route_of_cypher))
