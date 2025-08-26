# lib for GUI elements, buttons etc..
import tkinter as tk




# The GUI setup
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("450x430")
root.configure(bg="#1E1E2F")

# Widgets for labels and buttons..

# Specify Label specifics like text, font style and color, bg of the label and the fg of the label
title_label = tk.Label(root, text=" Number Guessing Game", font=("Arial Black", 20), bg="#1E1E2F", fg="#FFFFFF")
title_label.pack(pady=20) # Vertical spacing fo 20 pixels from top to bottom with default pack behaviour

enter = tk.Entry(root, font=("Arial", 14), justify="center", width=10, bg="#2E2E3F", fg="#FFFFFF", bd=0, insertbackground="#FFFFFF")
enter.pack(pady=10, padx=20)

# bd = border, padx= space lft and right pady= top and bottom
guess_button = tk.Button(root, text="Guess", font=("Arial", 12, "bold"), bg="#6BCB77", fg="#1E1E2F",activebackground="#58C470", bd=0, padx=20, pady=10)
guess_button.pack(pady=10)


reset_button = tk.Button(root, text="Reset", font=("Arial", 12, "bold"), bg="#FF6B6B", fg="#1E1E2F",activebackground="#FF4C4C", bd=0, padx=20, pady=10)
reset_button.pack(pady=10)



root.mainloop()