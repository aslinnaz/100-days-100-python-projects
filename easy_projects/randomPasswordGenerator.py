# This program generates a random password of a specified length.

import secrets  #secrets module is used to generate cryptographically strong random numbers.
import string
from passwordStrengthChecker import strength_check

while True:
    try:
        length = int(input("How long do you want your password to be? (At least 6 characters): "))
        if length >= 6:
            break
        print("Password length must be at least 6.")
    except ValueError:
        print("Please enter a valid number.")

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
special = "!@#$%^&*_+-=;:,.?/"

all_chars = uppercase + lowercase + digits + special

password = [
    secrets.choice(uppercase),
    secrets.choice(lowercase),
    secrets.choice(digits),
    secrets.choice(special)
]

password += [secrets.choice(all_chars) for _ in range(length - 4)]

secrets.SystemRandom().shuffle(password)

final_password = ''.join(password)

print("Generated Password:", final_password)

#just for fun, let's also check the strength of the generated password using our strength checker
#the visual bar is cute
def strength_bar(score: int, width: int = 25) -> str:
    score = max(0, min(100, int(score)))
    filled = int(round((score / 100) * width))
    empty = width - filled
    return f"[{'█' * filled}{'░' * empty}] {score}/100"



result = strength_check(final_password)
print(f"Password Strength: {result['label']} ({result['score']}/100)")
print("Strength Bar:", strength_bar(result["score"]))

if result["tips"]:
    print("Improvement Tips:")
    for tip in result["tips"]:
        print("-", tip)