#!/usr/bin/env python3

# Created by: Hertz
# Created on: May,26th, 2022.
# This program asks the user to enter a decimal number and also enters
# a number that represents how many decimals the number should have.


def round_decimal(user_num, num_place):
    user_num[0] = user_num[0] * (10 ** num_place)
    user_num[0] = user_num[0] + 0.5
    user_num[0] = int(user_num[0])
    user_num[0] = user_num[0] / (10 ** num_place)


def main():

    print("This program rounds according to the number of places you enter.")
    print("")

    #  create a list and ask the user to enter a decimal number and
    # how many places they want to round too.
    actual_num = []

    # user input
    dec_places = input("Enter a decimal number:")
    dec_num_place = input("Enter a decimal places to round too:")

    try:
        # convert user inputs into float and integer.
        dec_places_f = float(dec_places)
        dec_num_place_int = int(dec_num_place)
        actual_num.append(dec_places_f)

        # call the function
        round_decimal(actual_num, dec_num_place_int)
        # display the answer to the user
        print("The decimal places is {}.".format(actual_num[0]))

    # how errors will be solved.
    except Exception:
        print("Invalid input, Enter numbers only ")


if __name__ == "__main__":
    main()