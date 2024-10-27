import tkinter as tk
from tkinter import font
from tkinter import ttk
import subprocess
import threading

# Define functions to run each of your Python scripts
def run_program_1():
    subprocess.run(["python", "two_person_model.py"])  # Replace with the actual path if needed

def run_program_2():
    subprocess.run(["python", "three_person_model.py"])  # Replace with the actual path if needed

# Define the function to run the selected program in a separate thread
def run_selected_program():
    selected_program = program_choice.get()
    if selected_program == 1:
        threading.Thread(target=run_program_1).start()
    elif selected_program == 2:
        threading.Thread(target=run_program_2).start()

# Create the main Tkinter window
root = tk.Tk()
root.title("Python Program Runner")
root.geometry("400x300")  # Set window size

# Set a light background color
root.configure(bg="#f0f0f0")

# Create font objects for title and radio buttons
title_font = font.Font(size=14, weight="bold")
choice_font = font.Font(size=10, weight="bold")

# Frame for content
frame = ttk.Frame(root, padding="20")
frame.pack(expand=True, fill=tk.BOTH)

# Label
label = tk.Label(frame, text="Choose a program to run:", font=title_font, bg="#f0f0f0")
label.pack(anchor="center", pady=10)

# Radio buttons with smaller bold text
program_choice = tk.IntVar()
program_choice.set(1)  # Default choice

radio1 = tk.Radiobutton(frame, text="Speech Separation for Two Persons", variable=program_choice, value=1, font=choice_font, bg="#f0f0f0")
radio1.pack(anchor="w", pady=(5, 0))

radio2 = tk.Radiobutton(frame, text="Speech Separation for Three Persons", variable=program_choice, value=2, font=choice_font, bg="#f0f0f0")
radio2.pack(anchor="w", pady=(10, 0))

# Button
run_button = ttk.Button(frame, text="Run Program", command=run_selected_program)
run_button.pack(pady=20)

# Run the Tkinter main loop
root.mainloop()
