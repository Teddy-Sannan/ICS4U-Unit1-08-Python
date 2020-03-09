#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: Februrary
# This program generates 10 numbers from 1-99 and shows the user the lowest
#  value in the list

import random


def main():
    # list of generated numbers
    numbers = []

    # maximum and minimum value
    maximum = 101
    minimum = 0

    # randomly generates numbers
    for digits in range(10):
        digit = random.randint(0, 99)
        numbers.append(digit)

    # loops through list to find maximum and minimum
    for number in numbers:
        if minimum <= number:
            minimum = number

        elif maximum >= number:
            maximum = number

    # prints maximum and minimum
    print(numbers)
    print()
    print("The maximum value is: ", maximum)
    print("The minimum value is: ", minimum)


if __name__ == "__main__":
    main()
