from systems.screen_manager import OpenMenu, CloseMenu
from screens.game_screen import GameScreen
from systems.save_load import *
from systems.audio_manager import *

from time import sleep
import os

buttons = [
    "Easy",
    "Normal",
    "Hard",
    "Nightmare",
    "Load Save"
]


class DifficultiesScreen:
    def __init__(self):
        self.selection = 0
        self.open = False

    def display(self):
        # Clear the screen
        os.system('cls')

        self.open = True

        # Print the title
        print("DIFFICULTIES")

        # Go through the button options, and if we've reached the selected, add arrows
        for i in range(len(buttons)):
            if i == self.selection:
                print(buttons[i] + " <<")
            else:
                print(buttons[i])
        print('\n'*3)
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

        if self.selection != 4:
            self.close()
            CloseMenu()

        # Check what the current button selection is
        match self.selection:
            case 0:
                s = GameScreen("easy")
                s.display()
            case 1:
                s = GameScreen("normal")
                s.display()
            case 2:
                s = GameScreen("hard")
                s.display()
            case 3:
                s = GameScreen("nightmare")
                s.display()
            case 4:
                if SaveExists():
                    # Load save
                    s = GameScreen("", LoadData())
                    s.display()
                else:
                    self.back()
            case 5:
                OpenMenu("main_menu")

    def back(self):
        playSound("blipSelect")

        self.close()

        OpenMenu("main_menu")

    def close(self):
        if not self.open:
            return

        os.system('cls')

        self.open = False
