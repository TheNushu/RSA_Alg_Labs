# Project Specification

Study Programme: Bachelor of Science; Computer Science and Data Science (English Programme)

## Topic and Implementation
The project topic is the implementation of RSA encryption app. I chose this topic because I am interested in cybersecurity and encryption process in particular. I also wanted to have an interactive project for easier working with the process.

Within this app, a user can choose a size of rsa keys that they desire within their requirements of: speed and security. After they generate keys with their requirements, the user can provide in the GUI a text that they wish to encrpyt and the app will provide to them an encrypted version of the text that they inserted. 

As for inputs, each of the fields is highly flexible and user can input fields such as: `text to encrypt` (str), `text to decrypt` (converted from str from app to int to be worked on), `public key` (tuple `(public exponent int, modulus n int`), `private key` (tuple `(private exponent int, modulus n int`) and `key bit size` (bit).

There is only a single "special" data structure compared to the common python ones such as: int and str, and that is `key data structure`. A key data structure is a tuple of the format `(exponent, modulus n)` where an exponent can either be public (usually a common prime number such as e = `65537`) or private (made out of the modular multiplicative inverse of e modulo (p-1)(q-1) is the number d such that d * e ≡ 1 (mod (p-1)(q-1)). Where p and q are large prime numbers). Modulus n is made out of the product of two large prime numbers that are to be generated with [rsa_functionality_py](https://github.com/TheNushu/RSA_Alg_Labs/blob/main/RSA_app/rsa_functionality.py)

The internal logic of the app handles functionalities such as:
* (1) [secure](https://stackoverflow.com/questions/20936993/how-can-i-create-a-random-number-that-is-cryptographically-secure-in-python) random number generation 
* (2) [Miller Rabin test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test) to determine if a number is *likely* prime
* (3) prime number generation using generation from (1) and confirmed as prime from (2)
* (4) rsa key generation using prime numbers from (3) [modular exponentiation](https://en.wikipedia.org/wiki/Modular_exponentiation)
* (5) [rsa encryption](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Encryption) algorithm of a text given by the user, using a public key from (4)
* (6) [rsa decryption](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Decryption) algorithm of an encrpyted text given by the user, using the corresponding private key from (4)

The UI handles functionalities such as:
* (7) user interface generation using [tkinter](https://docs.python.org/3/library/tkinter.html) widgets
* (8) copy and paste functionalities with buttons and user peripheral hardware
* (9) wrapping functions for encryption and decryption algorithm from [rsa_functionality_py](https://github.com/TheNushu/RSA_Alg_Labs/blob/main/RSA_app/rsa_functionality.py) such that it works with tkinter buttons

## Languages
The project documentation and code language are English and Python respectively. I can review projects implemented in: python, lua, c++. Javascript is also an option for project review.

will be implemented as a web application using Python with the `Flask` library (I can peer review projects implemented in Python). The project documentation will be written in English, but the code itself will be implemented in English.

## Sources
- [Secure random generation with a range (Stackoverflow)](https://stackoverflow.com/questions/20936993/how-can-i-create-a-random-number-that-is-cryptographically-secure-in-python)
- [Predicting tool generated number of python random module (Github Project)](https://github.com/tna0y/Python-random-module-cracker?tab=readme-ov-file)
- [Miller Rabin test (Wikipedia)](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)
- [Miller Rabin test (Geeks for Geeks)](https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/)
- [Modular Exponentiation (Wikipedia)](https://en.wikipedia.org/wiki/Modular_exponentiation)
- [RSA encryption system (Wikipedia)](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- [tkinter (docs python)](https://docs.python.org/3/library/tkinter.html)


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
