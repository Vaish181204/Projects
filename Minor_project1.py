import tkinter as tk
from tkinter import messagebox
import random

# Initialize the main window
root = tk.Tk()
root.title("Number Guessing Game")

# Generate a random number between 1 and 25
target_num= random.randint(1, 25)

# Function to check the user's guess
def check_guess():
    try:
        # Get the user's guess from the entry widget
        user_guess = int(guess_entry.get())
        # Compare the guess to the target number
        if user_guess == target_num:
            messagebox.showinfo("Your Guess", "Superb!! You have guessed the correct number!!!")
            root.destroy()
        elif user_guess < target_num:
            messagebox.showinfo("Sorry... Try Again", "Try Guessing a Higher Number")
        else:
            messagebox.showinfo("Sorry... Try Again", "Try Guessing a Lower Number")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

# Create an entry widget for the user to input their guess
guess_entry = tk.Entry(root)
guess_entry.pack()

# Create a button that will check the user's guess when clicked
guess_button = tk.Button(root, text="Play", command=check_guess)
guess_button.pack()

# Start the main loop
root.mainloop()