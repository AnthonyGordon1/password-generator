import string
import secrets

# Use secrets module for cryptographic security
def generate_password(length: int = 15):
    #Use safe punctuation
    safe_punctuation = "!@#$%^&*"
    chars = string.ascii_letters + string.digits + safe_punctuation

    #Use at least one of the char types
    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(safe_punctuation),
    ]
    
    #Fill in the rest randomly
    password += [secrets.choice(chars) for i in range(length - 4)]

    #Shuffle around characters for more randomization
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

password = generate_password()
print("Generated password: " + password)