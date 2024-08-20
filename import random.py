import random


word_list: list = ["ПОЯСОЧЕК"]
# with open("D:/Python_files/Hangman/word_rus.txt", encoding="utf8") as file:
#     for line in file:
#         word_list.append(line.strip())


def get_word(res: list) -> str:
    result = random.choice(res).upper()
    return result


# функция получения текущего состояния
def display_hangman(tries: int) -> str:
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


lang: str = valid_lang()

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

    def valid_input() -> str:  # не обязательно делать вложенной, вытащи её наружу
        while True:
            if lang == "r":
                alphabet = input(
                    "Введите букву или слово целиком:"
                ).upper()  # Но тут после повторного ввода, программа завершает работу
                print()  # Зачем? Добавь /n в инпут
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

    def Letter_in_a_word(
        result: str, input_Letter: str
    ):  # не обязательно делать вложенной, вытащи её наружу
        while True:  # Подумай, нужен ли тут вообще этот цикл?
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
                    return res, valid_input()  # Тут у тебя шиза слегонца
                    # Поэтому и не происходит ввод второй буквы - ты выходишь из функции и заканчиваешь игру

                else:
                    print("Вы не угалали букву :(")
                    print(
                        display_hangman(tries := tries - 1)
                    )  # Ты не обновил переменную tries. Можно так - Погугли про моржовый оператор
                    print(f"Ваше количество попыток: {tries}")
                    # И что происходит дальше? Цикл пошел по новой, вместо того, чтобы продолжить игру)

    Letter_in_a_word(get_word(word_list), input_val)


play(get_word(word_list))
