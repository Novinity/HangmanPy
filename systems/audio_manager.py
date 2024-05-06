import playsound
import asyncio
from systems.settings import *

sound_dir = os.fsencode("resources/sound")
music_dir = os.fsencode("resources/music")


async def play_sound(soundName):
    try:
        # Go through all sounds in folder
        for sound in os.listdir(sound_dir):
            # Decode the file name so we can check it properly
            filename = os.fsdecode(sound)
            if filename.startswith(soundName):
                # Play the sound
                playsound.playsound(os.fsdecode(sound_dir) + '/' + filename)
    except:
        # Sound failed to play
        pass


def playSound(soundName):
    if not get_sound_enabled():
        return
    # Run it asynchronously as to not pause any processes
    asyncio.run(play_sound(soundName))
