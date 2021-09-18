"""Optimized algorithm to predict a number.

Module exposes functions:
- predict_number_optimized(number_to_guess: int) -> int
- user_test_predict_number_optimized()

Function user_test_predict_number_optimized runs if the module 
is called directly.
"""


def predict_number_optimized(number_to_guess: int) -> int:
    """Predicts the number with least number of attempts.

    The received number_to_guess is an integer from 1 to 100. Function
    makes repetitive attempts to guess the value of number_to_guess,
    improving itself on each try. To improve itself it uses hints:
    was the last guess greater or less than the seeking value.

    It finally returns the number of attempts needed to find the value
    of number_to_guess.

    Args:
        number_to_guess (int): Some integer from 1 to 100.

    Returns:
        int: Number of attempts to predict the value of number_to_guess
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


def user_test_predict_number_optimized():
    """Tests out the function predict_number_optimized."""
    while True:
        user_input_str = input('\n\nEnter a number from 1 to 100\n\n')

        if not user_input_str.isdigit():
            print("\n\nThe value entered doesn't look like an integer")
        elif not (1 <= int(user_input_str) <= 100):
            print("\n\nThe integer entered is outside of allowed range.")
        else:
            user_input_int = int(user_input_str)
            attempts = predict_number_optimized(user_input_int)

            print(f'\n\nI found it in {attempts} attempts\n\n')
            break


if __name__ == '__main__':
    user_test_predict_number_optimized()
