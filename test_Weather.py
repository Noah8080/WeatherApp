import unittest

from Weather import is_five_digits
class test_is_five_digits(unittest.TestCase):

    def test_valid_input(self):
        result = is_five_digits(12345)
        self.assertTrue(result)
        
    def test_invalid_input(self):
        result = is_five_digits(1234)
        self.assertFalse(result)
    
        
from Weather import test_json_dumps
class test_test_json_dumps(unittest.TestCase):
    
    def test_invalid_string(self):
        result = test_json_dumps("This is not a valid JSON string")
        self.assertFalse(result)
    
    def test_valid_string(self):
        result = test_json_dumps('{"name": "John", "age": 30}')
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
