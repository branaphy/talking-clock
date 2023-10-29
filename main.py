# Authors: Alice Vanni, Amber Lankheet, Brandi Hongell, Jingxuan Yue, Wenjun Meng

import tkinter as tk
from tkinter import messagebox, DISABLED, NORMAL

from English import speak_time_in_english
from Mandarin import speak_time_in_mandarin
from Italian import speak_time_in_italian
from German import speak_time_in_german
from Latin import speak_time_in_latin
from Dutch import speak_time_in_dutch
from Weather import get_weather
from helpers import get_current_time, compute_gradient_color, random_time

hour_colors = ['#FFFFCC', '#FFCC99', '#FFCCCC', '#FF99CC', '#FFCCFF', '#CC99FF', '#CCCCFF', '#99CCFF', '#CCFFFF',
               '#99FFCC', '#CCFFCC', '#CCFF99']

root = tk.Tk()
root.title("Multilingual Talking Clock")

clock_width = 520
clock_height = 500

# Centering the window on the screen:
x_position = (root.winfo_screenwidth() - clock_width) // 2
y_position = (root.winfo_screenheight() - clock_height) // 2

root.geometry(f"{clock_width}x{clock_height}+{x_position}+{y_position}")

weather_label = tk.Label(root, font=('lucida console', 16, 'bold'), foreground='black')
weather_label.grid(row=0, column=0, columnspan=6, pady=20, sticky='n')

time_label = tk.Label(root, font=('lucida console', 40, 'bold'), foreground='black')
time_label.grid(row=1, column=0, columnspan=6, pady=20, sticky='n')

eng_icon = tk.PhotoImage(file="icons/eng_icon.png")
english_button = tk.Button(root, image=eng_icon, borderwidth=0, command=speak_time_in_english)
english_button.grid(row=4, column=0, padx=10, pady=20)

chn_icon = tk.PhotoImage(file="icons/chn_icon.png")
mandarin_button = tk.Button(root, image=chn_icon, borderwidth=0, command=speak_time_in_mandarin)
mandarin_button.grid(row=4, column=1, padx=10, pady=20)

ita_icon = tk.PhotoImage(file=r"icons/ita_icon.png")
italian_button = tk.Button(root, image=ita_icon, borderwidth=0, command=speak_time_in_italian)
italian_button.grid(row=4, column=2, padx=10, pady=20)

nl_icon = tk.PhotoImage(file="icons/nl_icon.png")
dutch_button = tk.Button(root, image=nl_icon, borderwidth=0, command=speak_time_in_dutch)
dutch_button.grid(row=4, column=3, padx=10, pady=20)

de_icon = tk.PhotoImage(file="icons/de_icon.png")
german_button = tk.Button(root, image=de_icon, borderwidth=0, command=speak_time_in_german)
german_button.grid(row=4, column=4, padx=10, pady=20)

lat_icon = tk.PhotoImage(file="icons/lat_icon.png")
latin_button = tk.Button(root, image=lat_icon, text="Latin", borderwidth=0, width=64, height=43,
                         command=speak_time_in_latin)
latin_button.grid(row=4, column=5, padx=10, pady=20)


def time():
    try:
        hour, minute, am_or_pm = get_current_time()
        start_color = hour_colors[int(hour) - 1]
        end_color = hour_colors[int(hour) % 12]
        ratio = float(minute) / 60.0
        gradient_color = compute_gradient_color(start_color, end_color, ratio)
        root.configure(bg=gradient_color)
        time_label.configure(bg=gradient_color)
        weather_label.configure(bg=gradient_color)
        weather_icon_label.configure(bg=gradient_color)
        time_label.config(text=f"{hour}:{minute} {am_or_pm}")

        english_button.config(state=NORMAL)
        mandarin_button.config(state=NORMAL)
        italian_button.config(state=NORMAL)
        dutch_button.config(state=NORMAL)
        german_button.config(state=NORMAL)
        latin_button.config(state=NORMAL)

    except Exception as time_error:
        messagebox.showerror("Error", f"An error occurred: {str(time_error)}")
    finally:
        time_label.after(60000, time)


def update_weather():
    try:
        city = "Leeuwarden"
        current_weather = get_weather(city, "584eb395bcf45a34c7ec7511b7d82c25")
        weather_label.config(text=current_weather)
    except Exception as weather_error:
        weather_label.config(text="Weather update failed.")
        print(f"Error updating weather: {weather_error}")
    finally:
        root.after(600000, update_weather)


def choose_weather_icon(weather_string):
    if not isinstance(weather_string, str):
        print("Error: Invalid weather_string input in choose_weather_icon.")
        return 'general'
    weather_map = {
        'sun': 'sun',
        'cloud': 'cloud',
        'rain': 'rain',
        'mist': 'mist',
        'snow': 'snow'
    }
    return next((weather_map[key] for key in weather_map if key in weather_string), 'general')


try:
    weather = choose_weather_icon(get_weather('Leeuwarden', "584eb395bcf45a34c7ec7511b7d82c25"))
    weather_icon = tk.PhotoImage(file=f"icons/{weather}.png")
    weather_icon_label = tk.Label(root, image=weather_icon, height=100, width=100)
    weather_icon_label.grid(row=2, column=0, columnspan=6, pady=20)
except Exception as e:
    print(f"Error while fetching and displaying weather icon: {e}")


def display_random_time():
    try:
        time_str = random_time()  # Get a random time string
        time_label.config(text=time_str)  # Display the random time

        # Extract the hour, minute, and AM/PM from the random time string
        hour, minute, am_or_pm = time_str.split()[0].split(':') + [time_str.split()[1]]
        hour = int(hour)
        minute = int(minute)

        # Determine the start and end colors
        start_color = hour_colors[hour - 1]  # Subtract 1 because list is 0-indexed
        end_color = hour_colors[hour % 12]  # Use modulo to loop back to 0 after 11

        # Compute the gradient ratio based on the current minute
        ratio = minute / 60.0

        # Calculate the gradient color for the random time's minute
        gradient_color = compute_gradient_color(start_color, end_color, ratio)

        # Update the background color of the root, label, and weather_label
        root.configure(bg=gradient_color)
        time_label.configure(bg=gradient_color)
        weather_label.configure(bg=gradient_color)
        weather_icon_label.configure(bg=gradient_color)

        # Disable speaking buttons -- this function solely affects GUI to show the color changing effects
        english_button.config(state=DISABLED)
        mandarin_button.config(state=DISABLED)
        italian_button.config(state=DISABLED)
        dutch_button.config(state=DISABLED)
        german_button.config(state=DISABLED)
        latin_button.config(state=DISABLED)

    except Exception as rand_error:
        messagebox.showerror("Error", f"An error occurred: {str(rand_error)}")


random_time_button = tk.Button(root, text='Display Random Time', command=display_random_time)
random_time_button.grid(row=3, column=0, columnspan=3, pady=20, padx=5, sticky='ew')

current_time_button = tk.Button(root, text='Display Current Time', command=time)
current_time_button.grid(row=3, column=3, columnspan=3, pady=20, padx=5, sticky='ew')

try:
    update_weather()
    time()
except Exception as init_error:
    print(f"Error initializing: {init_error}")

root.mainloop()
