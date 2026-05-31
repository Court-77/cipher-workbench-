from collections import Counter
import string

# Frequency analysis
def letter_frequencies(text):
    letters = [
        c.upper()
        for c in text
        if c.upper() in string.ascii_uppercase
    ]

    total = len(letters)
    if total == 0:
        return {}

    counts = Counter(letters)

    return {
        letter: (counts[letter] / total) * 100
        for letter in string.ascii_uppercase
    }
