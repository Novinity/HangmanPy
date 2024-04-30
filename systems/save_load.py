import os
import csv
from cryptography.fernet import Fernet
from time import sleep


# For checking if there is an existing save
def SaveExists():
    if os.path.exists("data/save.dat"):
        return True
    return False


def SaveData(info):
    try:
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
            writable = info['word'] + '\n' + str(info['chances']) + '\n' + ','.join(info["mistakes"]) + '\n' + ','.join(
                info["found"])

            encryptable = bytes(writable, 'utf-8')

            # Encrypting the file contents
            fernet = Fernet(key)
            encrypted = fernet.encrypt(encryptable)
            # Write the encrypted version to the file
            f.write(encrypted)

        return True
    except:
        return False


def LoadData():
    data = {}
    if not os.path.exists("data/save.dat") or not os.path.exists("data/filekey.key"):
        return data

    key = ""
    with open('data/filekey.key', 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)

    with open("data/save.dat", 'rb') as f:
        decrypted = fernet.decrypt(f.read()).decode('utf-8')
        index = 0
        for line in decrypted.split('\n'):
            if line.strip() == '':
                continue
            if index == 0:
                data["word"] = line.strip()
            elif index == 1:
                data["chances"] = int(line.strip())
            elif index == 2:
                data["mistakes"] = line.strip().split(',')
            elif index == 3:
                data["found"] = line.strip().split(',')
            index += 1
    return data


def DeleteSaveData():
    if not os.path.exists("data/save.dat"):
        return
    os.remove("data/save.dat")


def SaveHighScore(name, score):
    # Try Except so we don't stop if saving doesn't work, since it's not as important as everything else
    # Unfortunately does make it harder to debug, but oh well.
    try:
        # Loading current data so we can keep it
        data = LoadHighScores()
        with open("data/highscores.csv", 'w') as f:
            # If it's already in there, check if they've just gotten a higher score
            if name in data:
                if int(data[name]) < int(score):
                    data[name] = score
            else:
                data[name] = score
            # Create the writer
            w = csv.DictWriter(f, ['name', 'score'])

            # Sorted so that we can display the correct placements
            sortedData = sorted(data)
            for i in sortedData:
                w.writerow({'name': i, 'score': data[i]})
        return True
    except:
        return False


def LoadHighScores():
    data = {}
    if not os.path.exists("data/highscores.csv"):
        return data
    with open("data/highscores.csv", newline='') as f:
        w = csv.DictReader(f, fieldnames=['name', 'score'])
        # Go through each row and add it to the data
        for row in w:
            data[row['name']] = int(row['score'])
    return data


def ClearAllData():
    if os.path.exists("data/highscores.csv"):
        os.remove("data/highscores.csv")
    if os.path.exists("data/save.dat"):
        os.remove("data/save.dat")
    if os.path.exists("data/filekey.key"):
        os.remove("data/filekey.key")