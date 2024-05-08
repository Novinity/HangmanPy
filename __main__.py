import systems.installation as installation

if not installation.CheckForMissing():
    installation.PromptInstallation()
    exit()

from systems.save_load import *
from systems.screen_manager import OpenMenu
import os

import keyboard

if not os.path.exists("./data"):
    os.mkdir("./data")

print("CONTROLS:")
print("\nMenu")
print("\nChange selection: Up and Down arrow keys")
print("Go back: Backspace")
print("Select: Enter")
print("Clear all data: Delete")
print("\nIn-Game")
print("\nType: A-Z on Keyboard")
print("Confirm Guess: Enter")
print("Exit / Save & Exit: Type 'exit'")

print("\n\n")
input("Press enter to confirm...")

# Initialize the main menu
main_menu = OpenMenu("main_menu")

# So that we can stay open, and to check at every moment
while True:
    from systems.screen_manager import currentlyOpen
    if currentlyOpen is None:
        continue

    # Get whether the user has used the keyboard
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        key = event.name

        if key == "up" or key == "down":
            currentlyOpen.change_selection(key)
        elif key == "enter":
            currentlyOpen.select()
        elif key == "backspace":
            currentlyOpen.back()
        elif key == "delete" and currentlyOpen:
            os.system('cls')
            while True:
                shouldDel = input(
                    "Are you sure you want to clear ALL data (highscores and save)? This cannot be undone! (y/n)")
                if shouldDel.lower().strip() == "y":
                    ClearAllData()
                    currentlyOpen.display()
                    break
                elif shouldDel.lower().strip() == "n":
                    currentlyOpen.display()
                    break
                else:
                    print("That is not an option!")
                    continue
