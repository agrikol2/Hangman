import random


word_list = ["ПОЯСОЧЕК"]
# with open("D:/Python_files/Hangman/word_rus.txt", encoding="utf8") as file:
#     for line in file:
#         word_list.append(line.strip())


def get_word(res):
    result = random.choice(res).upper()
    return result


# функция получения текущего состояния
def display_hangman(tries):
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
    return stages[tries]


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
else:
    print("Let's play Hangman!")


def play(word):
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6
    print(display_hangman(tries))
    print(f"Ваше количество попыток/Your number of tries: {tries}")
    print()
    print("_" * len(word))

    def valid_input():
        while True:
            if lang == "r":
                alphabet = input(
                    "Введите букву или слово целиком:"
                ).upper()  # Но тут после повторного ввода, программа завершает работу
                print()
                if not alphabet.isalpha():
                    print("Повторите ввод")
                else:

                    return alphabet
            else:
                alphabet = input("Enter the letter or word chief:").upper()
                if not alphabet.isalpha():
                    print("Please, re-enter: ")
                else:
                    return alphabet

    input_val = valid_input().upper()

    def Letter_in_a_word(result, input_Letter):
        while True:
            if lang == "r":
                if input_Letter in result:
                    res = ""
                    print("Вы угадали букву!", res, sep="\n")
                    for i in result:
                        if input_Letter != i:
                            res += "_"
                        if input_Letter == i:
                            res += i
                    print(res)
                    return res, valid_input()  # Тут я по идее возвращаюсь к вводу
                else:
                    print("Вы не угалали букву :(")
                    print(display_hangman(tries - 1))
                    print(f"Ваше количество попыток: {tries - 1}")
            else:
                if input_Letter in result:
                    res = ""
                    print("You guessed the letter!", res, sep="\n")
                    for i in result:
                        if input_Letter != i:
                            res += "_"
                        if input_Letter == i:
                            res += i
                    print(res)
                    return res, valid_input()  # Тут я по идее возвращаюсь к вводу
                else:
                    print("You missed the letter :(")
                    print(display_hangman(tries - 1))
                    print(f"Your number of tries: {tries-1}")
                    pass

    Letter_in_a_word(get_word(word_list), input_val)


play(get_word(word_list))
