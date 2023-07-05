import random
import string

def random_string(length):
    """Returns a random string of specified length."""
    characters = string.ascii_letters + string.digits
    random_string = ""
    for _ in range(length):
        random_index = random.randint(0, len(characters) - 1)
        random_string += characters[random_index]

    return random_string

def random_number(length):
    """Returns a random string of specified length."""
    characters = string.digits
    random_string = ""
    for _ in range(length):
        random_index = random.randint(0, len(characters) - 1)
        random_string += characters[random_index]

    return random_string

def random_date():
    month = random.randint(1, 12)
    date = random.randint(1, 28)
    if month < 10:
        month = f"0{month}"
    if date < 10:
        date = f"0{date}"
    return f"{random.randint(1900, 1999)}-{month}-{date}"

def random_email(length):
    """Returns a random email of specified length."""
    return random_string(length) + "@example.com"
