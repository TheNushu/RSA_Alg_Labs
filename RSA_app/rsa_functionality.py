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
- gen_prime_candidate(bit_length):
	Generates a probable prime number not divisible by the first few prime numbers.
- is_miller_rabin_passed(candidate_prime):
Determines if a number is likely prime using the Miller-Rabin test.
- generate_prime(bits): Generates a prime number with a specified number of bits.
- generate_keys(): Generates RSA public and private keys.
- encrypt_message(message, public_key): Encrypts a message using the RSA public key.
- decrypt_message(ciphertext, private_key): Decrypts a message using the RSA private key.
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
    """Generate a random number with a specified bit length.

    Args:
        bit_length (int): bit size of random number

    Returns:
        int: number with bit_length size in bits
    Raises:
        ValueError: If bit size less than 8 or of a different type than int
    """
    if isinstance(bit_length, int) is not True:
        raise ValueError("Bit size must be an integer.")

    if bit_length < 8:
        raise ValueError(f"Bit size must be at least 8 to form "
                         f"a valid value for the keys, got {bit_length}")

    system_random = random.SystemRandom()
    return system_random.randint(2**(bit_length-1) + 1, 2**bit_length - 1)

def gen_prime_candidate(bit_length):
    """Generate a prime candidate not divisible by first primes.

    Args:
        bit_length (int): bit size of prime candidate

    Returns:
        int: random number that is not divisble by the first arbitrary primes
    """

    while True:
        prime_candidate = generate_n_bit_random(bit_length)
        for divisor in FIRST_PRIMES_LIST:
            if prime_candidate % divisor == 0 and divisor**2 <= prime_candidate:
                break
        else:
            return prime_candidate

def is_miller_rabin_passed(candidate_prime):
    """Perform the Miller-Rabin primality test on a candidate prime number.
    
    Args:
        candidate_prime (int): number to be tested with miller rabin test
    
    Returns:
        bool: True if passed as prime, False otherwise
    """
    # note, the check if it is a small prime number
    # is done in gen_prime_candidate()
    if isinstance(candidate_prime, int) is not True:
        raise ValueError("Candidate prime must be an integer.")

    if candidate_prime % 2 == 0:
        return False

    max_divisions_by_two = 0
    remaining = candidate_prime - 1
    while remaining % 2 == 0:
        remaining = remaining // 2
        max_divisions_by_two += 1
    assert 2**max_divisions_by_two * remaining == candidate_prime - 1

    def is_composite(test_base):
        """
    	Determine if candidate_prime (int) is composite/not prime
        using the Miller-Rabin primality test conditions.

        Args:
            test_base (int): base used by miller rabin test in
                             modular exponentiation (line 110)

        Returns:
            bool: True if prime_candidate is likely prime, False otherwise
    	"""
        if pow(test_base, remaining, candidate_prime) == 1:
            return False
        for i in range(max_divisions_by_two):
            if pow(test_base, 2**i * remaining, candidate_prime) == candidate_prime - 1:
                return False
        return True

    system_random = random.SystemRandom()
    for _ in range(20):  # Number of trials
        test_base = system_random.randint(2, candidate_prime - 1)
        if is_composite(test_base):
            return False
    return True

def generate_prime(bits):
    """Generate a prime number with a given number of bits.

    Args:
        bits (int): bit size of prime number to be generated

    Returns:
        int: a prime number with specified bit size
    """
    while True:
        prime_candidate = gen_prime_candidate(bits)
        if is_miller_rabin_passed(prime_candidate):
            return prime_candidate

def generate_keys(bits):
    """Generate a pair of RSA keys.

    Args:
        bits (int): bit sizes of keys

    Returns:
        tuple: A tuple containing the RSA keys:
            - (public_exponent, modulus_n): Public key components.
            - (private_exponent, modulus_n): Private key components.

    Raises:
        TypeError: If `bits` is not an integer.
        ValueError: If `bits` is less than 8.
    """
    public_exponent = 65537  # Common choice for public exponent
    if isinstance(bits, int) is not True:
        raise TypeError("Bit size must be an integer.")

    if bits < 8:
        raise ValueError(f"Bit size must be at least 8 to form "
                         f"a valid value for the keys, got {bits}")
    while True:
        #ensure bit length of modulus as desired
        while True:
            prime_p = generate_prime(bits // 2) # e.g. for a 1024 bit key size
            prime_q = generate_prime(bits // 2) # each prime needs to be 512 bits

            modulus_n = prime_p * prime_q
            if modulus_n.bit_length() == bits:
                break

        phi_n = (prime_p - 1) * (prime_q - 1)
        if phi_n % public_exponent != 0:
            break

    private_exponent = pow(public_exponent, -1, phi_n)
    return (public_exponent, modulus_n), (private_exponent, modulus_n)

def encrypt_message(message, public_key):
    """
    Encrypts a message using the RSA public key.

    Args:
        message (str): The message to be encrypted.
        public_key (tuple): A tuple containing the RSA public key components (e, n):
                            - e (int): Public exponent.
                            - n (int): Modulus.

    Returns:
        int: The encrypted ciphertext.

    Raises:
        TypeError: If `message` is not a string or if `public_key` is not a tuple of two integers.
        ValueError: If `message` is empty or consists only of whitespace,
                    or if the message bit length is greater than or equal to the modulus bit length.
    """

    if len(message) <= 0 or str.isspace(message):
        raise TypeError("Message must be non-empty.")

    if not isinstance(message, str):
        raise TypeError("The message should be a string")

    if not isinstance(public_key, tuple) or len(public_key) != 2:
        raise TypeError("The public key must be a tuple of two integers (e, n)")

    public_exponent, modulus_n = public_key
    if not (isinstance(public_exponent, int) and isinstance(modulus_n, int)):
        raise TypeError("Both public exponent and modulus must be integers")

    modulus_bit_length = modulus_n.bit_length()
    message_int = int.from_bytes(message.encode('utf-8'), 'big')
    message_bit_length = message_int.bit_length()

    # Check if the message bit length is less than the modulus bit length
    if message_bit_length >= modulus_bit_length:
        raise ValueError(f"The message is too long ({message_bit_length} bits) to be encrypted"
                         f"with the given key ({modulus_bit_length}) bits."
                         f"Please either reduce the message size or use a bigger key.")

    ciphertext = pow(message_int, public_exponent, modulus_n)
    return ciphertext

def decrypt_message(ciphertext, private_key):
    """
    Decrypt a ciphertext using the RSA private key.

    Args:
        ciphertext (int): The encrypted ciphertext to be decrypted.
        private_key (tuple): A tuple containing the RSA private key components (d, n):
                            - d (int): Private exponent.
                            - n (int): Modulus.

    Returns:
        str: The decrypted message.

    Raises:
        TypeError: If `ciphertext` is not an integer or if `private_key`
                   is not a tuple of two integers.
        ValueError: If `ciphertext` is empty or consists only of whitespace,
                    or if the decrypted message bit length is
                    greater than or equal to the modulus bit length.
    """

    string_cipher = str(ciphertext)

    if len(string_cipher) <= 0 or str.isspace(string_cipher):
        raise TypeError("Message must be non-empty.")

    if not isinstance(private_key, tuple) or len(private_key) != 2:
        raise TypeError("The public key must be a tuple of two integers (e, n)")

    private_exponent, modulus_n = private_key
    if not (isinstance(private_exponent, int) and isinstance(modulus_n, int)):
        raise TypeError("Both public exponent and modulus must be integers")

    modulus_bit_length = modulus_n.bit_length()
    message_int = pow(ciphertext, private_exponent, modulus_n)
    message_bit_length = message_int.bit_length()

    # Check if the message bit length is less than the modulus bit length
    if message_bit_length >= modulus_bit_length:
        raise ValueError(f"The message is too long ({message_bit_length} bits) to be encrypted"
                         f"with the given key ({modulus_bit_length}) bits."
                         f"Please either reduce the message size or use a bigger key.")

    message = message_int.to_bytes((message_int.bit_length() + 7) // 8, 'big').decode('utf-8')
    return message
