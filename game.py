import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = random.randint(1, 100)
count = 0

while True:
    guess = input("Make a guess: ")

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    count += 1

    if guess < number:
        print("Too low.")
    elif guess > number:
        print("Too high.")
    else:
        print(f"Congratulations! You've guessed the number {number} in {count} attempts.")
        break