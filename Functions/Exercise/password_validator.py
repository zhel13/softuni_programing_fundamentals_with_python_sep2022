def password_validator (some_password):
    pass_is_valid = []
    if len(some_password) < 6 or len(some_password) > 10:
        pass_is_valid.append("Password must be between 6 and 10 characters")

    if not some_password.isalnum():
        pass_is_valid.append("Password must consist only of letters and digits")

    digit_counter = 0
    for digit in some_password:
        if digit.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        pass_is_valid.append("Password must have at least 2 digits")

    return pass_is_valid


password = input()
password_is_valid = password_validator(password)
if len(password_is_valid) == 0:
    print("Password is valid")
else:
    print("\n".join(password_is_valid))