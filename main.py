# The starting point of execution for the Talking Clock. This contains the code pertaining the GUI.

# Authors: Alice Vanni, Amber Lankheet, Brandi Hongell, Jingxuan Yue, Wenjun Meng

import tkinter as tk
from English import speak_time_in_english
from Mandarin import speak_time_in_mandarin
from Italian import speak_time_in_italian
from German import speak_time_in_german
from Latin import speak_time_in_latin
from Dutch import speak_time_in_dutch
from Weather import get_weather
from helpers import get_current_time, compute_gradient_color, random_time

hour_colors = ['#FF0000', '#FF7F00', '#FFFF00', '#7FFF00', '#00FF00', '#00FF7F',
               '#00FFFF', '#007FFF', '#0000FF', '#7F00FF', '#FF00FF', '#FF007F']

root = tk.Tk()
root.title("Multilingual Talking Clock")
screen_height = root.winfo_screenheight()
x = ((root.winfo_screenwidth()) - screen_height) // 2
root.geometry(f"500x{screen_height}+{x}+0")


# define function to fetch current hour and minute, update display time and bg color according to time
def time():
    '''
    This function fetches the current hour and minute and displays 
    time and background colour according to the time fetched.
    It takes no arguments.

    Returns
    -------
    None.
    
    This function does not return a value, it configures the GUI.
    '''
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
    weather_icon_label.configure(bg=gradient_color)

    time_label.config(text=f"{hour}:{minute} {am_or_pm}")
    # time_label.after(10000, time)


def update_weather():
    '''
    This function takes no arguments, it retrieves the current weather 
    in Leeuwarden (NL) using the Weather API.
    It gets updated every 10 minutes.

    Returns
    -------
    None.
    
    This function does not return a value, it has consequences on the GUI.
    '''
    city = "Leeuwarden"
    weather = get_weather(city, "584eb395bcf45a34c7ec7511b7d82c25")
    weather_label.config(text=weather)
    root.after(600000, update_weather)  # Update every 10 minutes


weather_label = tk.Label(root, font=('lucida console', 20, 'bold'), 
                         foreground='white')
weather_label.pack(anchor='center', pady=20)

# label widget to display time with display properties
time_label = tk.Label(root, font=('lucida console', 40, 'bold'), 
                      foreground='white')
time_label.pack(expand=True, anchor='center')

def choose_weather_icon(weather_string):
    '''
    This function takes a weather string as its only argument and choose
    the appropriate icon based on the current weather. 
    If no appropriate icon is found, it chooses a general one.

    Parameters
    ----------
    weather_label : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    '''
    weather_list = ['sun', 'cloud', 'rain', 'mist', 'snow']
    for i in weather_list:
        if weather_string.find(i)!=-1:
            return i
    return 'general'

weather = choose_weather_icon(get_weather('Leeuwarden', "584eb395bcf45a34c7ec7511b7d82c25"))
weather_icon = tk.PhotoImage(file=f"icons/{weather}.png")
# label widget to show the weather icon based on the previous function
weather_icon_label = tk.Label(root, image=weather_icon, height=100,
                           width=100)
weather_icon_label.pack(anchor='center', pady=20)

def display_random_time():
    '''
    This function takes no argument; it generates a random time string to
    be displayed in the GUI; based on the generated string, 
    it also changes the colour of the background.

    Returns
    -------
    None.
    
    This function does not return a value, it has effects on the GUI.
    '''
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


random_time_button = tk.Button(root, text='Get Random Time',
                               command=display_random_time)
random_time_button.pack(pady=20)

current_time_button = tk.Button(root, text='Current Time', command=time)
current_time_button.pack(pady=20)

# language buttons that will speak the in the selected language when called
eng_icon = tk.PhotoImage(file="icons/eng_icon.gif")
english_button = tk.Button(root, image=eng_icon, height=25,
                           width=100, command=speak_time_in_english)
english_button.image = eng_icon
english_button.pack(pady=20)

chn_icon = tk.PhotoImage(file="icons/chn_icon.png")
mandarin_button = tk.Button(root, image=chn_icon, height=25,
                           width=100, command=speak_time_in_mandarin)
mandarin_button.pack(pady=20)

ita_icon = tk.PhotoImage(file = r"icons/ita_icon.gif")
italian_button = tk.Button(root, image=ita_icon, borderwidth=0, height= 25,
                           width=100, command=speak_time_in_italian)
italian_button.pack(pady=20)

nl_icon = tk.PhotoImage(file="icons/nl_icon.png")
dutch_button = tk.Button(root, image=nl_icon, height=25, 
                         width=100, command=speak_time_in_dutch)
dutch_button.pack()

de_icon = tk.PhotoImage(file="icons/de_icon.gif")
german_button = tk.Button(root, image=de_icon, borderwidth=0, height=25,
                          width=100, command=speak_time_in_german)
german_button.image = de_icon
german_button.pack(pady=20)

lat_icon = tk.PhotoImage(file="icons/lat_icon.png")
latin_button = tk.Button(root, image=lat_icon, height=25, 
                         width=100, command=speak_time_in_latin)
latin_button.image = lat_icon
latin_button.pack(pady=20)

# call the weather function to initialize the weather label
update_weather()
# call the time function to initialize the label
time()

# main event loop for GUI
root.mainloop()
