import json
import os


def set_sound_enabled(val):
    # Initialize data variable
    data = {}
    # If the settings file exists, load it's JSON contents into the data variable
    # If not, put some default data into the data variable
    if not os.path.exists("data/settings.json"):
        data = json.loads('{"sound_enabled": "True"}')
    else:
        with open("data/settings.json") as f:
            data = json.load(f)

    # If False, set to True, else set to False
    if data["sound_enabled"] == "False":
        data["sound_enabled"] = "True"
    else:
        data["sound_enabled"] = "False"

    # Write the new data into the settings file as json
    with open("data/settings.json", 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_sound_enabled():
    # Initialize data variable
    data = {}
    # If the settings file exists, load it's JSON contents into the data variable
    # If not, put some default data into the data variable
    if not os.path.exists("data/settings.json"):
        data = json.loads('{"sound_enabled": "True"}')
    else:
        with open("data/settings.json") as f:
            data = json.load(f)

    # Return whether sound enabled is set to true.
    return data["sound_enabled"] == "True"
