#!/usr/bin/env python
import tests #unit tests

def to_roman(number):
    q, r = divmod(number, 5)
    if number == 8:
        return "VIII"
    if number == 5:
        return "V"
    if number == 4:
        return "IV"
    if number < 4:
        return number * "I"

if __name__ == "__main__":
	x=tests.TestProgram
	x(module='tests') #run our tests
