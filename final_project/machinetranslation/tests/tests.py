import unittest
from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench("Hello"), "Bonjour") 
            
class TEstfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")
            
unittest.main()
