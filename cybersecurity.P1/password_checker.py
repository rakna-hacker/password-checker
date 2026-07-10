def check_password_strength(password):
    has_upper = False
    has_number = False
    has_symbol = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.isdigit():
            has_number = True
        elif not char.isalnum():
            has_symbol = True

    if len(password) >= 12 and has_upper and has_number and has_symbol:
        return "Strong"
    elif len(password) >= 8 and (has_upper or has_number or has_symbol):
        return "Medium"
    else:
        return "Weak"


password = input("Enter a password: ")
print(check_password_strength(password))