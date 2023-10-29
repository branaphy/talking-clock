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
from helpers import get_current_date, get_current_time, compute_gradient_color, random_time

hour_colors = ['#FFFFCC', '#FFCC99', '#FFCCCC', '#FF99CC', '#FFCCFF', '#CC99FF', '#CCCCFF', '#99CCFF', '#CCFFFF',
               '#99FFCC', '#CCFFCC', '#CCFF99']

dark_bg = '#000447'
dark_fg = '#ABB0FF'

root = tk.Tk()
root.title("Multilingual Talking Clock")

clock_width = 517
clock_height = 575

# Centering the window on the screen:
x_position = (root.winfo_screenwidth() - clock_width) // 2
y_position = (root.winfo_screenheight() - clock_height) // 2

root.geometry(f"{clock_width}x{clock_height}+{x_position}+{y_position}")

weather_label = tk.Label(root, font=('lucida console', 16), foreground='black')
weather_label.grid(row=1, column=0, columnspan=6, pady=20, sticky='n')

time_label = tk.Label(root, font=('lucida console', 40, 'bold'), foreground='black')
time_label.grid(row=3, column=0, columnspan=6, pady=20, sticky='n')

date_label = tk.Label(root, font=('lucida console', 16), foreground='black')
date_label.grid(row=4, column=0, columnspan=6, pady=10, sticky='n')

eng_icon = tk.PhotoImage(file="icons/eng_icon.png")
english_button = tk.Button(root, image=eng_icon, borderwidth=0, command=speak_time_in_english)
english_button.grid(row=6, column=0, padx=10, pady=20)
english_label = tk.Label(text="English", fg='black', font=('lucida console', 10))
english_label.grid(row=7, column=0)

chn_icon = tk.PhotoImage(file="icons/chn_icon.png")
mandarin_button = tk.Button(root, image=chn_icon, borderwidth=0, command=speak_time_in_mandarin)
mandarin_button.grid(row=6, column=1, padx=10, pady=20)
mandarin_label = tk.Label(text="Chinese", fg='black', font=('lucida console', 10))
mandarin_label.grid(row=7, column=1)

ita_icon = tk.PhotoImage(file=r"icons/ita_icon.png")
italian_button = tk.Button(root, image=ita_icon, borderwidth=0, command=speak_time_in_italian)
italian_button.grid(row=6, column=2, padx=10, pady=20)
italian_label = tk.Label(text="Italian", fg='black', font=('lucida console', 10))
italian_label.grid(row=7, column=2)

nl_icon = tk.PhotoImage(file="icons/nl_icon.png")
dutch_button = tk.Button(root, image=nl_icon, borderwidth=0, command=speak_time_in_dutch)
dutch_button.grid(row=6, column=3, padx=10, pady=20)
dutch_label = tk.Label(text="Dutch", fg='black', font=('lucida console', 10))
dutch_label.grid(row=7, column=3)

de_icon = tk.PhotoImage(file="icons/de_icon.png")
german_button = tk.Button(root, image=de_icon, borderwidth=0, command=speak_time_in_german)
german_button.grid(row=6, column=4, padx=10, pady=20)
german_label = tk.Label(text="German", fg='black', font=('lucida console', 10))
german_label.grid(row=7, column=4)

lat_icon = tk.PhotoImage(file="icons/lat_icon.png")
latin_button = tk.Button(root, image=lat_icon, text="Latin", borderwidth=0, width=64, height=43,
                         command=speak_time_in_latin)
latin_button.grid(row=6, column=5, padx=10, pady=20)
latin_label = tk.Label(text="Latin", fg='black', font=('lucida console', 10))
latin_label.grid(row=7, column=5)

dark_mode_var = tk.BooleanVar(value=False)


def time():
    try:
        hour, minute, am_or_pm = get_current_time()
        start_color = hour_colors[int(hour) - 1]
        end_color = hour_colors[int(hour) % 12]
        ratio = float(minute) / 60.0
        gradient_color = compute_gradient_color(start_color, end_color, ratio)

        if dark_mode_var.get():
            bg_color = dark_bg
            fg_color = dark_fg
        else:
            bg_color = gradient_color
            fg_color = 'black'

        root.configure(bg=bg_color)
        time_label.configure(bg=bg_color, fg=fg_color)
        date_label.configure(bg=bg_color, fg=fg_color)
        weather_label.configure(bg=bg_color, fg=fg_color)
        weather_icon_label.configure(bg=bg_color, fg=fg_color)
        english_label.configure(bg=bg_color, fg=fg_color)
        mandarin_label.configure(bg=bg_color, fg=fg_color)
        italian_label.configure(bg=bg_color, fg=fg_color)
        dutch_label.configure(bg=bg_color, fg=fg_color)
        german_label.configure(bg=bg_color, fg=fg_color)
        latin_label.configure(bg=bg_color, fg=fg_color)
        time_label.config(text=f"{hour}:{minute} {am_or_pm}")

        english_button.config(state=NORMAL)
        mandarin_button.config(state=NORMAL)
        italian_button.config(state=NORMAL)
        dutch_button.config(state=NORMAL)
        german_button.config(state=NORMAL)
        latin_button.config(state=NORMAL)

        english_label.grid(row=7, column=0)
        mandarin_label.grid(row=7, column=1)
        italian_label.grid(row=7, column=2)
        dutch_label.grid(row=7, column=3)
        german_label.grid(row=7, column=4)
        latin_label.grid(row=7, column=5)

        weather_label.grid(row=1, column=0, columnspan=6, pady=20, sticky='n')
        weather_icon_label.grid(row=2, column=0, columnspan=6, pady=20)
        date_label.grid(row=4, column=0, columnspan=6, pady=10, sticky='n')
        dark_mode_switch.grid(row=0, column=0, columnspan=6, pady=5)

    except Exception as time_error:
        messagebox.showerror("Error", f"An error occurred: {str(time_error)}")
    finally:
        time_label.after(60000, time)


def toggle_dark_mode():
    time()


def update_date():
    date_label.config(text=get_current_date())


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
        'snow': 'snow',
        'drizzle' : 'drizzle'
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
        time_label.configure(bg=gradient_color, fg='black')
        date_label.configure(bg=gradient_color)
        weather_label.configure(bg=gradient_color)
        weather_icon_label.configure(bg=gradient_color)

        # Disable speaking buttons -- this function solely affects GUI to show the color changing effects
        english_button.config(state=DISABLED)
        mandarin_button.config(state=DISABLED)
        italian_button.config(state=DISABLED)
        dutch_button.config(state=DISABLED)
        german_button.config(state=DISABLED)
        latin_button.config(state=DISABLED)

        # Disable labels
        english_label.grid_forget()
        mandarin_label.grid_forget()
        italian_label.grid_forget()
        dutch_label.grid_forget()
        german_label.grid_forget()
        latin_label.grid_forget()
        weather_label.grid_forget()
        weather_icon_label.grid_forget()
        date_label.grid_forget()
        dark_mode_switch.grid_forget()

    except Exception as rand_error:
        messagebox.showerror("Error", f"An error occurred: {str(rand_error)}")


random_time_button = tk.Button(root, text='Display Random Time', command=display_random_time,
                               font=('lucida console', 10))
random_time_button.grid(row=5, column=0, columnspan=3, pady=20, padx=5, sticky='ew')

current_time_button = tk.Button(root, text='Display Current Time', command=time,
                                font=('lucida console', 10))
current_time_button.grid(row=5, column=3, columnspan=3, pady=20, padx=5, sticky='ew')

dark_icon = tk.PhotoImage(file="icons/moon.png")
dark_mode_switch = tk.Checkbutton(root, text="Dark Mode", variable=dark_mode_var, relief="ridge",
                                  command=toggle_dark_mode, font=('lucida console', 10))
dark_mode_switch.grid(row=0, column=0, columnspan=6, pady=5)

try:
    update_weather()
    time()
    update_date()
except Exception as init_error:
    print(f"Error initializing: {init_error}")

root.mainloop()
