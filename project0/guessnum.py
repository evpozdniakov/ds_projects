"""Simple algorithm to guess a number.

Module exposes functions:
- guess_number(number_to_guess: int) -> int
- guess_number_user_test()

Function guess_number_user_test runs automatically
if you call the module directly.
"""


import numpy as np


def guess_number(number_to_guess: int) -> int:
    """Predicts the number with least number of attempts.

    The received number_to_guess is an integer from 1 to 100. Function
    makes repetitive attempts to guess the value of number_to_guess,
    improving itself on each try. (To improve itself it uses hints:
    was the last guess greater or less than the seeking value.) And it
    counts the attempts.

    Function works until it finds the number_to_guess.
    It returns the number of attempts needed.

    Args:
        number_to_guess (int): Some integer from 1 to 100.

    Raises:
        AssertionError: If number_to_guess is not an integer from 1 to 100.

    Returns:
        int: Number of attempts to guess the value of number_to_guess
    """
    assert(type(number_to_guess) is int)
    assert(1 <= number_to_guess <= 100)

    possible_min = 1
    possible_max = 100
    attempts = 0

    while True:
        attempts += 1
        guess = (possible_max - possible_min) // 2 + possible_min

        if guess < number_to_guess:
            possible_min = guess
        elif guess > number_to_guess:
            possible_max = guess
        else:
            return attempts


def guess_number_user_test():
    """Tests out the function guess_number."""
    while True:
        user_input_str = input('\n\nEnter a number from 1 to 100\n\n')

        if not user_input_str.isdigit():
            print("\n\nThe value entered doesn't look like an integer")
        elif not (1 <= int(user_input_str) <= 100):
            print("\n\nThe integer entered is outside of allowed range.")
        else:
            user_input_int = int(user_input_str)
            attempts = guess_number(user_input_int)

            print(f'\n\nI found it in {attempts} attempts\n\n')
            break


def guess_number_mean_test() -> float:
    """Runs guess_number function 10000 times
    and returns average number of attempts.

    Returns:
        float: Average number of attempts needed to guess number.
    """
    random_numbers = [np.random.randint(1, 100) for x in range(0, 10000)]

    attempts_list = []

    for n in random_numbers:
        a = guess_number(n)
        attempts_list.append(a)

    return np.mean(attempts_list)


if __name__ == '__main__':
    guess_number_user_test()
