from systems.screen_manager import OpenMenu
from systems.word_manager import *
from state.hangman_state import getState
from systems.save_load import *
from systems.audio_manager import *

import os


class GameScreen:
    def __init__(self, difficulty, saveData=None):
        self.open = False

        if saveData is not None:
            #print(saveData)
            self.chances = saveData["chances"]
            self.word = saveData["word"]
            self.mistakes = saveData["mistakes"]
            self.blanks = getBlanksFromFoundLetters(self.word, saveData["found"])

            self.blanks = self.blanks.strip()
        else:
            self.chances = 10

            match difficulty:
                case "easy":
                    self.chances = 10
                case "normal":
                    self.chances = 10
                case "hard":
                    self.chances = 7
                case "nightmare":
                    self.chances = 5

            self.word = getRandomWord(difficulty)
            self.mistakes = []
            self.difficulty = difficulty
            self.blanks = ("_ " * len(self.word)).strip()

    def display(self):
        # Clear the screen
        os.system('cls')

        self.open = True

        print(f"Chances: {self.chances}")

        if checkWin(self.blanks, self.word):
            print("   " + getState(-1))
            print('\n' * 2)
            print("You saved him!")
            print(f"Your final score: {self.chances}")
            DeleteSaveData()
            save = input("Save score? (y/n) ")
            while True:
                if save.lower() == 'y':
                    name = input("What's your name? ")
                    if name.strip() == '':
                        print("That is not a valid name!")
                        continue
                    if SaveHighScore(name, str(self.chances)):
                        print("Successfully saved score!")
                    else:
                        print("Oops! An error occurred while saving your score :(")
                    input("Press enter to continue")

                    self.close()
                    OpenMenu("main_menu")
                    break
                elif save.lower() == 'n':
                    self.close()
                    OpenMenu("main_menu")
                    break
                else:
                    print("That's not an option!")
                    save = input("Save data? (y/n) ")
            return

        print("   " + getState(self.chances))

        if self.chances == 0:
            print("You killed him. He's dead now. Are you happy with yourself?\n")
            print(f"The word was: {self.word}\n")
            input("Press enter to return to the menu.")
            self.close()
            OpenMenu("main_menu")
        else:
            print(self.blanks)
            print('\n' * 2)
            print("Used Letters:", ' '.join(self.mistakes))

            guess = input("Guess >> ")

            if guess.strip().lower() == 'exit':
                self.back()
                return

            # If it's not empty
            if guess.strip() != '':
                guess = guess.upper().strip()
                # If they're inputting more than one character
                if len(guess) > 1:
                    playSound("click")
                    print("You can't input more than one character!")
                    input("Press enter to guess again")
                else:
                    if not guess.isalpha():
                        playSound("click")
                        print("You can only use letters!")
                        input("Press enter to guess again")
                    # If they've already guessed the letter
                    elif guess in self.mistakes or guess in self.blanks:
                        playSound("click")
                        print("You've already used that letter!")
                        input("Press enter to guess again")
                    # If the letter's in the word
                    elif checkLetterMatch(guess, self.word):
                        # Get the new word
                        playSound("pickupCoin")
                        self.blanks = getNewWordMatch(guess, self.word, self.blanks)
                    else:
                        # Add a mistake and decrease their chances
                        playSound("hitHurt")
                        self.mistakes.append(guess)
                        self.chances -= 1

            self.display()

    def change_selection(self, dir):
        pass

    # So that there's no errors, but there's nothing selectable
    def select(self):
        pass

    def back(self):
        # Check if they've won
        if not checkWin(self.blanks, self.word):
            os.system('cls')
            in1 = input("Are you sure you want to exit? (y/n) ")
            if in1.lower().strip() == "y":
                while True:
                    in2 = input("Do you want to save? (y/n) ")
                    if in2.lower().strip() == "y":
                        # Generate info list
                        info = {
                            "word": self.word,
                            "chances": self.chances,
                            "mistakes": self.mistakes,
                            "found": getFoundLettersFromBlanks(self.blanks)
                        }
                        # Save info
                        SaveData(info)

                        # Return to the menu
                        self.close()
                        OpenMenu("main_menu")
                        break
                    elif in2.lower().strip() == "n":
                        self.close()
                        OpenMenu("main_menu")
                        break
                    else:
                        print("That's not an option!")
                        continue
            elif in1.lower().strip() == "n":
                self.display()
            else:
                print("That's not an option!")
                self.back()

    def close(self):
        if not self.open:
            return

        os.system('cls')

        self.open = False
