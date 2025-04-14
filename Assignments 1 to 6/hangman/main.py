import random

def hangman():
    
    words = ["python", "hangman", "programming", "developer", "computer",]
    
    word = random.choice(words)  # Computer selects a random word
    guessed_letters = set()  # Stores correct guesses
    incorrect_guesses = set()  # Stores incorrect guesses
    attempts = 6  # Number of allowed mistakes

    print("Welcome to Hangman!")
    
    while attempts > 0:
        # Display the word with guessed letters revealed
        display_word = " ".join([letter if letter in guessed_letters else "_" for letter in word])
        print("\nWord: ", display_word)
        
        if "_" not in display_word:
            print("\nCongratulations! You guessed the word:", word)
            break
        
        guess = input("\nGuess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in guessed_letters or guess in incorrect_guesses:
            print("You already guessed that letter. Try again!")
            continue

        if guess in word:
            guessed_letters.add(guess)
            print(f"Good job! {guess} is in the word.")
        else:
            incorrect_guesses.add(guess)
            attempts -= 1
            print(f"Wrong guess! {guess} is not in the word. Attempts left: {attempts}")

    if attempts == 0:
        print("\nGame Over! The word was:", word)

# Run the game
hangman()
