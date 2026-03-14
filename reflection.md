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

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---
- **AI tools used:** Gemini, GitHub Copilot, and Claude Code.
- **Correct AI suggestion:** I asked Claude Code to help me fix the issue with attempts not updating correctly (Bug 3). It suggested that the issue might be with the submit button and Streamlit state management. The info message displays before the submit handler runs, so it does not reflect the updated attempts. I verified the result by implementing the suggested fix and testing the game multiple times, confirming that the attempts now update correctly after each submission.
- **Misleading AI suggestion:** I asked Claude Code to refactor the `check_guess` function into `logic_utils.py`and ensure the logic is correct. It suggested to remove the `try-except` block that handles non-integer inputs, which is necessary to prevent crashing when input is not a valid integer. I verified the issue by inputting strings like "ppp". There were no error messages, so users would just be trapped in a loop without feedback. I had to re-add the try-except block to handle invalid inputs properly.

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
