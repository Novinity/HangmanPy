currentlyOpen = None


def OpenMenu(menuName):
    # Make the currentlyOpen actually useable
    global currentlyOpen

    if currentlyOpen is not None:
        currentlyOpen.close()

    # Importing here to avoid a circular import error
    from systems.menu_opener import Open

    currentlyOpen = Open(menuName)
    return currentlyOpen


def CloseMenu():
    global currentlyOpen

    if currentlyOpen is not None:
        currentlyOpen.close()
    currentlyOpen = None
