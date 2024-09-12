import random


word_list = ["поясочек"]
# with open("D:/Python_files/Hangman/word_rus.txt", encoding="utf8") as file:
#     for line in file:
#         word_list.append(line.strip())

guessed_letters: list = []  # список уже названных букв
guessed_words: list = []  # список уже названных слов
tries: int = 6


def get_word(res):
    result = random.choice(res).upper()
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
    res = "_" * len(get_word(word_list))
    while tries > 1:

        if lang == "r":
            if input_Letter in result:
                for i in result:
                    if input_Letter != i:
                        res += "_"
                    if input_Letter == i:
                        res += i
                    if input_Letter == result:
                        res += input_Letter  # Удалить
                        print(f"Вы угадали все слово целиком: {word_list[0]}")
                        exit()
                print("Вы угадали букву!", res, sep="\n")
                input_Letter = valid_input()

            else:
                print(stages[tries - 1])
                print(res)
                print(tries := tries - 1)
                valid_input()

    print("У вас закончились попытки, игра закончена", stages - 6)


Letter_in_a_word(get_word(word_list), input_val, tries)
