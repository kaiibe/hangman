from hangman import Hangman


def copyWords() -> list:
    words_file = open("words.txt", "r")
    words_list = []

    for i in words_file.readlines():
        words_list.append(i.strip().lower())
    words_file.close()

    return words_list


def check_chr(letter) -> bool:
    if len(letter) > 1 or len(letter) == 0:
        return False
    elif letter[0].isalpha():
        return True
    return False


def start():

    words = copyWords()

    while True:
        choice = input("Press Y/y to start: ").lower()

        if choice != 'y':
            break

        game = Hangman(words)
        valid_game = True
        while valid_game != False:

            letter = input("\nEnter your letter: ").lower()
            print("\x1B[2J")

            if check_chr(letter):
                valid_game = game.input_letter(letter)
            else:
                print("You need to enter only/at least ONE letter!!")
