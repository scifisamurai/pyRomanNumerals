from unittest import TestCase, TestProgram #unit testing framework
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

	def test_convert_9_to_roman(self):
		self.assertEquals("IX",main.to_roman(9))       

	def test_convert_12_to_roman(self):
		self.assertEquals("XII",main.to_roman(12))       

	def test_convert_14_to_roman(self):
		self.assertEquals("XIV",main.to_roman(14))       

	def test_convert_25_to_roman(self):
		self.assertEquals("XXV",main.to_roman(25))       

	def test_convert_44_to_roman(self):
		self.assertEquals("XXXXIV",main.to_roman(44))       

	def test_convert_48_to_roman(self):
		self.assertEquals("XXXXVIII",main.to_roman(48))       

    
if __name__ == "__main__":
	runTests=TestProgram
	runTests()
