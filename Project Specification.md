Week 1
* study program: Bachelor of Science
* langugage of the project: Python
		* langugages for which I could peer review projects: Python, Lua and possibly C++
* Algorithms and data structures: 
	* key generation
	* prime number generation (Miller-Rabin test) using secure random number generation (with random.SystemRandom() )
	* 
	* modular exponentiation
	* encryption/decryption algorithm
* "What problem are you solving":
	* securing plain text into encrypted text (that can be decrypted with private key usage)
* Inputs:
	* Encryption:	
		* user provides an ascii text to the program
	* Decryption:
		* encrypted text
		* private key
* Outputs:
	* Encryption:
		* feedback message if key generation is successful
		* displaying of keys to the user
		* ciphered text
		* error messages (if necessary)
	* Decryption:
		* original text
* Wished time complexities:
	* Key generation: polynomial
	* Ecryption: polynomial
	* Decryption: polynomial
	* Signature: polynomial
	* verification: polynomial
* Wished space complexities:
	* for all mentioned above (wished time complexities), space complexities should be linear
