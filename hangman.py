
import random

# Secret words
words = [
    "python",
    "computer",
    "programming",
    "database",
    "student",
    "technology",
    "hangman",
    "keyboard"
]

# Hangman drawing stages
HANGMAN = [
    """
     +---+
     |   |
         |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    ========
    """
]


def play_hangman():

    secret_word = random.choice(words)

    guessed_letters = set()

    wrong_guesses = 0
    max_attempts = 6

    print("\nWelcome to Hangman!")
    print("Guess the hidden word.")

    while wrong_guesses < max_attempts:

        print(HANGMAN[wrong_guesses])

        print("Guessed letters:",
              " ".join(sorted(guessed_letters)))

        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)

        if all(letter in guessed_letters
               for letter in secret_word):
            print("\nCongratulations! You won!")
            print("The word was:", secret_word)
            return

        guess = input("\nEnter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")
            print("Attempts remaining:",
                  max_attempts - wrong_guesses)

    print(HANGMAN[wrong_guesses])

    print("\nGame Over! You lost.")
    print("The correct word was:", secret_word)


if __name__ == "__main__":
    play_hangman()
