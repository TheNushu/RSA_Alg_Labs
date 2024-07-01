"""
This module contains unit tests for verifying the functionality of RSA encryption, decryption,
and key generation of the file rsa_functionality.py

The tests cover several core components of an RSA module which includes:
- Generating random integers with a specified bit length.
- Generating prime number candidates and verifying their primality using the Miller-Rabin test.
- Generating RSA key pairs (public and private keys).
- Encrypting and decrypting messages using RSA keys.
- Input validation across various functions to ensure robustness against
incorrect data types and values.

Tests are parameterized to assess behavior across a variety of bit lengths significant in
RSA contexts, such as 16, 256, 512, and 1024 bits. Each function's behavior is
verified under expected operational conditions to ensure it meets the requirements
for secure and efficient RSA operations.

The tests also include checks for exception handling to manage invalid inputs appropriately.

The test coverage aims to confirm the correctness of the implemented RSA algorithms
and the reliability of the system under various scenarios. 

Usage:
    Run this module directly with a Python interpreter to execute all tests,
    or use it as part of a larger test suite to assess RSA implementations.

Example:
    python3 -m unittest rsa_functionality_tests.py
"""


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

#rudimentary form of parametrised testing
#bit sizes relevant to testing
BITS = [16, 256, 512, 1024]

class TestRSAGeneration(unittest.TestCase):
    """Unit tests for RSA key generation and encryption functionality."""

    def test_gen_prime_candidate(self):
        """
        Test the generation of prime number candidates.

        Validates that the generated number has the correct bit length and is not divisible by
        any small prime number up to its square root.
        """
        for bit in BITS:
            prime = gen_prime_candidate(bit)
            self.assertTrue(
                prime.bit_length() == bit,
                f"Failed for bit length: {bit}. Number has {prime.bit_length()}"
                f"bits instead of {bit} bits."
            )
            self.assertFalse(
                any(prime % p == 0 for p in FIRST_PRIMES_LIST if p**2 <= prime),
                "Generated number is divisible by one of the first primeslist"
            )

    def test_n_bit_random(self):
        """
        Checks that the random generated number has the expected bit length.
        """
        for bit in BITS:
            rand_num = generate_n_bit_random(bit)
            self.assertTrue(
                rand_num.bit_length() == bit,
                f"Failed for bit length: {bit}."
                f"Number has {rand_num.bit_length()} bits instead of {bit} bits."
            )

    def test_miller_rabin(self):
        """Test the Miller-Rabin primality test implementation.

        Confirms that the function correctly identifies known prime and non-prime numbers.
        """

        primes= [101,
                 2147483647,
                 100000004749,
                 24815323469403931728221172233738523533528335161133543380459461440894543366372904768334987264000000000000000000479,
                 #512 bit prime used in 1024 bit key
                 10087577085940592356303078810544350121448766862904157167685249650430861947610081469946840264231795756657844594725521669390990363837279858535929119048375573]

        non_primes= [87,
                     98764321234,
                     12358848653920354053021237345,
                     1235884865392035405302123734711111111111111111111111111111111111111111257,
                     #512 bit
                     10087577085940592356303078810544350121448766862904157167685249650430861947610081469946840264231795756657844594725521669390990363837279858535929119048375575]

        for prime in primes:
            self.assertTrue(is_miller_rabin_passed(prime),
                            f"{prime} should be prime")

        for non_prime in non_primes:
            self.assertFalse(is_miller_rabin_passed(non_prime),
                             f"{non_prime} should not be prime")

    def test_generate_prime(self):
        """Test the prime number generation.

        Ensures that the generated prime has the correct bit length
        and passes the Miller-Rabin primality test (is prime).
        This is dependent on the test_rabin_miller
        and for the miller rabin function to work correctly.
        """

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
        """
        Test the RSA encryption and decryption processes.

        Validates that encryption and decryption of a message work
        as expected across different key sizes.
        """
        message = "Test message 12!.'s@[]"
        pseudo_encrytpted_message = "61897001964269" # 46 bits
        message_int = int.from_bytes(message.encode('utf-8'), 'big')
        message_bit_length = message_int.bit_length()

        for bit in [256, 512, 1024]:
            public_key, private_key = generate_keys(bit)

            encrypted = encrypt_message(message, public_key)
            decrypted = decrypt_message(encrypted, private_key)
            self.assertEqual(
                decrypted, message,
                "Decrypted message does not match the original"
            )

        public_key, private_key = generate_keys(1024)
        #1024 bit string
        message = "loremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremipsumloremips"
        
        encrypted = encrypt_message(message, public_key)
        decrypted = decrypt_message(encrypted, private_key)
        self.assertEqual(
            decrypted, message,
            "Decrypted 1024 message does not match the original"
        )

        #test edge case of 16 bit key       
        public_key, private_key = generate_keys(16)
        with self.assertRaises(ValueError, msg=f"Message of {message_bit_length} bits "
                                                f"is too big for 16 bits key to encrypt"):
            encrypt_message(message, public_key)
        with self.assertRaises(ValueError, msg=f"Message of {int(message_bit_length).bit_length()} bits"
                                                f" is too big for 16 bits key to decrypt"):
            decrypt_message(pseudo_encrytpted_message, private_key)

    def test_generate_keys(self):
        """
        Test the RSA key generation process to ensure keys are generated with correct properties.

        This test verifies that:
        - The public exponent is set to the commonly used value of 65537.
        - The modulus size is at least as large as the requested bit size.
        - The private exponent is within a reasonable range of the modulus size,
        ensuring it is appropriate for secure encryption and decryption.
        """
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
            bit_margin_error = max(bit_margin_error, 12)

            self.assertTrue(desired_bit - bit_margin_error <= priv_exponent_bits <= desired_bit + bit_margin_error,
                            f"The private exponent is more or less than"
                            f"{desired_bit} bits by {abs(diff_bits)} bits.")

    def test_input_validations(self):
        """
        Test input validation for various RSA functions
        to ensure robustness against incorrect inputs.

        This test checks that:
        - Functions raise appropriate exceptions for invalid inputs such
        as incorrect data types and values,
        ensuring the RSA module handles errors correctly.
        - Encryption and decryption functions specifically check for and
        handle invalid message formats, key formats, and empty inputs,
        preventing misuse and potential security flaws.
        """

        with self.assertRaises(ValueError):
            generate_keys(7)
        with self.assertRaises(TypeError):
            generate_keys("text")
        with self.assertRaises(TypeError):
            generate_keys(39.5)

        with self.assertRaises(ValueError):
            generate_n_bit_random(-1)
        with self.assertRaises(TypeError):
            generate_n_bit_random("text")
        with self.assertRaises(TypeError):
            generate_n_bit_random(39.5)

        with self.assertRaises(ValueError):
            is_miller_rabin_passed(-1)
        with self.assertRaises(TypeError):
            is_miller_rabin_passed("text")
        with self.assertRaises(TypeError):
            is_miller_rabin_passed(39.5)

        with self.assertRaises(TypeError, msg="Encrypt and decrypt should fail on inproper input"):
            encrypt_message(12345, (65537, 99991))  # Non-string message input
        with self.assertRaises(TypeError, msg="Encrypt and decrypt should fail on inproper input"):
            encrypt_message("text1", "text2") # Non-tuple public key
        with self.assertRaises(TypeError, msg="Encrypt and decrypt should fail on inproper input"):
            encrypt_message("text1", ("text2", "text3")) # Non-int key
        with self.assertRaises(TypeError, msg="Encrypt and decrypt should fail on inproper input"):
            encrypt_message("", (65537, 99991))  # Empty string

        with self.assertRaises(TypeError, msg="Encrypt and decrypt should fail on inproper input"):
            decrypt_message("text1", "text2") # Non-tuple public key
        with self.assertRaises(TypeError, msg="Encrypt and decrypt should fail on inproper input"):
            decrypt_message("text1", ("text2", "text3")) # Non-int key
        with self.assertRaises(TypeError, msg="Encrypt and decrypt should fail on inproper input"):
            decrypt_message("", (65537, 99991)) # Empty string

#30.06.24: coverage report 95%

if __name__ == '__main__':
    unittest.main()
