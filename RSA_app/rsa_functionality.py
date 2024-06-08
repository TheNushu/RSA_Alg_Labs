import random

# Pre generated primes
first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
					31, 37, 41, 43, 47, 53, 59, 61, 67,
					71, 73, 79, 83, 89, 97, 101, 103,
					107, 109, 113, 127, 131, 137, 139,
					149, 151, 157, 163, 167, 173, 179,
					181, 191, 193, 197, 199, 211, 223,
					227, 229, 233, 239, 241, 251, 257,
					263, 269, 271, 277, 281, 283, 293,
					307, 311, 313, 317, 331, 337, 347, 349]


def n_bit_random(n):
	#obtian a Random number
	if n < 2:    
		raise ValueError("Bit size must be at least 2 to form a valid range")
    # obtain a Random number
	return random.randrange(2**(n-1)+1, 2**n - 1)


def get_low_level_prime(n):
	#Generate a prime candidate divisible 
	#by first primes
	while True:
		prime_candidate = n_bit_random(n)
		# Test divisibility by pre-generated
		# primes
		for divisor in first_primes_list:
			if prime_candidate % divisor == 0 and divisor**2 <= prime_candidate:
				break
		else:
			return prime_candidate


def is_miller_rabin_passed(prime_candidate):
	#Run 20 iterations of Rabin Miller Primality test
	
	max_Divisions_By_Two = 0
	d= prime_candidate-1
	while d% 2 == 0:
		d>>= 1
		max_Divisions_By_Two += 1
	assert(2**max_Divisions_By_Two * d== prime_candidate-1)

	def is_composite(round_tester):
		if pow(round_tester, d, prime_candidate) == 1:
			return False
		for i in range(max_Divisions_By_Two):
			if pow(round_tester, 2**i * d, prime_candidate) == prime_candidate-1:
				return False
		return True

	# Set number trials 
	# More iterations = better security, slower process
	    #This is because, with more trials, the Rabil Miller
        #can be more probabilistically certain
	numberOfRabinTrials = 20
	for i in range(numberOfRabinTrials):
		round_tester = random.randrange(2, prime_candidate)
		if is_composite(round_tester):
			return False
	return True


def generate_prime(bits):
	while True:
		prime_candidate = get_low_level_prime(bits)
		if not is_miller_rabin_passed(prime_candidate):
			continue
		else:
			#print(prime_bits, "bit prime is: \n", prime_candidate)
			return prime_candidate

def generate_keys():
    p = generate_prime(512) #number of bits of the key
    q = generate_prime(512)
    n = p * q
    phi_n = (p - 1) * (q - 1)
	
    # Common choice for e
    e = 65537
	
    # if e and phi_n are coprime = security flaw,
    #   easy to decrypt
	# we change keys until that is not happening
	# we could also just change e instead
    while (p - 1) * (q - 1) % e == 0:
        p = generate_prime(512) 
        q = generate_prime(512)
    
    n = p * q
    phi_n = (p - 1) * (q - 1)
		
    # Calculate d, the mod inverse of e under phi(n)
    d = pow(e, -1, phi_n)

    # The public key is (e, n) and the private key is (d, n)
    return ((e, n), (d, n))


def encrypt_message(message, public_key):
    e, n = public_key
    # Convert message to an integer for encryption
    m_int = int.from_bytes(message.encode('utf-8'), 'big')
    c = pow(m_int, e, n)
    return c

def decrypt_message(ciphertext, private_key):
    d, n = private_key
    m_int = pow(ciphertext, d, n)
    # Convert integer back to string
    message = m_int.to_bytes((m_int.bit_length() + 7) // 8, 'big').decode('utf-8')
    return message
