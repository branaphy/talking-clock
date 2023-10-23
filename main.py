# The starting point of execution for the Talking Clock. This contains the code pertaining the GUI.

# Authors: Alice Vanni, Amber Lankheet, Brandi Hongell, Jingxuan Yue, Wenjun Meng

import tkinter as tk
from English import speak_time_in_english
# from Mandarin import speak_time_in_mandarin
# from Italian import speak_time_in_italian
# from Dutch import speak_time_in_dutch
from Weather import get_weather
from helpers import get_current_time

root = tk.Tk()
root.title("Talking Clock")
root.geometry("400x300+300+120")


# define function to fetch current hour and minute, update display time, refresh after 1s
def time():
    hour, minute = get_current_time()
    time_label.config(text=f"{hour}:{minute}")
    time_label.after(1000, time)


def update_weather():
    city = "Leeuwarden"  # Replace with your city or desired location
    weather = get_weather(city, "584eb395bcf45a34c7ec7511b7d82c25")  # Replace with your API key
    weather_label.config(text=weather)
    root.after(600000, update_weather)  # Update every 10 minutes


# define the background colour
bg_color = 'black'

root.configure(bg=bg_color)

weather_label = tk.Label(root, font=('lucida console', 20, 'bold'), background=bg_color, foreground='white')
weather_label.pack(anchor='center', pady=20)
# label widget to display time with display properties
time_label = tk.Label(root, font=('lucida console', 40, 'bold'), background=bg_color, foreground='white')
time_label.pack(expand=True, anchor='center')

# language buttons that will speak the in the selected language when called
english_button = tk.Button(root, text='Speak Time (English)', command=speak_time_in_english)
english_button.pack()

# mandarin_button = tk.Button(root, text='Speak Time (Mandarin)', command=speak_time_in_mandarin)
# mandarin_button.pack()

# italian_button = tk.Button(root, text='Speak Time (Italian)', command=speak_time_in_italian)
# italian_button.pack()

# dutch_button = tk.Button(root, text='Speak Time (Dutch)', command=speak_time_in_dutch)
# dutch_button.pack()

# call the weather function to initialize the weather label
update_weather()
# call the time function to initialize the label
time()

# main event loop for GUI
root.mainloop()
