#!/usr/bin/env python3

import random
import time

def askNum(text):
    """Returns an integer from input using 'text'. Loops until valid input given."""
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Incorrect Input!")

def calc(a,ops,b):
    """Returns integer operation result from using : 'a','ops','b'"""
    if ops == "+": 
        return a+b
    elif ops == "-": 
        return a-b
    elif ops == "*": 
        return a*b
    elif ops == "/": 
        return a//b   # integer division
    else: 
        raise ValueError("Unsupported math operation")

total = 5
correct = 0
start_time = time.time()
for _ in range(total):
    ops = random.choice("+-*/")
    a = random.randint(1,499)
    b = random.randint(1,99)

    # you only allow integer input - your division therefore is
    # limited to results that are integers - make sure that this
    # is the case here by rerolling a,b until they match
    while ops == "/" and (a%b != 0 or a<=b):
        a = random.randint(1,499)
        b = random.randint(2,99)

    # make sure not to go below 0 for -
    while ops == "-" and a<b:
        a = random.randint(1,499)
        b = random.randint(1,99)

    # make sure to not multiple too big of numbers
    if ops == "*":
        a = random.randint(1,99)
        b = random.randint(1,9)
    # as a formatted text 
    result = askNum(f"{a} {ops} {b} =\n")

    # calculate correct result
    corr = calc(a,ops,b)
    if  result == corr:
        correct += 1
        print("Correct")
    else:
        print(f"Wrong. Correct solution is: {a} {ops} {b} = {corr}")

end_time = time.time()
print(f"You have {(correct/total)*100}% correct in {round((end_time-start_time),2)} seconds.")

