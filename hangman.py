import random

def hangman():
    # Predefined list of words
    words = ["python", "developer", "hangman", "programming", "codealpha"]
    word = random.choice(words)  # pick a random word
    guessed_letters = []
    attempts = 6  # limit of wrong guesses

    print(" Welcome to Hangman Game!")
    print("Guess the word, one letter at a time.")
    print(f"You have {attempts} incorrect guesses allowed.\n")

    # Game loop
    while attempts > 0:
        # Show current progress
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
        print("Word: ", display_word)

        # Check if word is guessed
        if display_word == word:
            print("\n Congratulations! You guessed the word:", word)
            break

        # Take user input
        guess = input("Enter a letter: ").lower()

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("⚠ Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("⚠ You already guessed that letter.\n")
            continue

        # Check guess
        guessed_letters.append(guess)
        if guess in word:
            print("✅ Correct guess!\n")
        else:
            attempts -= 1
            print(f"❌ Wrong guess! Attempts left: {attempts}\n")

    else:
        print(f"\n Game Over! The word was: {word}")

# Run the gamea

if __name__ == "__main__":

    hangman()
