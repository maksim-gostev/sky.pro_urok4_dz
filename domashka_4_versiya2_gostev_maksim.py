# создаём словари вопросав
words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}
# словарь подведения ранга
levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}
# словарь правельности или неправельности ответов
answers_dictionary = {}
# словарь для обработки вопросов
words = {}
# правельных ответов
count = 0
# цикл выбора уровня сложности
while True:
    selection_difficulty = input('Выбирите уровень сложности(легко, средне, сложно):')
    if selection_difficulty == 'легко':
        words = words_easy.copy()
        break
    elif selection_difficulty == 'средне':
        words = words_medium.copy()
        break
    elif selection_difficulty == 'сложно':
        words = words_hard.copy()
        break
    else:
        print('Непонятный ответ попробуйте снова\n_________________________________________')
# цикл обработки ответов на вопросы
for keys, item in words.items():
    print(f'{keys}, {len(item)}, начинается {item[0]}...')
    answer = input()
    if answer == item:
        print(f'Верно. {keys.title()} — это {item}.')
    else:
        print(f'Неверно. {keys.title()} — это {item}.')
    answers_dictionary[keys] = answer == item

print('Правильно отвечены слова:')
# цикл подсчёта правельных ответов
for keys in answers_dictionary.keys():
    if answers_dictionary[keys] is True:
        print(keys)
        count += 1
print('______________________________')
print('Неправильно отвечены слова:')
# цикл подчсёта неправельных ответов
for keys in answers_dictionary.keys():
    if answers_dictionary[keys] is False:
        print(keys)
print('_______________________________')
# вывод ранга
print(f'Ваш ранг: {levels[count]}')
