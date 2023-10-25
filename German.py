# This code contains logic related to the linguistic rules of telling time in Dutch.

# Authors: Alice Vanni, Amber Lankheet, Brandi Hongell, Jingxuan Yue, Wenjun Meng

from helpers import get_current_time, play_audio
from gtts import gTTS
import tempfile

def speak_time_in_german():
    '''
    The speak_time_in_german() function takes no arguments.
    It generates a string that express the current time according to the local time.

    Returns
    -------
    None.
    
    This function does not return a value; it plays audio to speak the time.

    '''
    hour, minute, ampm = get_current_time()
    
    #Take out the 0 ("null") from the sentence
    hour = hour[1] if hour[0] == "0" else hour
    minute = minute[1] if minute[0] == "0" else minute
        
    #Select the hour
    if minute == 0:
        german_time = f"Es ist {hour} Uhr"
    elif minute == 30:
        german_time = f"Es ist halb {(hour + 1)}"
    else:
        german_time = f"Es ist {hour} Uhr {minute}"
    
    # Create a tts object in German
    german_tts = gTTS(text=german_time, lang='de')
    # Save the temporary file to play it with pydub
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    file_path = temp_file.name
    temp_file.close()
    german_tts.save(file_path)
    
    play_audio(file_path)
