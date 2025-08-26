import random

class NumberGuessingGame:
    def __init__(self): # Constructor runs when a new game starts
        self.reset_game() # Call reset to reset the game


    def check_guess(self, guess):
        if not str(guess).isdigit(): # Checks input is a number and returns message if not
            return "Please enter a number", False

        guess = int(guess) # Convert guess from String to int
        self.attempts += 1 # Add one attempt

        if guess < self.number_to_guess: # If guess is smaller, return message
            return "Too low! Try again.", False
        elif guess > self.number_to_guess: # If guess is higher, return message
            return "Too high! Try again.", False
        else: # Success message if number guessed is correct
            return f"Correct! You guessed it in {self.attempts}, tries.", True

    # Choose a random number between 1 and 100, keep track of attempts (base 0)
    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0