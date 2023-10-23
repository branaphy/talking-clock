# This code contains logic related to the linguistic rules of telling time in Italian.

# Authors: Alice Vanni, Amber Lankheet, Brandi Hongell, Jingxuan Yue, Wenjun Meng

#This code has the objective to select the correct audio file
#to express the hour and minutes.

import time
from helpers import get_current_time, play_audio

#Function to get the current time in the format HH:MM:SS.

def get_time():
    time_str = time.strftime("%I:%M:%p")
    time_var = time_str.split(":")
    return time_var

#Function to retrieve the correct audio file for the minutes
def get_mins_file():
    if 3 <= int(get_time()[1][1]) <= 7:
        if get_time()[1][0] == "1":
            mins_file = "quarter_past_it.wav"
        elif get_time()[1][0] == "4":
            mins_file = "quarter_to_it.wav"
        elif get_time()[1][0] == "5":
            mins_file = "05_rising_it.wav"
        else:
            mins_file = get_time()[1][0] + "5_falling_it.wav"
    elif int(get_time()[1][1]) >= 8 or int(get_time()[1][1]) <= 2:
        if get_time()[1][0] == "2" or get_time()[1][0] == "3":
            mins_file = "half_past_it.wav"
        if get_time()[1][0] == "4" or get_time()[1][0] == "5":
            mins_file = "10_rising_it.wav"
        else:
            mins_file = get_time()[1][0] + "0_falling_it.wav"
    else:
        mins_file = "Unknown"
    return mins_file
            
        

#Function to retrieve the correct file with the hour
#if the minutes are >45 --> hour+1
def get_hour_file():
    if int(get_time()[1]) >= 45:
        hour = int(get_time()[0]) + 1
        hour = 1 if hour == 13 else hour
        hour = "midnight" if hour == 0 else hour
        hour = "midday" if hour == 12 else hour
        hour_file = str(hour) + "_falling_it.wav"
    else:
        hour = get_time()[0]
        hour = "midnight" if hour == 0 else hour
        hour = "midday" if hour == 12 else hour
        hour_file = hour + "_rising_it.wav"
    return hour_file

#This code defines the fucntion to tell the time in Italian

def ita_speak_time():
    hour_file = get_hour_file()
    mins_file = get_mins_file()
    if "rising" in hour_file:
        audio_names = (hour_file, "and.wav", mins_file)
    elif hour_file == "midday.wav" or hour_file == "midnight.wav":
        audio_names = (mins_file, "a.wav", hour_file)
    else:
        audio_names = (mins_file, "alle.wav", hour_file)
    return for audio in audio_names:
        play_audio(audio)
