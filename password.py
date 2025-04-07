password = input("Введите  пароль: ")


def is_very_long(password):
    if len(password) > 12:
        return True


def has_digit(password):
    has_digit = any(i.isdigit()for i in password)
    if has_digit:
        return True


def has_upper_letters(password):
    has_upper_letters = any(i.isupper()for i in password)
    if has_upper_letters:
        return True


def has_lower_letters(password):
    has_lower_letters = any(i.islower()for i in password)
    if has_lower_letters:
        return True


def has_symbols(password):
    has_symbols = any(not i.isdigit() and not i.isalpha()for i in password)
    if has_symbols:
        return True


score = 0
list_foo = [has_digit, is_very_long, has_lower_letters,
            has_upper_letters, has_symbols]

for foo in list_foo:
    if foo(password):
        score += 2
print("Рейтинг пароля: ", score)
