import string
from analysis import chi_squared_score

ALPHABET = string.ascii_uppercase

# Caesar cipher decryption
def caesar_decrypt(text, shift):
    result = []

    for c in text:
        if c.upper() in ALPHABET:
            idx = ALPHABET.index(c.upper())
            new_idx = (idx - shift) % 26
            result.append(ALPHABET[new_idx])
        else:
            result.append(c)

    return "".join(result)


# Brute-force attack
def crack_caesar(ciphertext):
    candidates = []

    for shift in range(26):
        plaintext = caesar_decrypt(ciphertext, shift)
        score = chi_squared_score(plaintext)

        candidates.append((score, shift, plaintext))

    candidates.sort()
    return candidates
