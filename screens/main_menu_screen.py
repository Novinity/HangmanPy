from systems.screen_manager import OpenMenu
from systems.audio_manager import *

import os

buttons = [
    "Play",
    "Options",
    "Scores",
    "Quit"
]


class MainMenuScreen:
    def __init__(self):
        # Initialize default variables
        self.selection = 0
        self.open = False

    def display(self):
        # Clear the screen
        os.system('cls')

        self.open = True

        # Print the title
        print(" HANGMAN")
        print("    O")
        print("   /|\\")
        print("   / \\\n")

        # Go through the button options, and if we've reached the selected, add arrows
        for i in range(len(buttons)):
            if i == self.selection:
                print(buttons[i] + " <<")
            else:
                print(buttons[i])

    def change_selection(self, dir):
        playSound("click")
        # Check which direction it is
        if dir == "up":
            # If we're at the first element, go to the last
            if self.selection == 0:
                self.selection = len(buttons) - 1
            # Otherwise, just go up by one
            else:
                self.selection -= 1
        elif dir == "down":
            if self.selection == len(buttons) - 1:
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
                # Open difficulties menu
                OpenMenu("difficulties")
            case 1:
                # Open options menu
                OpenMenu("options")
            case 2:
                # Open scores menu
                OpenMenu("scores")
            case 3:
                # Exit app
                exit(0)

    # So there's no errors, but it's not needed since nothing is before the main menu
    def back(self):
        pass

    def close(self):
        if not self.open:
            return

        os.system('cls')

        self.open = False
