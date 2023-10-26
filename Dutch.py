# This code contains logic related to the linguistic rules of telling time in Dutch.

# This code contains logic related to the linguistic rules of telling time in Dutch.
import os

import pygame

from helpers import get_current_time


# Authors: Alice Vanni, Amber Lankheet, Brandi Hongell, Jingxuan Yue, Wenjun Meng

def speak_time_in_dutch():
    '''
    The speak_time_in_dutch() function takes no arguments.
    It selects the correct audio files from the DutchAudio folder to play the time that appears in the GUI.
    Returns
    -----
    None.

    This function does not take a value; it plays the audio to speak the time
    '''

    #hour, minute, am_or_pm = get_current_time()
    hour, minute, am_or_pm = ["06","20","pm"]
    #create an empty list
    audio_files = []

    #First, choose the right folder
    audio_folder = "DutchAudio"

    #Beginning of the sentence, it is...
    audio_files.append(os.path.join(audio_folder, "it_is_nl.wav"))

    #
    if minute != '00':
        if minute == '15':
            audio_files.append(os.path.join(audio_folder, "quarter_past_nl.wav"))
            audio_files.append(os.path.join(audio_folder, f"{hour}_falling_nl.wav"))
        elif minute == '30':
            audio_files.append(os.path.join(audio_folder, "half_nl.wav"))
            #adding +1 because the telling time is plus the next our.
            audio_files.append(os.path.join(audio_folder, f"{int(hour) + 1:02d}_falling_nl.wav"))
        elif minute == '45':
            audio_files.append(os.path.join(audio_folder, "quarter_to_nl.wav"))
            audio_files.append(os.path.join(audio_folder, f"{int(hour) + 1:02d}_falling_nl.wav"))
        elif 20 <= int(minute) < 30:
            audio_files.append(os.path.join(audio_folder, f"{30-int(minute)}_rising_nl.wav"))
            audio_files.append(os.path.join(audio_folder, "to_nl.wav"))
            audio_files.append(os.path.join(audio_folder, "half_nl.wav"))
            audio_files.append(os.path.join(audio_folder, f"{int(hour) + 1:02d}_falling_nl.wav"))

        elif 30 < int(minute) <= 40:
            audio_files.append(os.path.join(audio_folder, f"{30+int(minute)}_rising_nl.wav"))
            audio_files.append(os.path.join(audio_folder, "past_nl.wav"))
            audio_files.append(os.path.join(audio_folder, "half_nl.wav"))
            audio_files.append(os.path.join(audio_folder, f"{int(hour) + 1:02d}_falling_nl.wav"))
        #elif


        #elif m

    else:
        audio_files.append(os.path.join(audio_folder, f"{hour}_rising_nl.wav"))
        audio_files.append(os.path.join(audio_folder, "oclock_nl.wav"))



    #different stages of the day


    #play audio file
    for audio_file in audio_files:
        pygame.mixer.init()
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


#if __name__ == '__main__':
 #   speak_time_in_dutch()







# Authors: Alice Vanni, Amber Lankheet, Brandi Hongell, Jingxuan Yue, Wenjun Meng
