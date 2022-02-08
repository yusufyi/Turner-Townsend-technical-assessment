import unittest
import time

def collatz(n):
    timeout = time.time() + 5
    while n != 1:
        if n % 2 == 0 :
            n = n/2
        else:
            n = 3 * n +1
        if time.time() > timeout: #Breake if given variable is 0;
            break
        
    return int(n)      
        



#Unit Test
class TestCollatz(unittest.TestCase):
    
    def test_default_collatz(self):
        self.assertEqual(1,collatz(10))
        self.assertEqual(1,collatz(30))
        self.assertEqual(1,collatz(27))
        self.assertEqual(1,collatz(0))      #We will get error for this

        
    
