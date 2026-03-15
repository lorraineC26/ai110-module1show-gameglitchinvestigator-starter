# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

---
- Bug 1 (FIXED): The hints were backwards. When the player guessed a number that was too low, the app said "Too high!" and vice versa.
- Bug 2 (FIXED): The initial attempts on the main page does not match the attempts on the sidebar. The main page show one less attempt than the sidebar on the first load.
- Bug 3 (FIXED): The attempts on the main page does not update correctly. It shows 1 attempt left and "out of attempts" at the same time. In addition, the History does not update correctly. It should be the issue with the submit button.
- Bug 4 (FIXED): The "New Game" button does not completely reset the game. When I click it, it only resets the attempts and the secret number, but not the History and the message "Game over. Start a new game to try again".
- Bug 5 (FIXED): The difficulty levels for "Normal" and "Hard" do not work. While the Hard mode has the fewest attempts, the range (1 to 50) is smaller. The ideal difficulty levels should be: Easy (1-20, 8 attempts), Normal (1-50, 6 attempts), Hard (1-100, 5 attempts).

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---
- **AI tools used:** Gemini, GitHub Copilot, and Claude Code.
- **Correct AI suggestion:** I asked Claude Code to help me fix the issue with attempts not updating correctly (Bug 3). It suggested that the issue might be with the submit button and Streamlit state management. The info message displays before the submit handler runs, so it does not reflect the updated attempts. I verified the result by implementing the suggested fix and testing the game multiple times, confirming that the attempts now update correctly after each submission.
- **Misleading AI suggestion:** I asked Claude Code to refactor the `check_guess` function into `logic_utils.py`and ensure the logic is correct. It suggested to remove the `try-except` block that handles non-integer inputs, which is necessary to prevent crashing when input is not a valid integer. I verified the issue by inputting strings like "ppp". There were no error messages, so users would just be trapped in a loop without feedback. I had to re-add the try-except block to handle invalid inputs properly.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---
- **How I decided bugs were fixed:** For manual tests, I used the Streamlit app directly and checked specific behaviors—like guessing a number and verifying the hint message was correct (not backwards), comparing the main page and sidebar attempts counts, and clicking the "New Game" button to confirm both the history cleared AND the game state reset. For the difficulties, I selected each level (Easy, Normal, Hard) and checked that the number ranges and attempt limits matched what I expected. For pytest tests, I asked Claude Code to help me write the tests that specifically targeted the bug documented in this reflection. Then I ran `pytest` and ensured all assertions pass.

- **Test example:** I created a pytest test for Bug 3 called `test_bug3_attempts_with_info_message` that tracks attempts across multiple guesses and verifies the calculation `attempt_limit - attempts_made` matches the value that should display in the info message. I simulated 3 wrong guesses in a Normal difficulty game (6 attempt limit) and confirmed that after each guess, the "Attempts left" message would show the correct remaining count. This test passed after I fixed the bug, showing that the state updates were now properly tracked.

- **AI help with tests:** Yes, Claude Code helped me understand Streamlit state management and why the attempts message was stale. The issue was that the info message displayed *before* the submit handler updated the state, so it showed old values. Claude also suggested wrapping the display logic with `st.rerun()` after state updates to force a fresh render. Additionally, Claude helped me refactor the game logic into `logic_utils.py` so I could write unit tests for the core functions independently of Streamlit's widget behavior. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---
Every time a user clicks a button, Streamlit re-runs the entire script from top to bottom. This would normally reset all variables, so **session state** is a sticky note that remembers values like `attempts` and `history` across reruns. Without it, the game would forget everything each click. That's why I use `st.session_state` to store `attempts`, `history` and `secret` to keep track of the game state. When I fixed Bug 3, I also had to call `st.return()` at the end to force an extra refresh.

---


## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

---
- **Habit to reuse:** I want to make a documented list of bugs with clear descriptions and mark with something like `FIXME: ...` in the code to keep track of what I need to fix. This helps me stay organized and easy to communicate with AI tools about specific issues. I also would like to use copilot to generate commit messages based on the code changes I made (with some manual editing) to save time and ensure my commit history is clear.
- **What I would do differently:** Next time, I would start by writing some tests first. This would help me define the expected behavior and edge cases more clearly before getting into the code. I think this would be especially helpful for large projects. I would also ask AI to suggest potential edge cases to test that I might not have thought of.
- **How this project changed my thinking:** I have never used Streamlit before, and used python mostly for data analysis and leetcode problems. This project showed me by using AI tools, even I have no experience with Streamlit, I can quickly learn how to build/debug an interactive web app. The learning is more efficient and I feel more encouraged to try completely new things with the help of AI.