import string
import secrets

def generate_password(length: int = 15):
    safe_punctuation = "!@#$%^&*"
    chars = string.ascii_letters + string.digits + safe_punctuation
    password = ''.join(secrets.choice(chars) for i in range(length))
    return password

password = generate_password()
print("Generated password: " + password)