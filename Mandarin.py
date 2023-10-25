# This code contains logic related to the linguistic rules of telling time in Mandarin.

# Authors: Alice Vanni, Amber Lankheet, Brandi Hongell, Jingxuan Yue, Wenjun Meng

from helpers import get_current_time, play_audio
import pygame
import os

def speak_time_in_mandarin():
    '''
    This function takes no parameters and returns None
    This function retrieves the current time and plays
    the corresponding Mandarin Chinese time announcement based on the current time.
    The audio files should be located in the MandarinAudio folder and follow a specific naming convention.
    The function will automatically select the appropriate audio file for playback.
    '''
    # Get the current time
    hour, minute, ampm = get_current_time()
    audio_folder = "MandarinAudio"  # Folder containing audio files
    # Create a list of audio files to be played
    audio_files = []
    # Add "its_am" or "its_pm" audio
    audio_files.append(os.path.join(audio_folder, "its_am.wav" if ampm == "am" else "its_pm.wav"))
    if minute != '00':
        # Add hour audio
        audio_files.append(os.path.join(audio_folder, f"{hour}hour.wav"))
        audio_files.append(os.path.join(audio_folder, f"{minute}_m.wav"))
    else:
        # Add minute audio
        audio_files.append(os.path.join(audio_folder, f"{hour}hour.wav"))
        audio_files.append(os.path.join(audio_folder, "integer.wav"))
    # Play the list of audio files
    for audio_file in audio_files:
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
