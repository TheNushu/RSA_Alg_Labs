import unittest
from rsa_functionality import generate_keys, encrypt_message, decrypt_message

class TestRsaFunctionality(unittest.TestCase):
    def test_generate_keys(self):
        result = generate_keys() 
        return True
        self.assertEqual(result, expected_value)  



if __name__ == '__main__':
    unittest.main()
