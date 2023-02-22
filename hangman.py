import random
import hanger


class Hangman:
    def __init__(self, words):

        print("\x1B[2J")
        print("\nLet the game begin!")

        self.words = words
        self.random_word = self.getRandomWord()
        self.user_word = "_ " * len(self.random_word)
        self.number_of_tries = 7
        self.number_of_correct_letters = 0
        self.repeated_words = {}
        self.hanger = hanger.create_hanger()

        self.printInfo()

    def getRandomWord(self) -> str:
        random_int = random.randint(0, len(self.words)-1)
        random_word = self.words[random_int]
        print(
            f"Use the random word only for debug purpose!! '{random_word}'\n")
        return random_word

    def printInfo(self) -> None:
        print(f"Your current progress {self.user_word}")
        hanger.print_hanger(self.hanger)

        if self.number_of_tries > 1:
            print(f"You have {self.number_of_tries} more tries! ")
        else:
            print(f"You have {self.number_of_tries} more try! ")

    def input_letter(self, letter) -> bool:

        if letter in self.repeated_words:
            print("You have already picked this letter\n")
            self.printInfo()
            return True
        elif letter in self.random_word:
            valid_game = self.correctLetter(letter)
            self.repeated_words[letter] = True
            return valid_game
        else:
            valid_game = self.incorrectLetter()
            self.repeated_words[letter] = True
            return valid_game

    def correctLetter(self, letter) -> bool:
        print("Correct!!\n")
        for i in range(0, len(self.random_word)):
            if letter == self.random_word[i]:
                p = i + i
                self.assignLetter(letter, p)
                self.number_of_correct_letters += 1

        if self.number_of_correct_letters == len(self.random_word):
            self.game_won()
            return False

        self.printInfo()
        return True

    def assignLetter(self, letter, p) -> None:
        word = list(self.user_word)
        word[p] = letter
        self.user_word = ''.join(word)

    def incorrectLetter(self) -> bool:
        print("Incorrect!!\n")

        self.number_of_tries -= 1
        hanger.hang_it(self.hanger, self.number_of_tries)

        if self.number_of_tries == 0:
            self.game_lost()
            return False

        self.printInfo()
        return True

    def game_lost(self) -> None:
        print("Game is Over. You Lost!")
        hanger.print_hanger(self.hanger)
        print(f"Your word was '{self.random_word}'\n\n")

    def game_won(self) -> None:
        print("Game is Over. You Won!")
        hanger.print_hanger(self.hanger)
        print(f"Your word was '{self.random_word}'\n\n")
