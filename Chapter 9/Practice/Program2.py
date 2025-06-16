# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score
import random
import os

def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_score = 100

    while True:
        try:
            guess = int(input("👉 Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("📉 Too low! Try again.")
            elif guess > number_to_guess:
                print("📈 Too high! Try again.")
            else:
                score = max(max_score - (attempts - 1) * 10, 0)
                print(f"✅ Correct! You guessed it in {attempts} attempts.")
                return score
        except ValueError:
            print("❌ Please enter a valid number.")

# --- Read previous high score ---
hiscore_file = "Hi-score.txt"

# Handle if file doesn't exist or is empty
if os.path.exists(hiscore_file) and os.path.getsize(hiscore_file) > 0:
    with open(hiscore_file, "r") as f:
        prevScore = int(f.read())
else:
    prevScore = 0

print(f"📈 Current High Score = {prevScore}")

# --- Play the game ---
newScore = number_guessing_game()
print(f"🏆 Your score: {newScore}")

# --- Update high score if needed ---
if newScore > prevScore:
    with open(hiscore_file, "w") as f:
        f.write(str(newScore))
    print("🎉 New High Score Updated!")
else:
    print("🙁 Try again to beat the high score.")
