"""
This module provides functions for generating RSA keys, encrypting messages,
and decrypting messages using RSA cryptography. It implements the generation
of cryptographically strong prime numbers via the Miller-Rabin primality test
and uses these primes to create RSA public and private key pairs.

Default keys are set to 1024 bits, but the setting can be changed:
- more bits: better security / longer computing
- key bit size = 2 * bit size of the prime numbers (if both are 512 bits, key = 1024)

Functions:
- generate_n_bit_random(bit_length): Generates a random number of specified bit length.
- get_low_level_prime(bit_length):
	Generates a probable prime number not divisible by the first few prime numbers.
- is_miller_rabin_passed(candidate_prime):
Determines if a number is likely prime using the Miller-Rabin test.
- generate_prime(bits): Generates a prime number with a specified number of bits.
- generate_keys(): Generates RSA public and private keys.
- encrypt_message(message, public_key): Encrypts a message using the RSA public key.
- decrypt_message(ciphertext, private_key): Decrypts a message using the RSA private key.

Each function is documented with specific details on their operation and parameters.
"""

import random

# Pre-generated list of small primes to test divisibility for initial prime candidacy checks
FIRST_PRIMES_LIST = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67,
    71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149,
    151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
    233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313,
    317, 331, 337, 347, 349
]


def generate_n_bit_random(bit_length):
    """Generate a random number with a specified bit length."""
    if bit_length < 4:
        raise ValueError("Bit size must be at least 4 to form a valid range")
    
    system_random = random.SystemRandom()
    return system_random.randint(2**(bit_length-1) + 1, 2**bit_length - 1)

def get_low_level_prime(bit_length):
    """Generate a prime candidate not divisible by first primes."""
    while True:
        prime_candidate = generate_n_bit_random(bit_length)
        for divisor in FIRST_PRIMES_LIST:
            if prime_candidate % divisor == 0 and divisor**2 <= prime_candidate:
                break
        else:
            return prime_candidate


def is_miller_rabin_passed(candidate_prime):
    """Perform the Miller-Rabin primality test on a candidate prime number."""
    max_divisions_by_two = 0
    remaining = candidate_prime - 1
    while remaining % 2 == 0:
        remaining >>= 1
        max_divisions_by_two += 1
    assert 2**max_divisions_by_two * remaining == candidate_prime - 1

    def is_composite(test_base):
        """
    	Determine if a number is composite (not prime)
        using the Miller-Rabin primality test conditions.
    	"""
        if pow(test_base, remaining, candidate_prime) == 1:
            return False
        for i in range(max_divisions_by_two):
            if pow(test_base, 2**i * remaining, candidate_prime) == candidate_prime - 1:
                return False
        return True

    for _ in range(20):  # Number of trials
        test_base = random.randrange(2, candidate_prime)
        if is_composite(test_base):
            return False
    return True

def generate_prime(bits):
    """Generate a prime number with a given number of bits."""
    while True:
        prime_candidate = get_low_level_prime(bits)
        if is_miller_rabin_passed(prime_candidate):
            return prime_candidate


def generate_keys(bits):
    """Generate a pair of RSA keys."""
    public_exponent = 65537  # Common choice for public exponent

    while True:
        prime_p = generate_prime(bits // 2 + 8) # if user wants n bit key
        prime_q = generate_prime(bits // 2 + 8) # each prime should be half of that
                                                # add 8 bits to account for loss in
                                                # multiplications
        
        modulus_n = prime_p * prime_q
        phi_n = (prime_p - 1) * (prime_q - 1)
        if phi_n % public_exponent != 0:
            break

    private_exponent = pow(public_exponent, -1, phi_n)
    return (public_exponent, modulus_n), (private_exponent, modulus_n)

def encrypt_message(message, public_key):
    """Encrypt a message using the public key."""
    
    if len(message) <= 0 or str.isspace(message):
        raise ValueError("Message must be non-empty.")    

    if not isinstance(message, str):
        raise TypeError("The message should be a string")
 
    if not isinstance(public_key, tuple) or len(public_key) != 2:
        raise TypeError("The public key must be a tuple of two integers (e, n)")

    public_exponent, modulus_n = public_key
    if not (isinstance(public_exponent, int) and isinstance(modulus_n, int)):
        raise TypeError("Both public exponent and modulus must be integers")

    public_exponent, modulus_n = public_key
    message_int = int.from_bytes(message.encode('utf-8'), 'big')
    ciphertext = pow(message_int, public_exponent, modulus_n)
    return ciphertext

def decrypt_message(ciphertext, private_key):
    """Decrypt a message using the private key."""
    
    string_cipher = str(ciphertext)
    if len(string_cipher) <= 0 or str.isspace(string_cipher):
        raise ValueError("Message must be non-empty.") 

    if not isinstance(private_key, tuple) or len(private_key) != 2:
        raise TypeError("The public key must be a tuple of two integers (e, n)")

    private_exponent, modulus_n = private_key
    if not (isinstance(private_exponent, int) and isinstance(modulus_n, int)):
        raise TypeError("Both public exponent and modulus must be integers")

    message_int = pow(ciphertext, private_exponent, modulus_n)
    message = message_int.to_bytes((message_int.bit_length() + 7) // 8, 'big').decode('utf-8')
    return message
