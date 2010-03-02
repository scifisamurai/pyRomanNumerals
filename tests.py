#from unittest import TestCase, main
from unittest import TestCase, TestProgram
#from unittest import TestCase #testing framework
import main #code being testing

class TestConvertToRoman(TestCase):
	def test_convert_1_to_roman(self):
		self.assertEquals("I", main.to_roman(1))

	def test_convert_2_to_roman(self):
		self.assertEquals("II",main.to_roman(2))

	def test_convert_3_to_roman(self):
		self.assertEquals("III",main.to_roman(3))

	def test_convert_4_to_roman(self):
		self.assertEquals("IV",main.to_roman(4))

	def test_convert_5_to_roman(self):
		self.assertEquals("V",main.to_roman(5)) 

	def test_convert_8_to_roman(self):
		self.assertEquals("VIII",main.to_roman(8))       

#def doIt(self):
    
if __name__ == "__main__":
	#doIt
	c=TestProgram
	c()
#	main()
