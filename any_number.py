#!/usr/bin/env python3

# Created by Devin Jhu
# Created on June 2022
# The rounder


def rounding(number, round_to):
    # rounds the users number to their desired decimal place

    rounded_number = 10**round_to

    number[0] = int(number[0] * rounded_number + 0.5) / rounded_number


def main():
    # Takes user input, passes it to round function,
    # then outputs the rounded number

    number = []

    print("This program rounds numbers")

    # input
    number_input = input("Enter number: ")
    decimal_string = input("Enter decimal points to round to: ")

    # process
    try:
        single_number = float(number_input)
        number.append(single_number)
        decimal = int(decimal_string)

        if decimal >= 0:
            rounding(number, decimal)
            print("\nThe rounded number is {0}".format(number[0]))
        else:
            print("not a number")

    except Exception:
        print("not a number")

    print("\nDone.")


if __name__ == "__main__":
    main()
