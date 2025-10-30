import random
import math

# Taking inputs from the user
lower = int(input("Enter the lower bound: "))
upper = int(input("Enter the upper bound: "))

# Generating a random number
x = random.randint(lower, upper)

# Maximum number of chances based on binary search logic
max_attempts = round(math.log(upper - lower + 1, 2))
print(f"\nYou have only {max_attempts} chances to guess the integer!\n")

# Initialize attempt counter
count = 0

while count < max_attempts:
    count += 1
    # Taking the user's guess
    guess = int(input("Guess a number: "))

    # Checking the guess
    if guess == x:
        print(f"Congratulations! You guessed it in {count} {'try' if count == 1 else 'tries'}.")
        break
    elif guess < x:
        print("Too low!")
    else:
        print("Too high!")

# If all attempts are used
if count >= max_attempts and guess != x:
    print(f"\nThe number was {x}.")
    print("Better luck next time!")
