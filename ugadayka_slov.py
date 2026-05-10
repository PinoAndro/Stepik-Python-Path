import random

def get_word():
    return random.choice(word_list).upper()

def display_hangman(tries): # Рисуем виселицу
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play():
   word = get_word()
   guessed = False
   tries = 6 # количество попыток
   while guessed == False:
      word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова                    # сигнальная метка
      guessed_letters = []               # список уже названных букв
      guessed_words = []                 # список уже названных слов                   
      print('Давайте играть в угадайку слов!')
      print(display_hangman(tries))
      while guessed == False:
         print(word_completion)
         print("Введите букву или слово:")
         while tries > 0:
                  input_choice = input()
                  if len(input_choice) == 1:
                     char = input_choice.upper()
                     if char.isalpha():
                        if char in guessed_letters:
                           print("Буква уже была названа!")
                           continue
                        guessed_letters.append(char)
                     else:
                        print("Давай все-таки введем букву :)")
                     if char in word:
                        word_completion_list = list(word_completion)
                        for index, value in enumerate(word):
                           if value == char:
                              word_completion_list[index] = word[index]
                        word_completion = ''.join(word_completion_list)
                        if word_completion == word: 
                           left_tries = 7 - tries
                           print(f'Поздравляем, вы угадали слово {word} за {left_tries} попыток! Вы победили!')
                           guessed = True
                           break
                        tries -= 1
                        print(f'Число оставшихся попыток: {tries}')
                        print(display_hangman(tries))
                        break
                     else:
                        print("Такой буквы нет!")
                        tries -= 1
                        print(f'Число оставшихся попыток: {tries}')
                        print(display_hangman(tries))
                        break
                  
                  else:
                     while True:
                           char = input_choice.upper()
                           if char.isalpha():
                              break
                           else:
                              print("Давай все-таки введем слово :)")
                     while tries > 0:
                           if char in guessed_words:
                              print("Слово уже было названо!")
                              char = input()
                           elif char == word:
                              left_tries = 7 - tries
                              print(f'Поздравляем, вы угадали слово {word} за {left_tries} попыток! Вы победили!')
                              guessed = True
                              tries = 0

                           else:
                              print("Неверное слово!")
                              print(word)
                              tries -= 1
                              print(f'Число оставшихся попыток: {tries}')
                              print(display_hangman(tries))
                              guessed_words.append(char)
                              break
                  if tries == 0 and char != word:
                     print("Игра окончена! Вы проиграли!")
                     guessed = True
                     break



word_list = ['КЛОУН', "КОТ", "ПАРУС", "СМЕХ", "КЛЮЧ", "МОЛОКО", "КАРАБАС", "КУТУС"]
game_is_on = True
while game_is_on:
   play()
   print("Напишите что-нибудь, если хотите снова поиграть")
   again_or_not = input()
   if len(again_or_not) > 0:
      game_is_on = True
