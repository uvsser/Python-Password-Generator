The README below assumes you are using Python 3 and the `secrets` module for cryptographically strong password generation as in your script.[1]

```markdown
# Python Password Generator

A simple, secure password generator written in Python.  
It creates random passwords that always include at least one uppercase letter, one lowercase letter, one digit, and one punctuation character.

## Features

- Uses Python's `secrets` module and `SystemRandom` for security‑sensitive randomness.
- Enforces a minimum password length of 8 characters.
- Guarantees at least one uppercase, one lowercase, one digit, and one punctuation character.
- Shuffles characters so the required character types are not always at the start.
- Includes a modern GUI built with CustomTkinter.

## How it works

The `password_generator(length: int = 16) -> str` function:

1. Checks that `length` is at least 8 and raises a `ValueError` otherwise.  
2. Picks one character from each character set (uppercase, lowercase, digits, punctuation).  
3. Fills the remaining characters with random choices from all allowed sets.  
4. Shuffles the list using `SystemRandom` and returns it as a string.

## Requirements

- Python 3.x
- `customtkinter` (for the GUI)

All other modules used (`secrets`, `string`) are from the Python standard library.

## Installation

Clone the repository and install the dependencies:

```
git clone https://github.com/uvsser/Python-Password-Generator.git
cd Python-Password-Generator
pip install -r requirements.txt
```

## CLI Usage (optional)

You can import and use the generator function directly in Python code:

```
from main import password_generator

print(password_generator(16))
```

Adjust the length argument as needed, but keep it at 8 or higher.

## GUI Usage (optional)

To run the modern GUI:

```
python gui.py
```

Use the slider to choose the password length, click **Generate**, and then click **Copy** to copy the generated password to the clipboard.

## Project Structure

- `main.py` – core password generation logic.
- `gui.py` – CustomTkinter graphical interface for generating and copying passwords.
- `requirements.txt` – list of Python dependencies for the project.
- `README.md` – project documentation (this file).

