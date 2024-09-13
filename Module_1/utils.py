import random


word_list = [
    "СЛОВО",
    "КЛИМАТ",
    "СТЕНА",
    "КЛАВИАТУРА",
    "АВТОМОБИЛЬ",
    "КОЛОННА",
    "КОШКА",
    "БУТЕРБРОД",
    "СТЕКЛО",
    "ДВЕРЬ",
    "ШТОРА",
]
# with open("D:/Python_files/Hangman/word_rus.txt", encoding="utf8") as file:
#     for line in file:
#         word_list.append(line.strip().upper())


tries: int = 6

result = random.choice(word_list)


def get_word(res):
    return result


# функция получения текущего состояния
stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
    """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
    # голова, торс, обе руки, одна нога
    """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                """,
    # голова, торс, обе руки
    """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                """,
    # голова, торс и одна рука
    """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                """,
    # голова и торс
    """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                """,
    # голова
    """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
    # начальное состояние
    """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """,
]


def valid_lang() -> str:
    while True:
        lang_choice = input(
            "Выберете язык/Choose language: R = русский, E = english: "
        ).lower()
        if lang_choice not in ["r", "e"]:
            print(
                "Вы ввели не верно. Ведите один из вариантов ответа/You entered incorrectly. Enter one of the answer options"
            )
        else:
            return lang_choice


lang = valid_lang()

if lang == "r":
    print("Давайте играть в угадайку слов!")
    print(stages[tries])
    print(f"Ваше количество попыток: {tries}")

    print()
    print("_" * len(get_word(word_list)))


else:
    print("Let's play Hangman!")


def valid_input() -> str:
    while True:
        if lang == "r":
            alphabet = input("Введите букву или слово целиком:").upper()
            if not alphabet.isalpha():
                print("Повторите ввод")
            else:
                return alphabet.upper()


input_val = valid_input()


def Letter_in_a_word(result: str, input_Letter: str, tries):
    res = "_" * len(result)
    while tries > 0:
        if lang == "r":
            if input_Letter in result:
                if input_Letter == result:
                    print(f"Вы угадали все слово целиком: {result}")
                    exit()
                for i in range(len(result)):
                    if input_Letter == result[i]:
                        res = res[:i] + result[i] + res[i + 1 :]
                if res == result:
                    print(f"Вы угадали все слово целиком: {result}")
                    exit()
                print("Вы угадали букву!", res, sep="\n")
                input_Letter = valid_input()

            else:
                print("Вы не угадали букву. Попробуйте ещё раз")
                print(stages[tries := tries - 1])
                print(f"Количество оставшихся попыток: {tries}")
                print(res)
                input_Letter = valid_input()
                # if (
                #     tries > 0
                # ):  # Проверка, чтобы не предлагать ввод, если попыток больше нет
                #     input_Letter = valid_input()
    print(
        f"У вас закончились попытки, игра закончена. Загаданное слово: {result}",
        stages[tries - 7],
    )
    exit()


Letter_in_a_word(get_word(word_list), input_val, tries)
