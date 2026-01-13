import random
import string

def generate_password(length=12):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]

    all_chars = lowercase + uppercase + digits
    for _ in range(length - 3):
        password_chars.append(random.choice(all_chars))

    random.shuffle(password_chars)

    return ''.join(password_chars)

password = generate_password(12)
print(password)
