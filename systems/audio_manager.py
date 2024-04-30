import os
import playsound
import asyncio

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


async def play_music(songName):
    try:
        # Go through all songs in folder
        for song in os.listdir(music_dir):
            # Decode the file name so we can check it properly
            filename = os.fsdecode(song)
            if filename.startswith(songName):
                # Play the song
                playsound.playsound(os.fsdecode(music_dir) + '/' + filename)
    except:
        # Song failed to play
        pass


def playSound(soundName):
    # Run it asynchronously as to not pause any processes
    asyncio.run(play_sound(soundName))


def playSong(soundName):
    # Run it asynchronously as to not pause any processes
    asyncio.run(play_music(soundName))
