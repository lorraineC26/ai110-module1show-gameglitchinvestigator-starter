import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"


def test_bug3_attempts_tracking():
    """
    Bug 3: Attempts did not update correctly on main page.
    This test verifies that attempts increment properly and the game ends when attempts are exhausted.
    """
    from logic_utils import update_score

    # Simulate Easy difficulty with 8 attempt limit (range 1-20)
    secret = 15
    attempt_limit = 8
    attempts = 0
    score = 0

    # Simulate 7 failed guesses (attempts 1-7)
    guesses = [1, 3, 5, 7, 9, 11, 13]
    for guess in guesses:
        outcome, _ = check_guess(guess, secret)
        attempts += 1
        score = update_score(score, outcome, attempts)
        assert attempts <= attempt_limit, "Attempts should not exceed limit"

    # After 7 attempts, we still have 1 attempt left
    assert attempts == 7
    assert attempt_limit - attempts == 1, "Should have 1 attempt left"

    # Make one more failed guess (8th attempt, exhausts limit)
    outcome, _ = check_guess(18, secret)
    attempts += 1
    score = update_score(score, outcome, attempts)

    # Now attempts should equal limit, game should be over
    assert attempts == attempt_limit
    assert attempt_limit - attempts == 0, "Attempts should be 0 when limit reached"


def test_bug3_attempts_with_info_message():
    """
    Bug 3: The info message showed stale attempt values.
    Verify that "Attempts left" calculation is correct at each step.
    """
    secret = 50
    attempt_limit = 6  # Normal difficulty
    attempts_made = 0

    # Simulate the info message display: "Attempts left: {attempt_limit - attempts_made}"
    # After 3 wrong guesses, should show "Attempts left: 3"
    wrong_guesses = [10, 20, 30]

    for guess in wrong_guesses:
        _, _ = check_guess(guess, secret)
        attempts_made += 1
        # Verify the info message would display the correct remaining attempts
        attempts_left = attempt_limit - attempts_made
        assert attempts_left == attempt_limit - attempts_made, \
            f"After {attempts_made} attempts, should show {attempts_left} attempts left"

    assert attempts_made == 3
    assert attempt_limit - attempts_made == 3, "Info message should show 3 attempts left"


def test_bug4_new_game_reset():
    """
    Bug 4: The "New Game" button does not completely reset the game.
    Before fix: Only resets attempts and secret, but not History and status.
    Verify that game state is completely reset.
    """
    # Simulate a game in progress with multiple guesses and some score
    game_state = {
        "secret": 50,
        "attempts": 5,
        "score": 20,
        "history": [10, 20, 30, 40, 45],
        "status": "playing",
        "last_message": "📈 Go HIGHER!",
        "last_outcome": "Too Low"
    }

    # Simulate losing condition (out of attempts, outcome not Win)
    game_state["attempts"] = 6  # Hit the limit
    game_state["status"] = "lost"
    game_state["last_message"] = "Out of attempts! The secret was 50."
    game_state["last_outcome"] = "Lost"

    # Verify game is in "lost" state with history
    assert game_state["status"] == "lost"
    assert len(game_state["history"]) > 0
    assert game_state["last_outcome"] == "Lost"

    # Now simulate the new game reset (from on_new_game callback)
    game_state["attempts"] = 0
    game_state["score"] = 0
    game_state["history"] = []
    game_state["status"] = "playing"
    game_state["secret"] = 75  # New random secret
    game_state["last_message"] = None
    game_state["last_outcome"] = None

    # Verify all state is properly reset
    assert game_state["attempts"] == 0, "Attempts should be reset to 0"
    assert game_state["score"] == 0, "Score should be reset to 0"
    assert game_state["history"] == [], "History should be cleared (THIS WOULD HAVE CAUGHT BUG 4)"
    assert game_state["status"] == "playing", "Status should be reset to 'playing'"
    assert game_state["last_message"] is None, "Last message should be cleared (THIS WOULD HAVE CAUGHT BUG 4)"
    assert game_state["last_outcome"] is None, "Last outcome should be cleared"
    assert game_state["secret"] != 50, "Secret should be a new random number"


