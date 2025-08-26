# lib for GUI elements, buttons etc..
import tkinter as tk
from logic import NumberGuessingGame

game = NumberGuessingGame()


# The GUI setup
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("450x430")
root.configure(bg="#1E1E2F")


# Get the input from enter-box/input, call check_guess from logic
# Green label text if correct, yellow if wrong
def check_guess():
    message, correct = game.check_guess(enter.get())
    result_label.config(text=message, fg="#6BCB77" if correct else "#FFD93D")

def reset_game():
    game.reset_game() # Start a new game
    enter.delete(0, tk.END) # Clear enter box
    result_label.config(text="", fg="#FFFFFF") # Reset the result label


# Widgets for labels and buttons..

# Specify Label specifics like text, font style and color, bg of the label and the fg of the label
title_label = tk.Label(root, text=" Number Guessing Game: 1-100", font=("Comic Sans MS", 20), bg="#2E2E3F", fg="#FFFFFF")
title_label.pack(pady=20) # Vertical spacing fo 20 pixels from top to bottom with default pack behaviour

enter = tk.Entry(root, font=("Comic Sans MS", 14), justify="center", width=10, bg="#2E2E3F", fg="#FFFFFF", bd=0, insertbackground="#FFFFFF")
enter.pack(pady=10, padx=20)

# bd = border, padx= space lft and right pady= top and bottom
guess_button = tk.Button(root, text="Guess", font=("Comic Sans MS", 12, "bold"), bg="#6BCB77", fg="#1E1E2F",activebackground="#58C470", activeforeground="#FFFFFF", command=check_guess, bd=0, padx=20, pady=10)
guess_button.pack(pady=10)


reset_button = tk.Button(root, text="Reset", font=("Comic Sans MS", 12, "bold"), bg="#FF6B6B", fg="#1E1E2F",activebackground="#FF4C4C", activeforeground="#FFFFFF", command=reset_game, bd=0, padx=20, pady=10)
reset_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Comic Sans MS", 10),  bg="#1E1E2F", fg="#FFFFFF",)
result_label.pack(pady=20)

root.mainloop()