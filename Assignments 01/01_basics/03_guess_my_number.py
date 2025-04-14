# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48
# Starter Code

import random

def main():
    computer_guess_number = random.randint(0, 99)
    user_guess_number = int(input("I am thinking of a number between 0 and 99... Enter a guess: "))

    while user_guess_number != computer_guess_number:
        if user_guess_number < computer_guess_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        user_guess_number = int(input("Enter a new number: "))

    print(f"Congrats! The number was: {computer_guess_number}")

if __name__ == '__main__':
    main()
