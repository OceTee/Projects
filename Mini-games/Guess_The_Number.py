import random

print("Welcome to the Guessing Game!")
print("Try to guess my secret number between 1 and 100.")

number = random.randint(1, 100)  # generate random number
guess = -1  # initialize guess to an invalid value

while guess != number:
    guess_str = input("Enter your guess: ")
    guess = int(guess_str)

    if guess < number:
        print("Too low, try again.")
    elif guess > number:
        print("Too high, try again.")

print(f"Congratulations! You guessed the number {number} correctly!")