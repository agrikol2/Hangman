from Module_1.f.utils import *


def play(word):

    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6
    if lang == "r":
        print("Давайте играть в угадайку слов!")
        print(display_hangman(tries))
        print(f"Ваше количество попыток/Your number of tries: {tries}")
        print()
        print("_" * len(word))

    else:
        print("Let's play Hangman!")

    # print(display_hangman(tries))
    # print(f"Ваше количество попыток/Your number of tries: {tries}")
    # print()
    # print("_" * len(word))


play(get_word(word_list))
