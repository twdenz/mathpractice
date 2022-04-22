#!/usr/bin/env python3

import random
import time


def askNum(text: str):
    """Returns an integer from input using 'text'. Loops until valid input given."""
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Incorrect Input!")


def calc(a: int, ops: str, b: int):
    """Returns integer operation result from using : 'a','ops','b'"""
    if ops == "+":
        return a + b
    elif ops == "-":
        return a - b
    elif ops == "*":
        return a * b
    elif ops == "/":
        return a // b  # integer division
    else:
        raise ValueError("Unsupported math operation")


def wrong_answer(wrong_answers: list):
    """Returns the correction of all wrong questions."""
    print(f"You have {len(wrong_answers)} wrong answers")
    for wrong_answer in wrong_answers:
        print(wrong_answer)


total: int = 3
ONE_MIN_NUM = 2
THREE_NUM_MAX = 499
TWO_NUM_MAX = 99

correct: int = 0
start_time = time.time()
wrong_answers = []
for _ in range(total):
    ops = random.choice("+-*/")
    a = random.randint(ONE_MIN_NUM, THREE_NUM_MAX)
    b = random.randint(ONE_MIN_NUM, TWO_NUM_MAX)

    # you only allow integer input - your division therefore is limited to results that are integers - make sure that this is the case here by rerolling a,b until they match
    while ops == "/" and (a % b != 0 or a <= b):
        a = random.randint(ONE_MIN_NUM, THREE_NUM_MAX)
        b = random.randint(2, TWO_NUM_MAX)

    # make sure not to go below 0 for -
    while ops == "-" and a < b:
        a = random.randint(ONE_MIN_NUM, THREE_NUM_MAX)
        b = random.randint(ONE_MIN_NUM, TWO_NUM_MAX)

    # make sure to not multiple too big of numbers
    if ops == "*":
        a = random.randint(ONE_MIN_NUM, TWO_NUM_MAX)
        b = random.randint(ONE_MIN_NUM, 9)
    # as a formatted text
    result = askNum(f"\n{a} {ops} {b} =\n")

    # calculate correct result
    corr = calc(a, ops, b)
    if result == corr:
        correct += 1
    else:
        wrong_answers.append(f"Correction: {a} {ops} {b} = {calc(a, ops, b)}")


end_time = time.time()
total_time = round((end_time - start_time), 2)
perc_correct = round((correct / total) * 100, 1)
print(f"\nYou have {perc_correct}% correct in {total_time} seconds.\n")
wrong_answer(wrong_answers)
