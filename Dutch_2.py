# This code contains logic related to the linguistic rules of telling time in Dutch.
import os

# import pygame

from helpers import get_current_time, play_audio


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

    hour, minute, am_or_pm = get_current_time()
    #hour, minute, am_or_pm = ["11","59","pm"]

    #create an empty list
    audio_files = []

    #First, choose the right folder
    audio_folder = "DutchAudio"

    #Beginning of the sentence, it is...
    audio_files.append(os.path.join(audio_folder, "it_is_nl.wav"))

    #then looking at the minutes and choosing the right file.
    # Adding this to round the minute to the closest multiple of 5, then
    # you can also simplify the if statements if you want (- Alice)
    minute = round(int(minute) / 5) * 5
    minute = str(minute)
    
    if minute != '00' and minute != '60':
        print("first condition met")
        if int(minute) == 15:
            audio_files.append(os.path.join(audio_folder, "quarter_past_nl.wav"))
            audio_files.append(os.path.join(audio_folder, f"{hour}_falling_nl.wav"))
        elif int(minute) == 30:
            audio_files.append(os.path.join(audio_folder, "half_nl.wav"))
            #adding +1 because the telling time is plus the next hour, also two digits are required in the audio file
            audio_files.append(os.path.join(audio_folder, f"{int(hour) + 1:02d}_falling_nl.wav"))
        elif int(minute) == 45:
            audio_files.append(os.path.join(audio_folder, "quarter_to_nl.wav"))
            audio_files.append(os.path.join(audio_folder, f"{int(hour) + 1:02d}_falling_nl.wav"))

        #between the 20 and 30 minutes, we substracted 30 minutes by the minutes on the clock
        elif 18 <= int(minute) < 30:
            audio_files.append(os.path.join(audio_folder, f"{30-int(minute):02d}_rising_nl.wav"))
            audio_files.append(os.path.join(audio_folder, "to_nl.wav"))
            audio_files.append(os.path.join(audio_folder, "half_nl.wav"))
            audio_files.append(os.path.join(audio_folder, f"{int(hour) + 1:02d}_falling_nl.wav"))

        elif 30 < int(minute) <= 40:
            audio_files.append(os.path.join(audio_folder, f"{int(minute)-30:02d}_rising_nl.wav"))
            audio_files.append(os.path.join(audio_folder, "past_nl.wav"))
            audio_files.append(os.path.join(audio_folder, "half_nl.wav"))
            audio_files.append(os.path.join(audio_folder, f"{int(hour) + 1:02d}_falling_nl.wav"))

        elif 50 <= int(minute) <= 55:
            audio_files.append(os.path.join(audio_folder, f"{60-int(minute) :02d}_rising_nl.wav"))
            audio_files.append(os.path.join(audio_folder, "to_nl.wav"))
            audio_files.append(os.path.join(audio_folder, f"{int(hour) + 1:02d}_falling_nl.wav"))

        elif 1 <= int(minute) <= 10:
            audio_files.append(os.path.join(audio_folder, f"{0 + int(minute) :02d}_rising_nl.wav"))
            audio_files.append(os.path.join(audio_folder, "past_nl.wav"))
            audio_files.append(os.path.join(audio_folder, f"{hour}_falling_nl.wav"))


        #elif m

    else:
        hour = int(hour) + 1 if int(minute) == 60 else hour
        audio_files.append(os.path.join(audio_folder, f"{hour}_rising_nl.wav"))
        audio_files.append(os.path.join(audio_folder, "oclock_nl.wav"))



    #different stages of the day


    #play audio file
    # To do this, you can just use the play_audio() funtion Brandi wrote in the helpers file, it takes the audio_file as the argument (- Alice)
    for audio_file in audio_files:
        play_audio(audio_file)
        # pygame.mixer.init()
        # pygame.mixer.music.load(audio_file)
        # pygame.mixer.music.play()
        # while pygame.mixer.music.get_busy():
        #     pygame.time.Clock().tick(10)


# if __name__ == '__main__':
#    speak_time_in_dutch()



