# Different states for the hangman in-game based on the amount of chances the player has left

def getState(chances):
    match chances:
        case 10:
            return """







            """
        case 9:
            return """






======
        """
        case 8:
            return """

|
|
|
|
|
======
        """
        case 7:
            return """
*---*
|
|
|
|
|
======
            """
        case 6:
            return """
*---*
|   |
|
|
|
|
======
            """
        case 5:
            return """
*---*
|   |
|   o
|
|
|
======
            """
        case 4:
            return """
*---*
|   |
|   o
|   |
|
|
======
            """
        case 3:
            return """
*---*
|   |
|   o
|  /|
|
|
======
            """
        case 2:
            return """
*---*
|   |
|   o
|  /|\\
|
|
======
            """
        case 1:
            return """
*---*
|   |
|   o
|  /|\\
|  / 
|
======
            """
        case 0:
            return """
*---*
|   |
|   o
|  /|\\
|  / \\
|
======
            """
        case -1:
            return """
   \o/
    |
   / \\
            """