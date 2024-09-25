Overview:
This is a simple yet engaging Rock Paper Scissors game created using Python's Tkinter library for the graphical user interface (GUI). The game allows users to play against a computer opponent, where each player selects one of the three options: Rock, Paper, or Scissors. The result of the game is displayed in a message box, indicating whether the player won, lost, or if it was a draw.

Key Features:

Graphical User Interface:

The game features a visually appealing interface with a background image (sps.jpg) that enhances the user experience.
A frame with a border is used to enclose the option label, making it stand out against the background.
User Interaction:

Users can select their choice by clicking one of the three buttons: "Rock," "Paper," or "Scissors."
The buttons are styled with custom colors for an attractive appearance, using hex color codes for background and text colors.
Game Logic:

Upon selecting an option, the computer randomly chooses its move (also Rock, Paper, or Scissors) using the random module.
The game's rules are implemented to determine the outcome based on the choices made by the player and the computer:
Rock beats Scissors
Scissors beat Paper
Paper beats Rock
The results are conveyed to the player through a pop-up message box using messagebox.showinfo().
Layout and Design:

The window is configured to a fixed size of 600x400 pixels, ensuring consistency in the display.
Buttons are designed to fill available space and expand responsively, enhancing usability on various screen sizes.
The text on the buttons and labels is styled with a clear and readable font.
Customization:

The game allows for easy modifications, such as changing the background image, button colors, or adding more game features like scoring or multiple rounds.
Usage: To play the game, simply run the Python script. Select your choice by clicking one of the buttons. The result of the game will be displayed in a message box after your selection.
