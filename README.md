```markdown
# Python Password Generator

A simple, secure password generator written in Python.  
It creates random passwords that always include at least one uppercase letter, one lowercase letter, one digit, and one punctuation character.

## Features

- Uses Python's `secrets` module and `SystemRandom` for cryptographically strong randomness.
- Enforces a minimum password length of 8 characters.
- Guarantees at least one uppercase, one lowercase, one digit, and one punctuation character.
- Shuffles characters so the required character types are not always at the start.

## How it works

The `password_generator(length: int = 16) -> str` function:

1. Checks that `length` is at least 8 and raises a `ValueError` otherwise.  
2. Picks one character from each character set (uppercase, lowercase, digits, punctuation).  
3. Fills the remaining length with random characters from all allowed sets.  
4. Shuffles the list of characters using `SystemRandom` and returns it as a string.

This project uses Python's `secrets` module, which is designed for generating cryptographically strong random numbers suitable for managing passwords and tokens. [web:94]

## Requirements

- Python 3.x

No third‑party dependencies are required; only the Python standard library is used (`secrets` and `string`).

## Usage

1. Clone the repository:

   ```
   git clone https://github.com/uvsser/Python-Password-Generator.git
   cd Python-Password-Generator
   ```

2. Run the script from the command line (example):

   ```
   python main.py
   ```

3. Or import the function into another script:

   ```
   from main import password_generator

   print(password_generator(16))
   ```
