#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
    return [max(elem) for elem in numbers]


def join_integers(numbers):
    return int("".join([str(elem) for elem in numbers]))


def generate_prime_numbers(limit):
    premiers = []
    nombres = [i for i in range(2, limit + 1)]
    while len(nombres) != 0:
        premiers.append(nombres[0])
        nombres = [elem for elem in nombres if elem % nombres[0] != 0]
    # for elem in nombres:
    # if elem % nombres != 0:
    # nombres_2.append(elem)
    # nombres = nombres_2

    return premiers


def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
    # ma méthode
    # result = []
    # if excluded_multiples is None:
    # numbers = [i for i in range(1, num_combinations + 1)]
    # else:
    # numbers = [i for i in range(1, num_combinations + 1) if i % excluded_multiples != 0]

    # for i in numbers:
    # for elem in strings:
    # result.append(f"{elem}{i}")

    result = [
        string + str(i)
        for i in range(1, num_combinations + 1)
        if excluded_multiples is None or i % excluded_multiples != 0
        for string in strings
    ]
    #for i in range(1, num_combinations + 1):
        #result += [string + str(i) for string in strings if excluded_multiples is None or i % excluded_multiples != 0]

    return result


if __name__ == "__main__":
    print(get_maximums([[1, 2, 3], [6, 5, 4], [10, 11, 12], [8, 9, 7]]))
    print("")
    print(join_integers([111, 222, 333]))
    print(join_integers([69, 420]))
    print("")
    print(generate_prime_numbers(17))
    print("")
    print(combine_strings_and_numbers(["A", "B"], 2, None))
    print(combine_strings_and_numbers(["A", "B"], 5, 2))
