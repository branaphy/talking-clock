# This code contains logic related to the linguistic rules of telling time in Dutch.

# Authors: Alice Vanni, Amber Lankheet, Brandi Hongell, Jingxuan Yue, Wenjun Meng

from gtts import gTTS
import tempfile
from helpers import get_current_time, play_audio


def speak_time_in_latin():
    """
    The speak_time_in_latin() function takes no arguments.
    It generates a string that express the current time according 
    to the local time.
    If an error occurs, it will say so.

    Returns
    -------
    None.
    
    This function does not return a value; it plays audio to speak the time.

    """
    hour, minute, ampm = get_current_time()

    try:
        # Define Latin numbers to express hours
        latin_numbers = ["unus", "duo", "tres", "quattuor", "quinque", "sex",
                         "septem", "octo", "novem", "decem", "undecim", "duodecim",
                         "tredecim", "quattuordecim", "quindecim", "sedecim",
                         "septendecim", "octodecim", "novemdecim", "viginti",
                         "viginti unus", "viginti duo", "viginti tres",
                         "viginti quattuor", "viginti quinque", "viginti sex",
                         "viginti septem", "viginti octo", "viginti novem", "triginta",
                         "triginta unus", "triginta duo", "triginta tres", "triginta quattuor",
                         "triginta quinque", "triginta sex", "triginta septem", "triginta octo",
                         "triginta novem", "quadraginta", "quadraginta unus", "quadraginta duo",
                         "quadraginta tres", "quadraginta quattuor", "quadraginta quinque",
                         "quadraginta sex", "quadraginta septem", "quadraginta octo",
                         "quadraginta novem", "quinquaginta", "quinquaginta unus",
                         "quinquaginta duo", "quinquaginta tres", "quinquaginta quattuor",
                         "quinquaginta quinque", "quinquaginta sex", "quinquaginta septem",
                         "quinquaginta octo", "quinquaginta novem"]
        # Convert the current time to Latin and select the current time
        latin_hour = latin_numbers[int(hour) - 1]
        if minute == 0:
            latin_time = f"Hora est {latin_hour}."
        else:
            latin_minute = latin_numbers[int(minute) - 1]
            latin_time = f"Hora est {latin_hour} et {latin_minute} minuta."

        # Create a tts object in Latin
        latin_tts = gTTS(text=latin_time, lang='la')
        # Save the temporary file to play it with pygame
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        file_path = temp_file.name
        temp_file.close()
        latin_tts.save(file_path)

        play_audio(file_path)
    except Exception as latin_error:
        print(f"An error occurred in speak_time_in_latin: {latin_error}")
        # It will say "I'm sorry, an error occured" in Latin
        latin_tts = gTTS(text="Doleo, sed error occurrit", lang='la')
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        file_path = temp_file.name
        temp_file.close()
        latin_tts.save(file_path)

        play_audio(file_path)
