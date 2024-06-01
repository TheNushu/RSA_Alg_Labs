import rsa  #used as placeholder until we implement our
            #own functions 
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
    public_key = generate_prime(1024) #number of bits of the key
    private_key = generate_prime(1024)

    return public_key, private_key

def encrypt_message(entry_text, entry_public_key):
    return f"Hey your text: {entry_text} is encrypted with: {entry_public_key[0:30]}..."

def decrypt_message(entry_text, entry_private_key):
    return f"Hey your private text: {entry_text} is decrypted with: {entry_private_key[0:30]}..."
