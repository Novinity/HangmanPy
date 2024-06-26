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
        for difficulty in data:
            print(difficulty.upper())
            # Print title accordingly based on the amount of high scores
            if len(data[difficulty]) >= 5:
                print("(Top 5)")
            elif len(data[difficulty]) == 0:
                print("No high scores yet! Why don't you be the first?")
                continue
            # Sort the data
            sorted_data = dict(reversed(list(json.loads(
                json.dumps({k: v for k, v in sorted(data[difficulty].items(), key=lambda item: int(item[1]))})).items())))

            index = 1
            # Go through the top 5 placeholders and add them to the screen
            for i in sorted_data:
                if index == 6:
                    break
                print(f"> {str(index)}. {i}: {str(sorted_data[i])}")
                index += 1
            print('\n')

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
