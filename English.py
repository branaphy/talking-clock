# This code contains logic related to the linguistic rules of telling time in American English.

# Authors: Alice Vanni, Amber Lankheet, Brandi Hongell, Jingxuan Yue, Wenjun Meng

from helpers import get_current_time, play_audio


def speak_time_in_english():
    hour, minute = get_current_time()

    hour_audio_path = f"EnglishAudio/hour_{int(hour)}.wav"
    minute_audio_path = f"EnglishAudio/minute_{minute}.wav"

    play_audio(hour_audio_path)
    play_audio(minute_audio_path)
