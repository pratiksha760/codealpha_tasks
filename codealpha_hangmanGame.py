
import random

words = ["python", "computer", "program", "coding", "keyboard"]

secret_word = random.choice(words)

guessed_letters = []

max_attempts = 6
wrong_guesses = 0

print("================================")
print("       WELCOME TO HANGMAN!")
print("================================")
print("Guess the hidden word one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

while wrong_guesses < max_attempts:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_attempts - wrong_guesses)

    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You won!")
        print("The word was:", secret_word)
        break

    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

if wrong_guesses == max_attempts:
    print("\nGAME OVER!")
    print("The correct word was:", secret_word)

print("\nThanks for playing Hangman!")
