import random
secret_number = random.randint(1, 100)
attempts=0
print("Welcome to the Number Guessing Game!")
while True:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break