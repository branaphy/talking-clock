# This code contains logic related to the linguistic rules of telling time in American English.

# Authors: Alice Vanni, Amber Lankheet, Brandi Hongell, Jingxuan Yue, Wenjun Meng
import os
from helpers import get_current_time, play_audio


def speak_time_in_english():
    """
       This function takes no parameters and returns None
       This function retrieves the current time and plays
       the corresponding American English time announcement based on the current time.
       The audio files should be located in the EnglishAudio folder and follow a specific naming convention.
       The function will automatically select the appropriate audio file for playback.
    """
    # Get the current time
    hour, minute, ampm = get_current_time()

    audio_folder = "EnglishAudio"  # Folder containing audio files
    # Create a list of audio files to be played
    audio_files = []

    audio_files.append(os.path.join(audio_folder, f"hour_{hour}.wav"))
    audio_files.append(os.path.join(audio_folder, f"minute_{minute}.wav"))

    # Add am pm audio
    audio_files.append(os.path.join(audio_folder, "am.wav" if ampm == "AM" else "pm.wav"))
    # Play the list of audio files
    for audio_file in audio_files:
        play_audio(audio_file)
