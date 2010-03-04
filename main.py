#!/usr/bin/env python
import tests #our unit tests

def to_roman(number):
	strRomanValue = "" 

	iQuotient, iRemainder = divmod(number, 10)
	if iQuotient >= 1:
		strRomanValue = iQuotient*"X"
	elif iRemainder+1 == 10:
		strRomanValue = "IX"
	if iRemainder+1 < 10:
		iQuotient, iRemainder = divmod(iRemainder, 5)

	if iQuotient == 1:
		strRomanValue = strRomanValue + "V"
	elif iRemainder+1 == 5:
		strRomanValue = strRomanValue + "IV"
	if iRemainder+1 < 5:
		strRomanValue =  strRomanValue + iRemainder * "I"

	return strRomanValue

if __name__ == "__main__":
	runTests=tests.TestProgram
	runTests(module='tests') #run our tests
