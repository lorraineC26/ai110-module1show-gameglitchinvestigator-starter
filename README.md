# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **Game's Purpose:** The app is a number guessing game where players try to guess a secret number within a limited number of attempts. The game has three difficulty levels (Easy: 1-20 with 8 attempts, Normal: 1-50 with 6 attempts, Hard: 1-100 with 5 attempts). Players get hints after each guess ("Too High" or "Too Low") to help them narrow down the number.

- [x] **Bugs Found:**
  1. **Backwards hints** — The app said "Too High" when guesses were too low, and vice versa.
  2. **Mismatched attempt counts** — The main page and sidebar showed different attempt numbers on first load.
  3. **Stale attempt messages** — The "Attempts left" message showed old values instead of updating after each guess.
  4. **Incomplete reset** — The "New Game" button didn't clear the game history and status messages.
  5. **Wrong difficulty settings** — Difficulty levels had incorrect number ranges and attempt limits.

- [x] **Fixes Applied:**
  1. **Fixed hints** — Swapped the "Too High" and "Too Low" logic in `check_guess()` function to match correct comparisons.
  2. **Synced attempts** — Changed initial attempts from 1 to 0 to match the sidebar calculation.
  3. **Fixed stale messages** — Added `st.rerun()` after updating game state so the info message displays fresh values.
  4. **Complete reset** — Updated the `on_new_game()` callback to clear history, status, and messages, not just attempts.
  5. **Corrected difficulties** — Updated difficulty ranges (Easy: 1-20, Normal: 1-50, Hard: 1-100) and attempt limits (8, 6, 5) to match intended balance.

## 📸 Demo

*Winning Game Demo: Successfully guessed the secret number with correct hints!*

![Screenshot of the fixed winning game](public/screenshot_winning%20game.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
