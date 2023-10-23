# This code contains functions used by all languages.

# Also contains necessary code for certain audio functions.

# Authors: Alice Vanni, Amber Lankheet, Brandi Hongell, Jingxuan Yue, Wenjun Meng

from time import strftime
import pygame
import random


def get_current_time():
    hour = strftime('%I')  # Get hour in 01, 02, ... , 11, 12 format
    minute = strftime('%M')  # Get minute in 00, 01, ... , 59 format
    am_or_pm = strftime('%p')  # Get AM or PM
    return hour, minute, am_or_pm  # Return hour and minute as strings


def play_audio(file_path):
    pygame.mixer.init()  # Initialize mixer module in pygame
    pygame.mixer.music.load(file_path)  # Load audio file specified by file_path into the mixer
    pygame.mixer.music.play()  # Play the loaded audio file
    while pygame.mixer.music.get_busy():  # Loop to check if the mixer is playing audio
        pygame.time.Clock().tick(10)  # Program waits for 10ms before running the check again


def compute_gradient_color(start_color, end_color, ratio):
    # Extract RGB values from the colors
    s_red, s_green, s_blue = [int(start_color[i:i + 2], 16) for i in (1, 3, 5)]
    e_red, e_green, e_blue = [int(end_color[i:i + 2], 16) for i in (1, 3, 5)]

    # Calculate the intermediate RGB values
    red = int(s_red + (e_red - s_red) * ratio)
    green = int(s_green + (e_green - s_green) * ratio)
    blue = int(s_blue + (e_blue - s_blue) * ratio)

    # Convert RGB values back to hex format and return
    return f"#{red:02X}{green:02X}{blue:02X}"


def random_time():
    hour = random.randint(1, 12)  # Random hour between 1 and 12
    minute = random.randint(0, 59)  # Random minute between 0 and 59
    am_or_pm = random.choice(["AM", "PM"])  # Randomly choose "AM" or "PM"
    return f"{hour:02}:{minute:02} {am_or_pm}"  # Return time in the format "HH:MM AM/PM"
