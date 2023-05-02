from random import randint


def get_random_password(length=8):
    result = ""
    count = 0
    while count < length:
        random_symbol = chr(randint(40, 126))
        result = result + random_symbol
        count = count + 1
    return result


def is_valid_password(password):
    has_upper = False
    has_lower = False
    has_num = False
    for ch in password:
        if "A" <= ch <= "Z":
            has_upper = True
        elif "a" <= ch <= "z":
            has_lower = True
        elif "0" <= ch <= "9":
            has_num = True
    if len(password) >= 8 and has_upper and has_lower and has_num:
        return True
    return False


def get_password():
    while True:
        password = get_random_password()
        if is_valid_password(password):
            return password
