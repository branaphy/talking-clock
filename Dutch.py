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


    # create an empty list
    audio_files = []

    # First, choose the right folder
    audio_folder = "DutchAudio"

    # Starting the sentence with 'it is'
    audio_files.append(os.path.join(audio_folder, "it_is_nl.wav"))

    # Then looking at the minutes and choosing the right file.
    # Creating the clcok in quarters
    # Adding +1 because the telling time is plus the next hour, also two digits are required in the audio file
    # when the hour is '00', the file with '12' needs to be used, but in the recording folder there is no file.
    if minute != '00' and minute != '60':
        print("first condition met")
        if 13<= int(minute) <=17:
            audio_files.append(os.path.join(audio_folder, "quarter_past_nl.wav"))
            if int(hour) == 00:
                audio_files.append(os.path.join(audio_folder, "12_falling_nl.wav"))
            else:
                audio_files.append(os.path.join(audio_folder, f"{hour}_falling_nl.wav"))
        elif 28 <= int(minute) <= 30:
            audio_files.append(os.path.join(audio_folder, "half_nl.wav"))
            audio_files.append(os.path.join(audio_folder, f"{int(hour) + 1:02d}_falling_nl.wav"))
        elif 43 <= int(minute) <= 47:
            audio_files.append(os.path.join(audio_folder, "quarter_to_nl.wav"))
            audio_files.append(os.path.join(audio_folder, f"{int(hour) + 1:02d}_falling_nl.wav"))

        # Between the 20 and 30 minutes, we substracted 30 minutes by the minutes on the clock
        elif 20 <= int(minute) < 30:
            audio_files.append(os.path.join(audio_folder, f"{30-int(minute):02d}_rising_nl.wav"))
            audio_files.append(os.path.join(audio_folder, "to_nl.wav"))
            audio_files.append(os.path.join(audio_folder, "half_nl.wav"))
            audio_files.append(os.path.join(audio_folder, f"{int(hour) + 1:02d}_falling_nl.wav"))
        # Here the minutes are substracted by 30
        elif 30 < int(minute) <= 40:
            audio_files.append(os.path.join(audio_folder, f"{int(minute)-30:02d}_rising_nl.wav"))
            audio_files.append(os.path.join(audio_folder, "past_nl.wav"))
            audio_files.append(os.path.join(audio_folder, "half_nl.wav"))
            audio_files.append(os.path.join(audio_folder, f"{int(hour) + 1:02d}_falling_nl.wav"))

        # Between 50 and 59, 60 is substracted by the minutes on the clock
        elif 50 <= int(minute) <= 59:
            audio_files.append(os.path.join(audio_folder, f"{60-int(minute) :02d}_rising_nl.wav"))
            audio_files.append(os.path.join(audio_folder, "to_nl.wav"))
            audio_files.append(os.path.join(audio_folder, f"{int(hour) + 1:02d}_falling_nl.wav"))

        # Between 1 and 10, 0 is added by the minutes on the clock
        # When the hour is 00, it makes sure that the '12' file is used
        elif 1 <= int(minute) <= 10:
            audio_files.append(os.path.join(audio_folder, f"{0 + int(minute) :02d}_rising_nl.wav"))
            audio_files.append(os.path.join(audio_folder, "past_nl.wav"))
            if int(hour) == 00:
                audio_files.append(os.path.join(audio_folder, "12_falling_nl.wav"))
            else:
                audio_files.append(os.path.join(audio_folder, f"{hour}_falling_nl.wav"))
        # minutes 11 and 12 are rounded to 10
        elif 11 <= int(minute) <= 12:
            audio_files.append(os.path.join(audio_folder, "10_rising_nl.wav"))
            audio_files.append(os.path.join(audio_folder, "past_nl.wav"))
            if int(hour) == 00:
                audio_files.append(os.path.join(audio_folder, "12_falling_nl.wav"))
            else:
                audio_files.append(os.path.join(audio_folder, f"{hour}_falling_nl.wav"))
        # minutes 18 and 19 are rounded to 20 past
        # here +1 is needed because the next hour is used
        elif  18 <= int(minute) <= 19:
            audio_files.append(os.path.join(audio_folder, "10_rising_nl.wav"))
            audio_files.append(os.path.join(audio_folder, "to_nl.wav"))
            audio_files.append(os.path.join(audio_folder, "half_nl.wav"))
            audio_files.append(os.path.join(audio_folder, f"{int(hour) + 1:02d}_falling_nl.wav"))
        # minutes 41 and 42 are rounded to 40 past
        # here +1 is needed because the next hour is used
        elif 41 <= int(minute) <= 42:
            audio_files.append(os.path.join(audio_folder, "10_rising_nl.wav"))
            audio_files.append(os.path.join(audio_folder, "past_nl.wav"))
            audio_files.append(os.path.join(audio_folder, "half_nl.wav"))
            audio_files.append(os.path.join(audio_folder, f"{int(hour) + 1:02d}_falling_nl.wav"))
        # minutes 48 and 49 are rounded to 50 past
        # here +1 is needed because the next hour is used
        elif 48 <= int(minute) <= 49:
            audio_files.append(os.path.join(audio_folder, "10_rising_nl.wav"))
            audio_files.append(os.path.join(audio_folder, "to_nl.wav"))
            audio_files.append(os.path.join(audio_folder, f"{int(hour) + 1:02d}_falling_nl.wav"))
            
    # The round hour is used here followed by the Dutch word for oclock
    else:
        hour = int(hour) + 1 if int(minute) == 60 else hour
        audio_files.append(os.path.join(audio_folder, f"{hour}_rising_nl.wav"))
        audio_files.append(os.path.join(audio_folder, "oclock_nl.wav"))

    #play audio file
    # To do this, you can just use the play_audio() funtion Brandi wrote in the helpers file, it takes the audio_file as the argument (- Alice)
    for audio_file in audio_files:
        play_audio(audio_file)





