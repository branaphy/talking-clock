# The starting point of execution for the Talking Clock. This contains the code pertaining the GUI.

# Authors: Alice Vanni, Amber Lankheet, Brandi Hongell, Jingxuan Yue, Wenjun Meng

import tkinter as tk
from English import speak_time_in_english
# from Mandarin import speak_time_in_mandarin
# from Italian import speak_time_in_italian
# from Dutch import speak_time_in_dutch
from Weather import get_weather
from helpers import get_current_time, compute_gradient_color, random_time

hour_colors = ['#FF0000', '#FF7F00', '#FFFF00', '#7FFF00', '#00FF00', '#00FF7F',
               '#00FFFF', '#007FFF', '#0000FF', '#7F00FF', '#FF00FF', '#FF007F']

root = tk.Tk()
root.title("Talking Clock")
root.geometry("400x300+300+120")


# define function to fetch current hour and minute, update display time and bg color according to time
def time():
    hour, minute, am_or_pm = get_current_time()

    # Determine the start and end colors
    start_color = hour_colors[int(hour) - 1]  # Subtract 1 because list is 0-indexed
    end_color = hour_colors[int(hour) % 12]  # Use modulo to loop back to 0 after 11

    # Compute the gradient ratio based on the current minute
    ratio = float(minute) / 60.0

    # Calculate the gradient color for the current minute
    gradient_color = compute_gradient_color(start_color, end_color, ratio)

    root.configure(bg=gradient_color)
    time_label.configure(bg=gradient_color)
    weather_label.configure(bg=gradient_color)

    time_label.config(text=f"{hour}:{minute} {am_or_pm}")
    # time_label.after(10000, time)


def update_weather():
    city = "Leeuwarden"
    weather = get_weather(city, "584eb395bcf45a34c7ec7511b7d82c25")
    weather_label.config(text=weather)
    root.after(600000, update_weather)  # Update every 10 minutes


weather_label = tk.Label(root, font=('lucida console', 20, 'bold'), foreground='white')
weather_label.pack(anchor='center', pady=20)

# label widget to display time with display properties
time_label = tk.Label(root, font=('lucida console', 40, 'bold'), foreground='white')
time_label.pack(expand=True, anchor='center')


def display_random_time():
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


random_time_button = tk.Button(root, text='Get Random Time', command=display_random_time)
random_time_button.pack(pady=20)

current_time_button = tk.Button(root, text='Current Time', command=time)
current_time_button.pack(pady=20)

# language buttons that will speak the in the selected language when called
eng_icon = tk.PhotoImage(file="eng_icon.gif")
english_button = tk.Button(root, image=eng_icon, height=25, width=100, command=speak_time_in_english)
english_button.image = eng_icon
english_button.pack(pady=20)

# mandarin_button = tk.Button(root, text='Speak Time (Mandarin)', command=speak_time_in_mandarin)
# mandarin_button.pack()

ita_icon = tk.PhotoImage(file = r"ita_icon.gif")
italian_button = tk.Button(root, image=ita_icon, height= 25, width=100, command=speak_time_in_italian)
italian_button.pack(pady=20)

# dutch_button = tk.Button(root, text='Speak Time (Dutch)', command=speak_time_in_dutch)
# dutch_button.pack()

# call the weather function to initialize the weather label
update_weather()
# call the time function to initialize the label
time()

# main event loop for GUI
root.mainloop()
