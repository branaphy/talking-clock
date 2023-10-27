# This code contains logic related to the linguistic rules of telling time in Italian.

# Authors: Alice Vanni, Amber Lankheet, Brandi Hongell, Jingxuan Yue, Wenjun Meng

from gtts import gTTS
import tempfile
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
    #hour, minute, ampm = get_current_time()
    hour, minute, ampm = ['12', '24', 'pm']
    try:
        # Select the closest multiple of 5 for the minutes
        minute = format(round(int(minute) / 5) * 5, '02')
        # Select the prosody for the minutes
        minute_prosody = "falling" if (0 <= int(minute) <= 30) else "rising"
        # Select the audio file for minutes
        if int(minute) > 35:
            if len(str(60-int(minute))) == 1:
                minute = "0" + str(60-int(minute))
                minute_audio = f"ItalianAudio/{minute}_{minute_prosody}_it.wav"
            else:
                minute = (60-int(minute))
        minute_audio = f"ItalianAudio/{minute}_{minute_prosody}_it.wav"
    
        # Select then the prosody for the hour
        hour_prosody = "falling" if minute_prosody == "rising" else "rising"
        if hour_prosody == "falling":
            hour = int(hour) + 1
            if int(hour) == 13:
                hour = "01"
        hour = "0" + str(hour) if len(str(hour)) == 1 else hour
        # To select the hour, we simply select the current hour, except for
        # midnight and midday, in which we take into account if the time is am or pm.
        hour_audio = f"ItalianAudio/12{ampm.lower()}_{hour_prosody}_it.wav"\
            if int(hour) == 12 else f"ItalianAudio/{hour}_{hour_prosody}_it.wav"
    
        # Select the linking word according to minutes and hour
        # The sequence in which hour and minute will be told is also selected
        # here based on minute prosody
        if minute == "00":
            audio_sequence = hour_audio.replace("rising", "falling")
        elif minute_prosody == "rising":
            linking_audio = "ItalianAudio/a.wav" if int(hour) == 12\
                else "ItalianAudio/alle.wav"
            audio_sequence = (minute_audio, linking_audio, hour_audio)
        else:
            linking_audio = "ItalianAudio/and.wav"
            audio_sequence = (hour_audio, linking_audio, minute_audio)   
            
        if type(audio_sequence) == str:
            play_audio(audio_sequence)
        else:
            for audio in audio_sequence:
                play_audio(audio)
    
    except Exception as e:
        # Create a tts object in Italian to speak the error
        # It will say "I'm sorry, an error occured" in Italian
        ita_tts = gTTS(text="Mi dispiace, si è verificato un errore", lang="it", slow=False)
        # Save the temporary file to play it with pygame
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        file_path = temp_file.name
        temp_file.close()
        ita_tts.save(file_path)
        play_audio(file_path)
