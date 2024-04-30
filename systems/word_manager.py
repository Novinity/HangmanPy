import random

easyWordPossibilities = [
    "CAT",
    "DOG",
    "SUN",
    "CUP",
    "HAT",
    "PEN",
    "BED",
    "BOOK",
    "BALL",
    "TREE",
    "FISH",
    "MOON",
    "DUCK",
    "RAIN",
    "CAKE",
    "BIRD",
    "FROG",
    "STAR",
    "MILK",
    "RING"
]

normalWordPossibilities = [
    "APPLE",
    "BANANA",
    "GUITAR",
    "TABLE",
    "HOUSE",
    "CLOCK",
    "PIANO",
    "JACKET",
    "ORANGE",
    "WINDOW",
    "FLOWER",
    "BOTTLE",
    "PIZZA",
    "SCHOOL",
    "TIGER",
    "DRAGON",
    "MONKEY",
    "PIRATE",
    "DOLPHIN",
    "ELEPHANT"
]

hardWordPossibilities = [
    "ELEPHANT",
    "SYMPHONY",
    "CHOCOLATE",
    "UNIVERSE",
    "KALEIDOSCOPE",
    "PARADOX",
    "SERENDIPITY",
    "CARNIVORE",
    "AMBIVALENT",
    "PHILOSOPHY",
    "EXTRATERRESTRIAL",
    "PSYCHOSOMATIC",
    "REMINISCENCE",
    "ACCOMMODATE",
    "DIFFICULTY",
    "MAGNIFICENT",
    "HYPOTHESIS",
    "TECHNOLOGY",
    "PERSEVERANCE",
    "QUINTESSENTIAL"
]

nightmareWordPossibilities = [
    "PSEUDOPSEUDOHYPOPARATHYROIDISM",
    "HIPPOPOTOMONSTROSESQUIPPEDALIOPHOBIA",
    "ANTIDISESTABLISHMENTARIANISM",
    "SUPERCALIFRAGILISTICEXPIALIDOCIOUS",
    "FLOCCINAUCINIHILIPILIFICATION",
    "ECCLESIASTICOPHOBIA",
    "PNEUMONOULTRAMICROSCOPICSILICOVOLCANOCONIOSIS",
    "XYLOPYROGRAPHY",
    "QUODLIBETARIAN",
    "JACKDAW",
    "PENNYWISE",
    "CRYPTOGRAPHY",
    "XEROPHYTE",
    "RHYTHM",
    "ZWIEBACK",
    "JUXTAPOSITION",
    "ZYGOTE",
    "EXTRAPOLATION",
    "XENOPHOBIA",
    "MISCELLANEOUS"
]


def getRandomWord(difficulty):
    # Check the difficulty, and return a random word from the according list
    match difficulty:
        case "easy":
            return easyWordPossibilities[random.randrange(0, len(easyWordPossibilities))]
        case "normal":
            return normalWordPossibilities[random.randrange(0, len(normalWordPossibilities))]
        case "hard":
            return hardWordPossibilities[random.randrange(0, len(hardWordPossibilities))]
        case "nightmare":
            return nightmareWordPossibilities[random.randrange(0, len(nightmareWordPossibilities))]


# Check if the player has gotten a correct letter
def checkLetterMatch(letter, word):
    return letter in word


# Get the new word display
def getNewWordMatch(letter, word, blanks):
    final = ""
    # Splitting to remove spaces
    blanks = blanks.split(' ')
    for i in range(len(word)):
        if word[i] == letter:
            for j in range(len(blanks)):
                # If we're at the same point in the word, add the letter, else just use the original one
                if j == i:
                    final += word[i] + " "
        else:
            final += blanks[i] + " "

    return final.strip()



def getBlanksFromFoundLetters(word, found_letters):
    blanks = ""
    for i in range(len(word)):
        if word[i] in found_letters:
            blanks += word[i] + " "
        else:
            blanks += '_ '
    return blanks


def getFoundLettersFromBlanks(blanks):
    split = blanks.split(' ')
    finalFound = []

    for i in split:
        if i != '_':
            finalFound.append(i)

    return finalFound


# Check if the player has won
def checkWin(blanks, word):
    blanks = blanks.split(' ')
    # Go through and check if each letter is right, if not, they haven't won
    for i in range(len(blanks)):
        if blanks[i] != word[i]:
            return False
    return True
