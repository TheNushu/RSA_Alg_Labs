import unittest
from rsa_functionality import (
    generate_n_bit_random,
    gen_prime_candidate,
    FIRST_PRIMES_LIST,
    is_miller_rabin_passed,
    generate_keys,
    generate_prime,
    encrypt_message,
    decrypt_message
)

BITS = [16, 256, 512, 1024]

class TestRSAGeneration(unittest.TestCase):
    """Unit tests for RSA key generation and encryption functionality."""


    def test_gen_prime_candidate(self):
        """Test the generation of low-level prime numbers."""

        for bit in BITS:
            prime = gen_prime_candidate(bit)
            self.assertTrue(
                prime.bit_length() == bit,
                f"Failed for bit length: {bit}. Number has {prime.bit_length()} bits instead of {bit} bits."
            )            
            self.assertFalse(
                any(prime % p == 0 for p in FIRST_PRIMES_LIST if p**2 <= prime),
                "Generated number is divisible by one of the first primeslist"
            )

    def test_n_bit_random(self):
        """Test random number generation for various bit lengths."""
        # Test with valid inputs
        for bit in BITS:
            rand_num = generate_n_bit_random(bit)
            self.assertTrue(
                rand_num.bit_length() == bit,
                f"Failed for bit length: {bit}. Number has {rand_num.bit_length()} bits instead of {bit} bits."
            )
            self.assertIsInstance(rand_num, int)

    def test_miller_rabin(self):
        """Test if miller-rabin test outputs correctly for known primes/non-primes."""
        primes= [101,
                 2147483647,
                 100000004749,
                 24815323469403931728221172233738523533528335161133543380459461440894543366372904768334987264000000000000000000479,
                 10087577085940592356303078810544350121448766862904157167685249650430861947610081469946840264231795756657844594725521669390990363837279858535929119048375573]

        non_primes= [87,
                     98764321234,
                     12358848653920354053021237345,
                     1235884865392035405302123734711111111111111111111111111111111111111111257,
                     10087577085940592356303078810544350121448766862904157167685249650430861947610081469946840264231795756657844594725521669390990363837279858535929119048375575]

        for prime in primes:
            self.assertTrue(is_miller_rabin_passed(prime),
                            f"{prime} should be prime")

        for non_prime in non_primes:
            self.assertFalse(is_miller_rabin_passed(non_prime),
                             f"{non_prime} should not be prime")

    def test_generate_prime(self):
        for bit in BITS:
            prime = generate_prime(bit)
            self.assertTrue(
                prime.bit_length() == bit,
                f"Failed for bit length: {bit}. Number has {prime.bit_length()} bits instead of {bit} bits."
            )             
            self.assertTrue(is_miller_rabin_passed(prime),
                            f"{prime} should be prime")
            self.assertEqual(prime.bit_length(), bit,
                             f"{prime} should have {bit} bits")

            another_prime = generate_prime(bit)
            self.assertFalse(is_miller_rabin_passed(prime * another_prime),
                             f"{prime * another_prime} should not be considered prime")

    def test_encryption_decryption(self):
        message = "Test message 12!.'s@[]"
        message_encrypt_bin = 347483515112933712292600995212162902755187981752939550
        for bit in BITS:
            public_key, private_key = generate_keys(bit)

            _, modulus_n = public_key
            if bit <= modulus_n.bit_length():
                with self.assertRaises(ValueError, msg="Encryption/Decription should not be possible with keys that are too small for a message."):
                    encrypt_message(message, public_key)
                    #decrypt should only raise value error because the key will be too small
                    #but this should not be possible to decrypt because the binary message
                    #is a result of encryption with a specific key
                    decrypt_message(message_encrypt_bin, private_key)
            else:
                encrypted = encrypt_message(message, public_key)
                decrypted = decrypt_message(encrypted, private_key)
                self.assertEqual(
                    decrypted, message,
                    f"Decrypted message does not match the original"
                )

    def test_generate_keys(self):
        with self.assertRaises(ValueError):
            generate_keys(7)
        with self.assertRaises(TypeError):
            generate_keys("text")
        with self.assertRaises(TypeError):
            generate_keys(39.5)
        for desired_bit in BITS:
            public_key, private_key = generate_keys(desired_bit)
            public_exponent, modulus_n = public_key
            private_exponent, _ = private_key

            self.assertEqual(public_exponent, 65537, "Public exponent e is not 65537")
            self.assertGreaterEqual(modulus_n.bit_length(),
                            desired_bit,
                            f"Modulus n is not at least {desired_bit} bits in length")

            priv_exponent_bits = private_exponent.bit_length()
            diff_bits = priv_exponent_bits - desired_bit
            #chose margin error for private exponent bits
            #its not always exactly desire_bits length
            #because of different multiplications and the
            #multiplicative inverse method

            #we check if its abnormally different
            bit_margin_error = 0.1 * desired_bit
            if bit_margin_error <= 12:
                bit_margin_error = 12

            self.assertTrue(desired_bit - bit_margin_error <= priv_exponent_bits <= desired_bit + bit_margin_error,
                            f"The private exponent is more or less than {desired_bit} bits by {abs(diff_bits)} bits.")

#23.06.24 05:52 am: coverage report 89%

if __name__ == '__main__':
    unittest.main()