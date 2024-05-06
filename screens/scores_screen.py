from systems.screen_manager import OpenMenu
from systems.audio_manager import *

from systems.save_load import *


class ScoresScreen:
    def __init__(self):
        # Initialize default variable
        self.open = False

    def display(self):
        # Clear the screen
        os.system('cls')

        self.open = True

        # Print the title
        print("SCORES")

        # Load the high scores
        data = LoadHighScores()
        # Print title accordingly based on the amount of high scores
        if len(data) >= 5:
            print("(Top 5)")
        elif len(data) == 0:
            print("No high scores yet! Why don't you be the first?")
        print("\n")
        index = 1
        # Go through the top 5 placeholders and add them to the screen
        for i in data:
            if index == 6:
                break
            print(f"> {str(index)}. {i}: {str(data[i])}")
            index += 1

        print("\n"*5)
        print("Back <<")

    def change_selection(self, dir):
        pass

    # Back is the only selectable
    def select(self):
        playSound("blipSelect")
        os.system('cls')

        OpenMenu("main_menu")

    # So backspace is useable
    def back(self):
        playSound("blipSelect")
        self.close()

        OpenMenu("main_menu")

    def close(self):
        if not self.open:
            return

        os.system('cls')

        self.open = False
