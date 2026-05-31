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
