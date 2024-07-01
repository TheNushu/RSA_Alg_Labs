# Project Specification

Study Programme: Bachelor of Science (BSc) (English Programme)

## Topic
The project topic is the implementation of RSA encryption app. I chose this topic because I am interested in cybersecurity and encryption process in particular. I also wanted to have an interactive project for easier working with the topic.

## Languages
The project documentation and code language are English and Python respectively. I can review projects implemented in: Python, Lua and C++. Javascript is also an option for project review and I am familiar with SQL.

## Algorithms and Data Structures

The internal logic of the app handles functionalities such as:
* (1) [secure](https://stackoverflow.com/questions/20936993/how-can-i-create-a-random-number-that-is-cryptographically-secure-in-python) random number generation 
* (2) [Miller Rabin test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test) to determine if a number is *likely* prime
* (3) prime number generation using generation from (1) and confirmed as prime from (2)
* (4) rsa key generation using prime numbers from (3) and [modular exponentiation](https://en.wikipedia.org/wiki/Modular_exponentiation)
* (5) [rsa encryption](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Encryption) algorithm of a text given by the user, using a public key from (4)
* (6) [rsa decryption](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Decryption) algorithm of an encrpyted text given by the user, using the corresponding private key from (4)

The UI handles functionalities such as:
* (7) user interface generation using [tkinter](https://docs.python.org/3/library/tkinter.html) widgets
* (8) copy and paste functionalities with buttons and user peripheral hardware
* (9) wrapping functions for encryption and decryption algorithm from [rsa_functionality_py](https://github.com/TheNushu/RSA_Alg_Labs/blob/main/RSA_app/rsa_functionality.py) such that it works with tkinter buttons

There is only a single "special" data structure besides the common python ones such as: int and str, and that is `key data structure`. A key data structure is a tuple of the format `(exponent, modulus n)` where an exponent can either be public (utosually a common prime number such as public exponent = `65537`) or private (made out of the modular multiplicative inverse of `public exponent mod (p-1)(q-1)` such that `private exponent * public exponent ≡ 1 (mod (p-1)(q-1))`. Where p and q are large prime numbers). Modulus n is made out of the product of two large prime numbers (`p*q` in our case) that are to be generated with [rsa_functionality_py](https://github.com/TheNushu/RSA_Alg_Labs/blob/main/RSA_app/rsa_functionality.py) (See: [Key Generation RSA (Wikipedia)](https://en.wikipedia.org/wiki/RSA_(cryptosystem)#Key_generation))

## Problem solved

Within this project, a user gains the ability to transform plain text into secure ecnrypted messages. Besides this use case, once can also get some more insight upon the process of RSA encryption by the use of this app.

## Inputs and Outputs

As for inputs, each of the fields is highly flexible and user can input fields such as: 
* `text to encrypt` (str)
	* the original text that the user wants encrypted 
* `text to decrypt` (converted from str in app to int to be worked on)
	* the encypted text that the user wants decrypted
* `public key` (tuple (`public exponent` int, `modulus n` int)
	* public key is used in the encryption process
* `private key` (tuple (`private exponent` int, `modulus n` int)
	* private key is used in the decryption process
 	* *highly important that the user doesn't share this key with untrustful parties*
* `key bit size` (bit).
	* the bit size of the keys has the following purposes:
 		* a bigger key is more secure (harder to find the product of the original prime numbers generated) but take a more initial time to compute
   		* the text to be encrypted is dependent on the key size

For the outpus, we have the following cases:
	* first, the user is always informed through `output text label` with different fedeback of their actions
 		* errors are coloured in red and general information in black
   	* after generating keys:
    		* user receives as output the private and public key at the bottom of the app in the fields:
      			* `your private key` and `your public key`
	 * after `encryption` the user receives as output the encrypted text
  	 * after `decryption` the user receives the original text

## Time complexities wished to achieve

* Time complexities:
	* Key generation: polynomial
	* Ecryption: polynomial
	* Decryption: polynomial
	* Signature: polynomial
	* verification: polynomial
* Wished space complexities:
	* for all mentioned above (wished time complexities), space complexities should be linear

 ## Sources
- [Secure random generation with a range (Stackoverflow)](https://stackoverflow.com/questions/20936993/how-can-i-create-a-random-number-that-is-cryptographically-secure-in-python)
- [Tool that predicts generated number of python random module (tna0y, Github)](https://github.com/tna0y/Python-random-module-cracker?tab=readme-ov-file)
- [Miller Rabin test (Wikipedia)](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test)
- [Miller Rabin test (Geeks for Geeks)](https://www.geeksforgeeks.org/primality-test-set-3-miller-rabin/)
- [Modular Exponentiation (Wikipedia)](https://en.wikipedia.org/wiki/Modular_exponentiation)
- [RSA encryption system (Wikipedia)](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
- [tkinter (docs python)](https://docs.python.org/3/library/tkinter.html)

