from secrets import choice, SystemRandom
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, punctuation

def password_generator(length: int = 16) -> str:
    # Enforce a minimum length of 8
    if length < 8:
        raise ValueError('Password length must be at least 8')
    else:
        # Enforcing at least one upper, lower, digit, and punctuation character
        password = [
            choice(ascii_uppercase), 
            choice(ascii_lowercase), 
            choice(digits), 
            choice(punctuation)
            ]
        
        # Fill remaining length
        source = ascii_letters + digits + punctuation
        password += [choice(source) for _ in range(length-4)]
        
        # We shuffle the list using SystemRandom, 
        # This prevents the first 4 characters from always being the required types.
        SystemRandom().shuffle(password)
        
    # Convert the list of characters back into a single string
    return ''.join(password)