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


class TestRSAGeneration(unittest.TestCase):
    """Unit tests for RSA key generation and encryption functionality."""

    def test_n_bit_random(self):
        """Test random number generation for various bit lengths."""
        BITS = [2, 4, 256, 512]
        for n in BITS:
            rand_num = generate_n_bit_random(n)
            self.assertTrue(
                2**(n-1) <= rand_num < 2**n,
                f"Failed for bit length: {n}"
            )

    def test_low_level_prime_generation(self):
        """Test the generation of low-level prime numbers."""
        prime = get_low_level_prime(1024)
        self.assertFalse(
            any(prime % p == 0 for p in FIRST_PRIMES_LIST if p**2 <= prime),
            "Generated number is divisible by one of the first primes list"
        )

    def test_miller_rabin(self):
        self.assertTrue(is_miller_rabin_passed(101), "101 should be prime")
        self.assertFalse(is_miller_rabin_passed(100), "100 should not be prime")

    def test_generate_prime(self):
        prime = generate_prime(20)
        self.assertTrue(is_miller_rabin_passed(prime), "Generated number should be prime")

    def test_generate_keys(self):
        public_key, private_key = generate_keys()
        e, n = public_key
        d, _ = private_key
        phi_n = n - (e * d % n)
        self.assertEqual(
            e * d % phi_n, 1,
            "Public and private keys are not inverses modulo φ(n)"
        )

    def test_encryption_decryption(self):
        message = "Test message"
        public_key, private_key = generate_keys()
        encrypted = encrypt_message(message, public_key)
        decrypted = decrypt_message(encrypted, private_key)
        self.assertEqual(
            decrypted, message,
            "Decrypted message does not match the original"
        )

    def test_input_validations(self):
        with self.assertRaises(ValueError):
            generate_n_bit_random(-1)  # Test negative bit length
        with self.assertRaises(TypeError):
            encrypt_message(12345, (65537, 99991))  # Non-string message input


if __name__ == '__main__':
    unittest.main()
