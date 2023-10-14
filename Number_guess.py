import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

while True:
    guess = int(input("Guess the secret number (between 1 and 100): ")
    if guess == secret_number:
        print("Congratulations! You guessed the secret number.")
        break
    elif guess < secret_number:
        print("Try a higher number.")
    else:
        print("Try a lower number.")
