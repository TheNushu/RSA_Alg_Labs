import unittest
from rsa_functionality import (
    generate_n_bit_random,
    get_low_level_prime,
    FIRST_PRIMES_LIST,
    is_miller_rabin_passed,
    generate_keys,
    generate_prime,
    encrypt_message,
    decrypt_message
)

bits = [4, 256, 512, 1024]

class TestRSAGeneration(unittest.TestCase):
    """Unit tests for RSA key generation and encryption functionality."""

    def test_n_bit_random(self):
        """Test random number generation for various bit lengths."""
        for n in bits:
            rand_num = generate_n_bit_random(n)
            self.assertTrue(
                2**(n-1) <= rand_num < 2**n,
                f"Failed for bit length: {n}. Number has {rand_num.bit_length()} bits instead of {n} bits."
            )

    def test_low_level_prime_generation(self):
        """Test the generation of low-level prime numbers."""

        for n in bits:
            prime = get_low_level_prime(n)
            self.assertFalse(
                any(prime % p == 0 for p in FIRST_PRIMES_LIST if p**2 <= prime),
                "Generated number is divisible by one of the first primeslist"
            )

    def test_miller_rabin(self):
        """Test if miller-rabin test outputs correctly for known primes/non-primes."""
        primes= [101,
                 2147483647,
                 100000004749,
                 24815323469403931728221172233738523533528335161133543380459461440894543366372904768334987264000000000000000000479,
                ]

        non_primes= [87,
                     98764321234,
                     12358848653920354053021237345,
                     1235884865392035405302123734711111111111111111111111111111111111111111257]

        for prime in primes:
            self.assertTrue(is_miller_rabin_passed(prime),
                            f"{prime} should be prime")

        for non_prime in non_primes:
            self.assertFalse(is_miller_rabin_passed(non_prime),
                             f"{non_prime} should not be prime")

    def test_generate_prime(self):
        bits = [32, 128, 512]

        for n in bits:
            prime = generate_prime(n)
            self.assertTrue(is_miller_rabin_passed(prime),
                            f"{prime} should be prime")
            self.assertEqual(prime.bit_length(), n,
                             f"{prime} should have {n} bits")
            another_prime = generate_prime(n)
            self.assertFalse(is_miller_rabin_passed(prime * another_prime),
                             f"{prime*another_prime} should not be considered prime")

    def test_encryption_decryption(self):
        message = "Test message 12!.'s@[]"
        public_key, private_key = generate_keys(1024)
        encrypted = encrypt_message(message, public_key)
        decrypted = decrypt_message(encrypted, private_key)
        self.assertEqual(
            decrypted, message,
            "Decrypted message does not match the original"
        )

    def test_input_validations(self):
        with self.assertRaises(ValueError):
            generate_n_bit_random(-1)  # Test negative bit length
        with self.assertRaises(TypeError, msg="encrypt should fail on inproper input"):
            encrypt_message(12345, (65537, 99991))  # Non-string message input
            encrypt_message("Meow", "Woof") # Non-tuple public key
            encrypt_message("Meow", ("Woof", "Quack")) # Non-int key
            encrypt_message("", (65537, 99991))  # Empty string

            decrypt_message("Meow", "Woof") # Non-tuple public key
            decrypt_message("Meow", ("Woof", "Quack")) # Non-int key
            decrypt_message("", (65537, 99991)) # Empty string
    
    def test_generate_keys(self):

        for b in bits:
            public_key, private_key = generate_keys(b)
            e, n = public_key
            d, _ = private_key

            self.assertEqual(e, 65537, "Public exponent e is not 65537")
            self.assertGreaterEqual(n.bit_length(),
                            b,
                            "Modulus n is not {b} bits in length")
            self.assertTrue(d.bit_length() >= b, 
                            f"Private exponent d should be at least {b} bits, got {d.bit_length()} bits. {n.bit_length()}")

#23.06.24 05:52 am: coverage report 89%

if __name__ == '__main__':
    unittest.main()
