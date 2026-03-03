import re
import math


def load_common_passwords(filename: str = "common_passwords.txt") -> set[str]:
    try:
        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            return {line.strip().lower() for line in f if line.strip()}
    except FileNotFoundError:
        return {"password", "123456", "qwerty", "letmein", "admin"}

COMMON_PASSWORDS = load_common_passwords()
def estimate_entropy(password: str) -> float:
    pool = 0
    if re.search(r"[a-z]", password): pool += 26
    if re.search(r"[A-Z]", password): pool += 26
    if re.search(r"\d", password): pool += 10
    if re.search(r"[^A-Za-z0-9]", password): pool += 33  # rough count of common symbols
    if pool == 0:
        return 0.0
    return len(password) * math.log2(pool)

def strength_check(pw: str) -> dict:
    pw_stripped = pw.strip()
    pw_lower = pw_stripped.lower()

    score = 0
    reasons = []
    tips = []

    if len(pw_stripped) == 0:
        return {"score": 0, "label": "Very weak", "reasons": ["Empty password"], "tips": ["Type a password."]}

    if pw_lower in COMMON_PASSWORDS:
        return {
            "score": 0,
            "label": "Very weak",
            "reasons": ["This is a very common password."],
            "tips": ["Use a unique passphrase, e.g., 4+ random words with symbols/numbers."]
        }

    if re.search(r"(.)\1\1", pw_stripped):  # 3 same chars in a row
        reasons.append("Contains repeated characters (e.g., 'aaa').")
        score -= 10
        tips.append("Avoid repeating the same character many times.")

    if re.search(r"(0123|1234|2345|3456|4567|5678|6789)", pw_stripped):
        reasons.append("Contains obvious number sequence (e.g., 1234).")
        score -= 10
        tips.append("Avoid sequences like 1234.")

   
    L = len(pw_stripped)
    if L < 8:
        reasons.append("Too short (< 8).")
        score += 5
        tips.append("Use at least 12 characters (or a passphrase).")
    elif L < 12:
        score += 20
    elif L < 16:
        score += 35
    else:
        score += 45


    has_lower = bool(re.search(r"[a-z]", pw_stripped))
    has_upper = bool(re.search(r"[A-Z]", pw_stripped))
    has_digit = bool(re.search(r"\d", pw_stripped))
    has_symbol = bool(re.search(r"[^A-Za-z0-9]", pw_stripped))

    variety = sum([has_lower, has_upper, has_digit, has_symbol])
    score += variety * 10

    if not has_lower: tips.append("Add lowercase letters.")
    if not has_upper: tips.append("Add uppercase letters.")
    if not has_digit: tips.append("Add digits.")
    if not has_symbol: tips.append("Add symbols (e.g., !@#).")


    ent = estimate_entropy(pw_stripped)
    if ent >= 80:
        score += 15
    elif ent >= 60:
        score += 10
    elif ent >= 40:
        score += 5
    else:
        reasons.append("Low entropy (easy to guess).")
        tips.append("Increase length and mix character types (or use a passphrase).")


    score = max(0, min(100, score))

   
    if score < 25:
        label = "Very weak"
    elif score < 45:
        label = "Weak"
    elif score < 65:
        label = "Okay"
    elif score < 85:
        label = "Strong"
    else:
        label = "Very strong"

   
    seen = set()
    tips_unique = []
    for t in tips:
        if t not in seen:
            tips_unique.append(t)
            seen.add(t)

    return {"score": score, "label": label, "reasons": reasons, "tips": tips_unique}

def strength_bar(score: int, width: int = 25) -> str:
    score = max(0, min(100, int(score)))
    filled = int(round((score / 100) * width))
    empty = width - filled
    return f"[{'█' * filled}{'░' * empty}]"


if __name__ == "__main__":
    pw = input("Enter a password to check strength: ")
    result = strength_check(pw)

    print(f"\nStrength: {result['label']} ({result['score']}/100)" ,strength_bar(result["score"]))
    
    if result["reasons"]:
        print("Reasons:")
        for r in result["reasons"]:
            print(f"- {r}")
    if result["tips"]:
        print("Tips:")
        for t in result["tips"]:
            print(f"- {t}")