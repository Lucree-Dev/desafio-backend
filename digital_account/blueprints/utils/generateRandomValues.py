import string
import random


def generate_char_and_number_random(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def randomic_letters_uppercase(length: int) -> str:
    """
    This method do a randomic letter with uppercase. You can choise a quantity of letters to create it.
    :lenth: The lenght to create a quantity of letters.
    :return: It will return a STRING will all random letters.
    """
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(length))


def random_float_number() -> float:
    """
    This method create a random float number.
    :return: it return a float.
    """
    return random.uniform(1, 100)


def generate_random_number(length):
    """
    That method will generate a random numbers.

    :param length: The lenght of number to generate.
    :return: It return the random number.
    """
    return int(''.join([str(random.randint(0,10)) for _ in range(length)]))