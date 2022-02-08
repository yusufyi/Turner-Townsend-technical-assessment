import unittest


def romanToInt(num):
    romansNum = {'I':1,'V':5,'X':10,'C':100,'M':1000}#Identifying Roman Numbers
    n=0
    val=0
    
    while n < len(num):
        romansNum = {'I':1,'V':5,'X':10,'L':50,'C':100,'M':1000}
        val+=romansNum[num[n]]
        n+=1
    
    return val

        
        

#Unit Test
class TestRomanNumeral(unittest.TestCase):
    def test_default_roman_numerals(self):
        self.assertEqual(10,romanToInt("X"))
        self.assertEqual(6,romanToInt("VI"))
        self.assertEqual(1017,romanToInt("MXVII"))

        
    