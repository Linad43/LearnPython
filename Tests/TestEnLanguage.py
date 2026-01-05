words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута"
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать"
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме"
}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично"
}


def choose_difficulty():
    """
    Выбор сложности,
    и при некорректном вводе,
    выбрать среднюю сложность
    """
    print("Выберите уровень сложности: легкий, средний, сложный.")
    difficulty = input().lower()

    match difficulty:
        case "легкий":
            return words_easy
        case "средний":
            return words_medium
        case "сложный":
            return words_hard
        case _:
            return words_medium


def play_game(words):
    """
    Игра в слова,
    ввод перевода слова и проверка на корректность ввода
    """
    answers = {}
    for word, value in words.items():
        # length_value = value.size()
        # first_char_value = value[0]
        print(f"{word}, {len(value)} букв, начинается на {value[0]}...\n")
        answer = input()
        answers[word] = bool(value == answer)
    return answers


def display_results(answers):
    """
    Вывод результатов игры
    """
    correct_words = []
    incorrect_words = []
    for word in answers.keys():
        if answers[word]:
            correct_words.append(word)
        else:
            incorrect_words.append(word)
    print("Правильно переведенные слова:\n")
    result = 0
    for word in correct_words:
        print(word)
    print("\nОшибки в словах:\n")
    for word in incorrect_words:
        print(word)
    calculate_rank(answers)


def calculate_rank(answers):
    """
    Вывод полученного ранга
    """
    correct_count = sum(answers.values())
    rank = levels[correct_count]
    print("\nВаш ранг:")
    print(rank)

words = choose_difficulty()
display_results(play_game(words))
print("\nЗавершение программы.")
