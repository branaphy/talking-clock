# This code contains logic related to the linguistic rules of telling time in Italian.

# Authors: Alice Vanni, Amber Lankheet, Brandi Hongell, Jingxuan Yue, Wenjun Meng

from helpers import get_current_time, play_audio

def speak_time_in_italian():
    '''
    The speak_time_in_italian() function takes no arguments.
    It selects the correct audio files to play according to the local time.

    Returns
    -------
    None.
    
    This function does not return a value; it plays audio to speak the time.

    '''
    hour, minute, ampm = get_current_time()
    
    #First, select the prosody for the minutes
    minute_prosody = "falling" if (0 <= int(minute) <= 27 or 58 <= int(minute) <= 59) else "rising"
    #Select the closest multiple of 5 for the minutes
    minute = round(int(minute) / 5) * 5
    #Select the audio file for minutes
    minute_audio = f"ItalianAudio/{minute}_{minute_prosody}_it.wav"
    
    #Select then the prosody for the hour
    hour_prosody = "falling" if minute_prosody == "rising" else "rising"
    #To select the hour, we simply select the current hour, except for
    #midnight and midday, in which we take into account if the time is am or pm.
    hour_audio = f"ItalianAudio/12{ampm.lower()}_{hour_prosody}_it.wav" if int(hour) == 12 else f"ItalianAudio/{hour}_{hour_prosody}_it.wav"
    
    #Select the linking word according to minutes and hour
    #The sequence in which hour and minute will be told is also selected here based on minute prosody
    if minute == 0:
        audio_sequence = (hour_audio.replace("rising", "falling"))
    elif minute_prosody == "rising":
        linking_audio = "ItalianAudio/a.wav" if int(hour) == 12 else "ItalianAudio/alle.wav"
        audio_sequence = (minute_audio, linking_audio, hour_audio)
    else:
        linking_audio = "ItalianAudio/and.wav"
        audio_sequence = (hour_audio, linking_audio, minute_audio)
    
    for audio in audio_sequence:
        play_audio(audio)
