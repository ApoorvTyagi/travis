import unittest
from Arithmatic import Arithmatic

class MyTest(unittest.TestCase):
    def test_arithmatic_function(self):
        obj=Arithmatic(10,5)
        self.assertEqual(obj.add(1,1),11)
        self.assertEqual(obj.sub(),5)
        self.assertEqual(obj.multiply(2,3),10)
        self.assertEqual(obj.divide(),2.0)

if __name__ == '__main__':
    unittest.main() 
