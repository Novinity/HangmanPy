from systems.screen_manager import OpenMenu
from systems.audio_manager import *

import os

buttons = [
    "Music",
    "Sounds"
]


class OptionsScreen:
    def __init__(self):
        self.selection = 0
        self.open = False

    def display(self):
        # Clear the screen
        os.system('cls')

        self.open = True

        # Print the title
        print("OPTIONS")
        print('\n')

        # Go through the button options, and if we've reached the selected, add arrows
        for i in range(len(buttons)):
            if i == self.selection:
                print(buttons[i] + " <<")
            else:
                print(buttons[i])

        print('\n'*5)
        if self.selection == len(buttons):
            print("Back <<")
        else:
            print("Back")

    def change_selection(self, dir):
        playSound("click")
        # Check which direction it is
        if dir == "up":
            # If we're at the first element, go to the last
            if self.selection == 0:
                self.selection = len(buttons)
            # Otherwise, just go up by one
            else:
                self.selection -= 1
        elif dir == "down":
            if self.selection == len(buttons):
                self.selection = 0
            else:
                self.selection += 1

        self.display()

    def select(self):
        playSound("blipSelect")
        os.system('cls')

        # Check what the current button selection is
        match self.selection:
            case 0:
                # Toggle music
                pass
            case 1:
                # Toggle sounds
                pass
            case 2:
                # Open main menu
                OpenMenu("main_menu")

    # So that backspace is uesable
    def back(self):
        playSound("blipSelect")
        self.close()

        OpenMenu("main_menu")

    def close(self):
        if not self.open:
            return

        os.system('cls')

        self.open = False
