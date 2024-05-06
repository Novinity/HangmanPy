from systems.screen_manager import OpenMenu
from systems.audio_manager import *
from systems.settings import *

import os

buttons = [
    "Sounds"
]


class OptionsScreen:
    def __init__(self):
        # Initialize default variables
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
            addition = ""
            if i == 0:
                # Show the current value of the Sound Enabled setting
                addition = " - " + str(get_sound_enabled())
            if i == self.selection:
                print(buttons[i] + addition + " <<")
            else:
                print(buttons[i] + addition)

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
        os.system('cls')

        # Check what the current button selection is
        match self.selection:
            case 0:
                # Toggle
                set_sound_enabled(not get_sound_enabled())
                self.display()
            case 1:
                # Open main menu
                OpenMenu("main_menu")
        playSound("blipSelect")

    # So that backspace is usable
    def back(self):
        playSound("blipSelect")
        self.close()

        OpenMenu("main_menu")

    def close(self):
        if not self.open:
            return

        os.system('cls')

        self.open = False
