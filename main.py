# The starting point of execution for the Talking Clock. This contains the code pertaining the GUI.

# Authors: Alice Vanni, Amber Lankheet, Brandi Hongell, Jingxuan Yue, Wenjun Meng

import tkinter as tk
from English import speak_time_in_english
# from Mandarin import speak_time_in_mandarin
# from Italian import speak_time_in_italian
# from Dutch import speak_time_in_dutch
from helpers import get_current_time

root = tk.Tk()
root.title("Talking Clock")
root.geometry("400x300+300+120")

def time():
    hour, minute = get_current_time()
    label.config(text=f"{hour}:{minute}")
    label.after(1000, time)

label = tk.Label(root, font=('lucida console', 40, 'bold'), background='purple', foreground='white')
label.pack(anchor='center')

english_button = tk.Button(root, text='Speak Time (English)', command=speak_time_in_english)
english_button.pack()

# mandarin_button = tk.Button(root, text='Speak Time (Mandarin)', command=speak_time_in_mandarin)
# mandarin_button.pack()

# italian_button = tk.Button(root, text='Speak Time (Italian)', command=speak_time_in_italian)
# italian_button.pack()

# dutch_button = tk.Button(root, text='Speak Time (Dutch)', command=speak_time_in_dutch)
# dutch_button.pack()

time()
root.mainloop()
