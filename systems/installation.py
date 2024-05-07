import os
import importlib.util
import sys

packages = [
    "keyboard",
    "playsound",
    "cryptography"
]

packages_with_instructions = [
    "keyboard",
    "playsound==1.2.2",
    "cryptography"
]


# In case the player doesn't have the correct packages installed, install it for them :)
def PromptInstallation():
    print("Uh oh! Looks like you don't have the required packages installed...")
    print("No worries though, we can do it automagically for you!")
    conf = input("Install packages (y/n)? ")
    while conf != 'y' and conf != 'n':
        print("That's not an option!")
        conf = input("Install packages (y/n)? ")
    if conf.lower() == 'y':
        print("Installing...")
        InstallPackages()
    elif conf.lower() == 'n':
        exit(1)


def InstallPackages():
    # Go through the packages list and run the pip install command
    # We can already assume they have python if they're at this point, since the compiled version won't have this error
    for i in packages_with_instructions:
        print(f"Installing {i}...")
        os.system(f"pip install {i}")
    print("Done! Please restart the app.")
    input()


def CheckForMissing():
    # Go through the packages list
    for package in packages:
        # If it's in the modules list, it's all good
        if package in sys.modules:
            continue
        # Previous check is not 100% reliable, so check if the module can be imported
        elif importlib.util.find_spec(package) is not None:
            continue
        # A package was not installed.
        else:
            return False
    return True
