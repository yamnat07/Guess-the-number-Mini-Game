# 🎯 Guess The Number

A simple command-line number guessing game built in Python. The program picks a random number between 1 and 100, and the player has to guess it using hints ("Too High" / "Too Low") until they get it right.

---

## 📌 What This Project Does

- Generates a random secret number between **1 and 100**.
- Prompts the user to guess the number.
- Gives feedback after every guess:
  - `Too High!` if the guess is greater than the secret number
  - `Too Low!` if the guess is smaller than the secret number
  - A congratulations message once the correct number is guessed
- Tracks and displays the **total number of attempts** taken to win.
- Lets the user **play again** with a new random number, or **exit** the game.

---

## 🖥️ Interface / How To Run

1. Make sure Python 3 is installed.
2. Run the script from your terminal:
   ```bash
   python guess-the-number.py
   ```
3. You'll see:
   ```
   ====================
   GUESS THE NUMBER
   ====================
   I have chosen a number, can you guess it?
   Enter your Guess:
   ```
4. Type a number between 1 and 100 and press Enter.
5. Keep guessing based on the hints until you find the correct number.
6. After winning, choose:
   ```
   1.Play again
   2.Exit
   ```

---

## 🧠 Concepts Used

This project is a great beginner exercise because it touches several core Python concepts:

| Concept | Where it's used |
|---|---|
| **Modules** | `import random` for generating random numbers |
| **Functions** | `guess_it()` for game logic, `main()` for the game loop/menu |
| **Function parameters** | `secret_num` passed into `guess_it()` |
| **Loops** | `while True` loops for repeated guessing and repeated menu prompts |
| **Conditionals** | `if / elif / else` to compare guess vs. secret number |
| **Type casting** | `int(input(...))` to convert text input into a number |
| **Exception handling** | `try / except ValueError` to catch non-numeric input |
| **f-strings** | Formatted output like `f"Total Attempts:{attempts}"` |
| **Boolean flow control** | `break` and `continue` to control loop execution |
| **Program entry point pattern** | Calling `main()` at the bottom of the script to start execution |

---

## 🛡️ Exception Handling in Attempts

The game is designed to handle bad input gracefully so it never crashes:

- **Non-numeric input** (e.g. typing `"abc"` instead of a number):
  - Caught by `except ValueError` inside the guessing loop.
  - Message shown: `Enter a number.`
  - Importantly, this does **not** increase the `attempts` counter — only valid numeric guesses within range count as an attempt.

- **Out-of-range input** (e.g. `0`, `150`, `-5`):
  - Checked with `if your_guess < 1 or your_guess > 100`.
  - Message shown: `Enter a number from 1 to 100.`
  - This also does **not** count as an attempt, and the loop uses `continue` to re-prompt immediately.

- **Menu input errors** (in `main()`):
  - If the user types something non-numeric at the "Play again / Exit" menu, it's caught by a separate `try / except ValueError` block with the message `Enter a valid number!!`.
  - If a numeric but invalid choice (like `3`) is entered, the `else` branch shows `Enter a valid choice!!!!`.

This layered validation ensures the **attempts counter only reflects genuine, valid guesses**, giving the player an accurate score.

---

## 📈 My Python Learning Progress

Building this project helped practice and demonstrate the following skills:

- ✅ Writing and calling custom functions
- ✅ Passing arguments between functions
- ✅ Using `while` loops for interactive, repeatable programs
- ✅ Validating user input safely with `try/except`
- ✅ Structuring a program with a clear `main()` entry point
- ✅ Using the `random` module for randomness
- ✅ Designing simple, readable console UI with formatted print statements
- ✅ Managing game state (attempts counter, replay loop) across multiple rounds

This project marks a milestone in moving from basic syntax practice to writing a **complete, interactive, error-resistant mini-application**.

---

## 🚀 Possible Future Improvements

- Add a difficulty selector (e.g. range of 1–50, 1–100, 1–500)
- Add a maximum number of attempts / limited lives mode
- Track and display a high score (fewest attempts) across sessions
- Add unit tests for the guessing logic
