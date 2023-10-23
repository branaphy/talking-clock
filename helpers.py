# This code contains functions used by all languages.

# Also contains necessary code for certain audio functions.

# Authors: Alice Vanni, Amber Lankheet, Brandi Hongell, Jingxuan Yue, Wenjun Meng

from time import strftime
import pygame

def get_current_time():
    hour = strftime('%I')  # Get hour in 01, 02, ... , 11, 12 format
    minute = strftime('%M')  # Get minute in 00, 01, ... , 59 format
    return hour, minute  # Return hour and minute as strings

def play_audio(file_path):
    pygame.mixer.init()  # Initialize mixer module in pygame
    pygame.mixer.music.load(file_path)  # Load audio file specified by file_path into the mixer
    pygame.mixer.music.play()  # Play the loaded audio file
    while pygame.mixer.music.get_busy():  # Loop to check if the mixer is playing audio
        pygame.time.Clock().tick(10)  # Program waits for 10ms before running the check again
