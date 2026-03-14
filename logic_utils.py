def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")

# FIX: Refactored logic into logic_utils.py using claude code
def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None:
        return False, None, "Enter a guess."

    if raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None

# FIX: Refactored logic into logic_utils.py using claude code
def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low", "Error"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"

    try:
        if guess > secret:
            return "Too High", "📉 Go LOWER!"
        else:
            return "Too Low", "📈 Go HIGHER!"
    except TypeError:
        # Handle type mismatch by converting both to int for comparison
        try:
            guess_int = int(guess) if isinstance(guess, str) else guess
            secret_int = int(secret) if isinstance(secret, str) else secret
            if guess_int > secret_int:
                return "Too High", "📉 Go LOWER!"
            else:
                return "Too Low", "📈 Go HIGHER!"
        except (ValueError, TypeError):
            return "Error", "❌ Comparison failed"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")
