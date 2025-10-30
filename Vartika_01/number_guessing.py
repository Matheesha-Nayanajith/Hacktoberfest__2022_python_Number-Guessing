import random
import math

# Taking inputs for lower and upper bounds
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

# Generate a random number between the bounds
target_number = random.randint(lower, upper)

# Calculate the maximum number of guesses allowed
max_guesses = round(math.log2(upper - lower + 1))
print(f"\nYou have {max_guesses} chances to guess the integer!\n")

# Initialize the guess counter
guess_count = 0

# Loop for taking guesses
while guess_count < max_guesses:
    guess_count += 1
    guess = int(input("Guess a number: "))

    if guess == target_number:
        print(f"Congratulations! You guessed it in {guess_count} tries.")
        break
    elif guess < target_number:
        print("Your guess is too low!")
    else:  # guess > target_number
        print("Your guess is too high!")

# If the player used all guesses without success
if guess_count >= max_guesses and guess != target_number:
    print(f"\nSorry! The number was {target_number}. Better luck next time!")
