import json
import os


def set_sound_enabled(val):
    data = ""
    if not os.path.exists("data/settings.json"):
        data = json.loads('{"sound_enabled": "True"}')
    else:
        with open("data/settings.json") as f:
            data = json.load(f)

    if data["sound_enabled"] == "False":
        data["sound_enabled"] = "True"
    else:
        data["sound_enabled"] = "False"

    with open("data/settings.json", 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def get_sound_enabled():
    data = ""
    if not os.path.exists("data/settings.json"):
        data = json.loads('{"sound_enabled": "True"}')
    else:
        with open("data/settings.json") as f:
            data = json.load(f)

    return data["sound_enabled"] == "True"
