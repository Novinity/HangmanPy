import os
from cryptography.fernet import Fernet
from time import sleep
import json


# For checking if there is an existing save
def SaveExists():
    if os.path.exists("data/save.dat"):
        return True
    return False


def SaveData(info):
    try:
        # Remove all the existing files
        if os.path.exists("data/filekey.key"):
            os.remove("data/filekey.key")
        if os.path.exists("data/save.dat"):
            os.remove("data/save.dat")
        sleep(0.1)

        # Generating and saving the encryption key
        key = Fernet.generate_key()
        with open('data/filekey.key', 'wb') as filekey:
            filekey.write(key)

        # Info should contain the word, current amount of chances, mistakes, and found letters
        with open("data/save.dat", 'wb') as f:
            # Creating the string for writing
            writable = json.dumps(info)

            encryptable = bytes(writable, 'utf-8')

            # Encrypting the file contents so that the user can't just save and win
            fernet = Fernet(key)
            encrypted = fernet.encrypt(encryptable)
            # Write the encrypted version to the file
            f.write(encrypted)

        return True
    except:
        return False


def LoadData():
    # Initialize data variable
    data = {}
    # If the save file or decryption key don't exist, return the empty data variable
    # since we can't do anything without both.
    if not os.path.exists("data/save.dat") or not os.path.exists("data/filekey.key"):
        return data

    # Initialize key variable
    key = ""
    # Read the key
    with open('data/filekey.key', 'rb') as filekey:
        key = filekey.read()
    # Initialize fernet with the key as input
    fernet = Fernet(key)

    with open("data/save.dat", 'rb') as f:
        # Decrypt the file using the fernet and key
        decrypted = fernet.decrypt(f.read()).decode('utf-8')
        print(decrypted)
        data = json.loads(decrypted)
    return data


# Delete existing save if it exists
def DeleteSaveData():
    if not os.path.exists("data/save.dat"):
        return
    os.remove("data/save.dat")


def SaveHighScore(name, score, difficulty):
    # Try Except so we don't stop if saving doesn't work, since it's not as important as everything else
    # Unfortunately does make it harder to debug, but oh well.
    try:
        # Loading current data so we can keep it
        data = LoadHighScores()
        with open("data/highscores.json", 'w') as f:
            # If it's already in there, check if they've just gotten a higher score
            if not difficulty in data:
                data[difficulty] = {}
            if name in data[difficulty]:
                if int(data[difficulty][name]) < int(score):
                    data[difficulty][name] = score
            else:
                data[difficulty][name] = score

            # Write json to file
            json.dump(data, f, sort_keys=True)
        return True
    except:
        return False


def LoadHighScores():
    # Initialize data variable
    data = {}
    # If we don't have a highscores file or the file is empty, return the empty data variable
    if not os.path.exists("data/highscores.json") or os.stat("data/highscores.json").st_size == 0:
        return data
    # Load the json from the file into the data variable
    with open("data/highscores.json", 'r') as f:
        data = json.load(f)
    # Return the data as a reversed dictionary so that it can be used in descending order
    return data


def ClearAllData():
    # Delete all files
    if os.path.exists("data/highscores.json"):
        os.remove("data/highscores.json")
    if os.path.exists("data/save.dat"):
        os.remove("data/save.dat")
    if os.path.exists("data/filekey.key"):
        os.remove("data/filekey.key")
