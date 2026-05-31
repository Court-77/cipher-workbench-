# Cipher Workbench 🔐

A Python-based cryptanalysis toolkit for breaking classical ciphers using frequency analysis and statistical scoring.

## Overview

This project explores classical cryptography by building tools that can:
- Analyze letter frequency distributions
- Score plaintext likelihood using chi-squared statistics
- Brute-force Caesar cipher encryption
- Rank candidate decryptions automatically

It demonstrates how statistical patterns in language can be used to break simple substitution ciphers without knowing the key.

---

## Features

### 🔎 Frequency Analysis
Extracts and analyzes letter frequency distributions from text.

### 📊 Chi-Squared Scoring
Measures how closely a text matches expected English letter frequencies.

### 🔓 Caesar Cipher Attack
- Tries all 26 possible shifts
- Decrypts each possibility
- Scores each result
- Returns the most likely plaintext

---

## Example

Input ciphertext:
LXFOPVEFRNHR

Output:
Shift 13 | Score 26.16 | YKSBCIRSEAUE
Shift 23 | Score 42.18 | ATTACKATDAWN


Best guess is ranked by lowest chi-squared score.

---

## How to Run

```bash
python main.py


## What I Learned
- Frequency analysis in cryptography
- Statistical language modeling
- Brute-force key search techniques
- Python modular program structure

## Future Improvements
- Vigenère cipher breaking
- Automatic cipher type detection
- Better plaintext scoring using n-grams
- CLI interface


## Disclaimer
This project is for educational purposes exploring classical cryptography techniques.
