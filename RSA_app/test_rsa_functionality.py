import unittest
from rsa_functionality import n_bit_random, get_low_level_prime, first_primes_list, is_miller_rabin_passed, generate_keys, generate_prime

class TestRSAGeneration(unittest.TestCase):

    def test_n_bit_random(self):
        for n in range(2, 10):  # Testing a variety of bit lengths
            rand_num = n_bit_random(n)
            self.assertTrue(2**(n-1) + 1 <= rand_num < 2**n, f"Failed for bit length: {n}")

    def test_low_level_prime_generation(self):
        # This test might be probabilistic and not assert an exact prime every time
        prime = get_low_level_prime(1024)
        #ERRORS, NEEDS TO BE WORKED ON
        self.assertFalse(any(prime % p == 0 for p in first_primes_list if p**2 <= prime),
                         "Generated number is divisible by one of the first primes list")

    def test_miller_rabin(self):
        # Testing primes and non-primes
        self.assertTrue(is_miller_rabin_passed(101))
        self.assertFalse(is_miller_rabin_passed(100))

    def test_generate_prime(self):
        prime = generate_prime(20)
        self.assertTrue(is_miller_rabin_passed(prime))

    def test_generate_keys(self):
        public_key, private_key = generate_keys()
        self.assertNotEqual(public_key, private_key)
        self.assertTrue(is_miller_rabin_passed(public_key))
        self.assertTrue(is_miller_rabin_passed(private_key))

if __name__ == '__main__':
    unittest.main()
