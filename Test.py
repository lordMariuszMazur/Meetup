# Test
import random


def reverse(input=""):
    return str(input)[::-1]


# print("This is: ", reverse("Mammoj"))


def select_password():
    """Selects a password that user needs to guest."""
    passwords = [
        "working",
        "leasure",
        "harder",
        "easier",
        "amazing",
        "australia",
        "kangaroo",
    ]
    print(passwords)  # for test purposes only
    password = passwords[random.randint(0, len(passwords) - 1)]
    print("pass: ", password)
    return password


def get_blank_password(password):
    """Creates a password with first letter visible
    and rest cover by \'_\'."""
    blank_password = password[0]
    for i in range(1, len(password)):
        blank_password += "_"
    print("yep: ", blank_password)


a = select_password()
get_blank_password(a)
