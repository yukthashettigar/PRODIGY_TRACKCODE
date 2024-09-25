import re

def assess_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password is too short. It should be at least 8 characters.")
    else:
        strength += 1

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for numbers
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")

    # Check for special characters
    if re.search(r"\W", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Provide feedback
    if strength == 5:
        return "Password is strong!", feedback
    elif strength >= 3:
        return "Password is medium strength.", feedback
    else:
        return "Password is weak.", feedback

password = input("Enter a password: ")
strength, feedback = assess_password_strength(password)
print(strength)
for item in feedback:
    print(item)
