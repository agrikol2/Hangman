from random import *
from string import ascii_uppercase, ascii_lowercase

rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"


word_list = []
with open("D:/Python_files/Hangman/word_rus.txt", encoding="utf8") as file:
    for line in file:
        word_list.append(line.strip())


def get_word(res):
    result = choice(res).upper()
    return result


# print(get_word(word_list))


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
    word_comlpetion = "_" * len(word)
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6
    print(display_hangman(tries))
    print(word_comlpetion)
    print()

    def valid_input():
        while True:
            if lang == "r":

                alphabet = input("Введите букву или слово целиком:").upper()
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

    input_val = valid_input()


play(get_word(word_list))
