import re

def check_password_strength(password):
    """
    Checks the strength of a password based on defined criteria.

    :param password: The password string to be checked.
    :return: Boolean value indicating whether the password meets the criteria.
    """
    # Minimum length of 8 characters
    if len(password) < 8:
        return False

    # Contains both uppercase and lowercase letters
    if not re.search(r'[A-Z]', password) or not re.search(r'[a-z]', password):
        return False

    # Contains at least one digit (0-9)
    if not re.search(r'\d', password):
        return False

    # Contains at least one special character (!, @, #, $, %, etc.)
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False

    return True


if __name__ == "__main__":
    # Get password input from the user
    password = input("Enter a password to check its strength: ")

    # Check the password strength
    if check_password_strength(password):
        print("Your password is strong! 👍")
    else:
        print("Your password is weak. Make sure it is at least 8 characters long, "
              "contains uppercase and lowercase letters, has at least one digit, "
              "and includes at least one special character.")
