# codealpha_tasks
# 🎮 Hangman Game

## 📌 Project Description
Hangman is a simple text-based word guessing game developed using Python. The player has to guess a hidden word one letter at a time. The game randomly selects a word from a predefined list of five words.

The player gets a maximum of 6 incorrect guesses to find the correct word.

## 🎯 Features
- Random word selection.
- Five predefined words.
- Maximum of 6 incorrect guesses.
- One-letter-at-a-time guessing.
- Displays correctly guessed letters.
- Checks repeated guesses.
- Input validation.
- Displays win or game-over messages.

## 🛠️ Technologies Used
- Python 3
- Random Module
- While Loop
- If-Else Statements
- Strings
- Lists

## 📂 Project Structure

```text
Hangman-Game/
│
├── hangman.py
└── README.md
```

## ▶️ How to Run the Project

1. Install Python 3 on your computer.
2. Download or clone this project.
3. Open the project folder.
4. Run the following command in the terminal:

```bash
python hangman.py
```

## 🎮 How to Play

1. Run the Python program.
2. The computer randomly selects a hidden word.
3. Enter one alphabet letter at a time.
4. If the letter is correct, it appears in the word.
5. If the letter is incorrect, you lose one attempt.
6. You have 6 incorrect guesses allowed.
7. Guess the complete word to win the game.
8. If you use all 6 incorrect guesses, the game ends.

## 💻 Sample Output

```text
================================
       WELCOME TO HANGMAN!
================================

Guess the hidden word one letter at a time.
You have 6 incorrect guesses allowed.

Word: _ _ _ _ _ _
Incorrect guesses left: 6

Enter a letter: p
Correct guess!

Word: p _ _ _ _ _
Incorrect guesses left: 6

Enter a letter: x
Wrong guess!

GAME OVER!

Thanks for playing Hangman!
```

## 📚 Concepts Learned
- Using the random module.
- Working with strings and lists.
- Implementing while loops.
- Using if-else conditions.
- Taking user input.
- Applying basic game logic.

## 👨‍💻 Author
Created as a beginner-level Python programming project.

## 📄 License
This project is created for educational purposes.
