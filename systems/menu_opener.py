# This script exists purely to avoid circular import errors

from screens.main_menu_screen import MainMenuScreen
from screens.difficulties_screen import DifficultiesScreen
from screens.scores_screen import ScoresScreen
from screens.options_screen import OptionsScreen

def Open(menuName):
    menu = None
    # Go through possible menu options
    match menuName:
        case "main_menu":
            menu = MainMenuScreen()
        case "difficulties":
            menu = DifficultiesScreen()
        case "options":
            menu = OptionsScreen()
        case "scores":
            menu = ScoresScreen()

    # If it exists, display it
    if menu:
        menu.display()
        return menu