"""
Love Formula – Public 30% Release
Educational / Personal / Research Use Only
Commercial use requires a paid license under the Trauma-Aligned License (TAL).

This version contains:
- Basic love/harsh keyword scoring
- Normalised single-value love_score output
- No advanced pattern analysis
- No relational modelling
- No escalation prediction
- No override systems
"""

import re

# ------------------------------------------------------------
# 1. Keyword sets (simplified for safety)
# ------------------------------------------------------------

POSITIVE_KEYWORDS = [
    "love", "kind", "thank", "thanks", "thank you", "grateful",
    "appreciate", "respect", "caring", "care", "support",
    "understand", "sorry", "apologise", "apologize",
    "compassion", "peace", "calm"
]

NEGATIVE_KEYWORDS = [
    "hate", "stupid", "idiot", "dumb", "shut up", "piss off",
    "kill", "hurt", "harm", "worthless", "loser",
    "angry", "fuck you", "f off", "bitch"
]

# ------------------------------------------------------------
# 2. Helper functions
# ------------------------------------------------------------

def count_matches(text: str, keywords: list) -> int:
    """
    Counts occurrences of each keyword in the given text.
    Case-insensitive, simple matching.
    """
    text = text.lower()
    count = 0
    for kw in keywords:
        # use regex word boundaries where appropriate
        pattern = r"\b" + re.escape(kw) + r"\b"
        matches = re.findall(pattern, text)
        count += len(matches)
    return count


# ------------------------------------------------------------
# 3. Main scoring function (public mode)
# ------------------------------------------------------------

def love_score(text: str) -> dict:
    """
    Returns a single scalar love_score between 0.0 and 1.0.
    This is a simplified educational version.

    Output:
        {
            "love_score": <float>
        }
    """

    if not isinstance(text, str):
        raise ValueError("Input must be a string.")

    # Count positive and negative signals
    pos = count_matches(text, POSITIVE_KEYWORDS)
    neg = count_matches(text, NEGATIVE_KEYWORDS)

    # Raw score: positive minus negative
    raw = pos - neg

    # Normalise into 0 → 1
    # raw will be converted into -1 → +1 range, then mapped to 0 → 1
    normalised = (raw + 1) / 2

    # Bound it safely
    love_val = max(0.0, min(1.0, normalised))

    return {"love_score": round(love_val, 4)}


# ------------------------------------------------------------
# 4. Example usage (for developers running locally)
# ------------------------------------------------------------
if __name__ == "__main__":
    example = "Thank you for helping me. I really appreciate your time."
    print(love_score(example))


---
