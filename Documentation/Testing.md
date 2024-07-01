# Testing

## General

Coverage disclaimer at the bottom of the file.

All of the logic of the project is within the file `rsa_functionality.py` and as such, this was the tested file. The main way of testing was done with the use of unittests and there is a performance test done manually for the same file. Manual testing has benen done also through the app to ensure that large text strings get encrypted and decrypted accordingly.

## Unittests

Unittests were designed to ensure that the program works correctly in all cases and catches errors early. The tests use representative input numbers of bit sizes, ranging from the edge case of 16 bit (the minimum accepted) up to 1024 bit numbers needed for the 2048 bit keys.

The following things are tested with the unittests:

* corectness of bit size of random generated number
* testing if a prime candidate is divisible by the first primes
* testing corectness of predicting of miller rabin test of known primes of different sizes
  * also testing if it fails non-primes
* generate prime function is tested on the premise that miller rabin test is correct
  * it checks if generated primes pass the miller rabin test
* for generate keys we ensure that they keys generated are of proper bit size
  * the private exponent is tested to see if the number of bits is within a good range. it is not a requirement to have the exact number of bits
* test encryption and decryption are tested based on correction of decrypted text = original text
  * a string of 1024 bits is tested
  * there is also a case of testing if the app correctly raises error when a user wants to encrypt a message that is bigger than a key
* input validation is also tested. ensuring that each function handles correctly the cases when they receive improper input such as text when expecting an int, empty text or negative sized numbers/keys

These tests can be located in the file `test_rsa_functionality.py` where they can be edited and changed.

In order to replicate the tests run the command:
```
python3 test_rsa_functionality.py
```
Once you are located in the terminal in the repository RSA_Alg_Labs/RSA_app


### test_input_validation

Currently, the logic passes all of the unittests implemented. \
![image](https://github.com/TheNushu/RSA_Alg_Labs/assets/131345754/78b829a2-edc9-4336-9ed3-7770659e3d91)

## Coverage Disclaimer

Throughout the course I've had several issues using the coverage module. I had managed to set it up and install on my machine, but after some time, it seems that it didn't want to be consistent anymore.

Code ran unittests with no errors, but the same code that had 95% coverage report, if a comment was added, or the order of two functions was changed, the number of misses would increase, the percentage of coverage and the "ran" lines would decrease.
![image](https://github.com/TheNushu/RSA_Alg_Labs/assets/131345754/94b51c68-aafe-4bc7-bdfb-ce67a6ac4214)\
![image](https://github.com/TheNushu/RSA_Alg_Labs/assets/131345754/b4017048-409e-4176-9382-8acbcccdaf1c)

I had tried using poetry and use it a virtual environment, but it kept acting the same way. As such, I couldn't provide the coverage report of the current unittest file. I have added in the Test_results folder past coverage results. The code shows that with the same code, the tool provided contradictory behaivour.
