import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

def play_game(user_choice):
    computer_choice = random.randint(0, 2)
    choices = ["Rock", "Paper", "Scissors"]
    
    result_message = f"Computer chose: {choices[computer_choice]}\n"
    
    if computer_choice == user_choice:
        result_message += "It's a draw."
    elif (computer_choice == 0 and user_choice == 2) or (computer_choice > user_choice):
        result_message += "You lose."
    else:
        result_message += "You win!"

    messagebox.showinfo("Result", result_message)

# Set up the main window
window = tk.Tk()
window.title("Rock Paper Scissors Game")
window.geometry("600x400")  # Set an initial window size
window.configure(bg="#3AAFA9")

# Load and set the background image
background_image = Image.open("sps.jpg")
background_image = background_image.resize((600, 400), Image.LANCZOS)
background_photo = ImageTk.PhotoImage(background_image)

# Create a label with a background image
background_label = tk.Label(window, image=background_photo)
background_label.place(relwidth=1, relheight=1)  # Fill the window with the background image

# Create a frame for the option label with border
frame = tk.Frame(window, bg="white", bd=2, relief=tk.SUNKEN)
frame.pack(pady=20)

# Create a label
label = tk.Label(frame, text="Choose your option", font=("Helvetica", 16), bg="#cb38a8",fg="white")
label.pack(pady=20)

# Create buttons for user choices with custom colors
button_width = 10  # Set the width of the buttons

rock_button = tk.Button(window, text="Rock", font=("Helvetica", 14), command=lambda: play_game(0), bg="#3d61c8", fg="white", width=button_width)
rock_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

paper_button = tk.Button(window, text="Paper", font=("Helvetica", 14), command=lambda: play_game(1), bg="#763dc8", fg="white", width=button_width)
paper_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

scissors_button = tk.Button(window, text="Scissors", font=("Helvetica", 14), command=lambda: play_game(2), bg="#8f3dc8", fg="white", width=button_width)
scissors_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

# Run the main event loop
window.mainloop()
