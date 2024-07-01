# Testing

## General

Coverage disclaimer at the bottom of the file.

All of the logic of the project is within the file `rsa_functionality.py` and as such, this was the tested file. The main way of testing was done with the use of unittests and there is a performance test done manually for the same file. Manual testing has been done also through the app to ensure that large text strings get encrypted and decrypted accordingly.

If you want to repeat the manual testing of large string encryption, please follow the instructions from the User_Guide section and insert your wanted texts.

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

At the moment of writing this documentation, the logic passes all of the unittests implemented. \
![image](https://github.com/TheNushu/RSA_Alg_Labs/assets/131345754/78b829a2-edc9-4336-9ed3-7770659e3d91)

## Performance testing

The following are the results of the performance test. We perfomed 100 iterations of each parameter with the following function:

```
def run_performance_test(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time, result
```
This function tracked the time that it took a function from the moment it received a call until it gave the result. All of the functions except Miller Rabin test have been tested using as parameters: `input_sizes = [256, 512, 1024] ` and miller rabin test has been tesed with known prime numbers of sizes 256 bits, 512 bits and 1024 bits.

Note: generate_keys() has been called outside the functions encrypt and decrypt to be able to see their performances individually. As we can see, if we were to have included `generate_keys()` within the encryption and decryption testing, we wouldn't have gotten very useful information.

### 256-bit Keys

| Function                        | Average Time (s) | Total Time (s) |
|---------------------------------|------------------|----------------|
| `generate_n_bit_random`         | 0.0000           | 0.0025         |
| `gen_prime_candidate`           | 0.0002           | 0.0227         |
| `is_miller_rabin_passed`        | 0.0028           | 0.2849         |
| `generate_prime`                | 0.0169           | 1.6913         |
| `generate_keys`                 | 0.0202           | 0.0605         |
| `encrypt_message`               | 0.0000           | 0.0605         |
| `decrypt_message`               | 0.0001           | 0.0605         |

### 512-bit Keys

| Function                        | Average Time (s) | Total Time (s) |
|---------------------------------|------------------|----------------|
| `generate_n_bit_random`         | 0.0000           | 0.0024         |
| `gen_prime_candidate`           | 0.0003           | 0.0300         |
| `is_miller_rabin_passed`        | 0.0230           | 2.2962         |
| `generate_prime`                | 0.1212           | 12.1193        |
| `generate_keys`                 | 0.0393           | 0.1178         |
| `encrypt_message`               | 0.0000           | 0.1178         |
| `decrypt_message`               | 0.0007           | 0.1178         |

### 1024-bit Keys

| Function                        | Average Time (s) | Total Time (s) |
|---------------------------------|------------------|----------------|
| `generate_n_bit_random`         | 0.0000           | 0.0025         |
| `gen_prime_candidate`           | 0.0004           | 0.0375         |
| `is_miller_rabin_passed`        | 0.0947           | 9.4691         |
| `generate_prime`                | 1.0903           | 109.0291       |
| `generate_keys`                 | 0.1649           | 0.4948         |
| `encrypt_message`               | 0.0001           | 0.4948         |
| `decrypt_message`               | 0.0041           | 0.4948         |

If you want to repeat the tests, use the function defined at the beginning of the section (`run_performance_test`) in a python file with the following templates:
* for the generate functions:
```
        for bits in input_sizes:
            times = []
            # Test generate_n_bit_random
            for _ in range(100):
                time_taken, _ = run_performance_test(generate_n_bit_random, bits)
                times.append(time_taken)
            avg_time = sum(times) / len(times)
            output = f"Average time for generate_n_bit_random with {bits} bits: {avg_time:.4f} seconds. Total time: {sum(times):.4f} s."
            print(output)
```
* for the miller rabin function: primes is an array of tuples [ ( bit size number(int), prime number of bit size(int) ) ]
```
    for prime in primes:
        times = []
    
        # Test generate_n_bit_random
        for _ in range(100):
            time_taken, _ = run_performance_test(is_miller_rabin_passed, prime[1])
            times.append(time_taken)
        avg_time = sum(times) / len(times)
        output = f"Average time for is_miller_rabin_passed for prime with {prime[0]} bits: {avg_time:.4f} seconds. Total time: {sum(times):.4f} s."
        print(output)
```
* and for the encryption/decryption functions:
```
      for bits in input_sizes:
            times = []
            message = "Test message for RSA encryption"
            public_key, private_key = generate_keys(bits)
            encrypted_message = encrypt_message(message, public_key)
            
            # Encrypt message
            time_taken, encrypted_message = run_performance_test(encrypt_message, message, public_key)
            output = f"Time for encrypting message with {bits} bits key: {time_taken:.4f} seconds. Total time: {sum(times):.4f} s."
            print(output)
            file.write(output + "\n")
```

If you want to repeat the tests, use the function defined at the beginning of the section (`run_performance_test`) in a python file with the following templates:
* for the generate functions:
```
        for bits in input_sizes:
            times = []
            # Test generate_n_bit_random
            for _ in range(100):
                time_taken, _ = run_performance_test(generate_n_bit_random, bits)
                times.append(time_taken)
            avg_time = sum(times) / len(times)
            output = f"Average time for generate_n_bit_random with {bits} bits: {avg_time:.4f} seconds. Total time: {sum(times):.4f} s."
            print(output)
```
* for the miller rabin function: primes is an array of tuples [ ( bit size number(int), prime number of bit size(int) ) ]
```
    for prime in primes:
        times = []
    
        # Test generate_n_bit_random
        for _ in range(100):
            time_taken, _ = run_performance_test(is_miller_rabin_passed, prime[1])
            times.append(time_taken)
        avg_time = sum(times) / len(times)
        output = f"Average time for is_miller_rabin_passed for prime with {prime[0]} bits: {avg_time:.4f} seconds. Total time: {sum(times):.4f} s."
        print(output)
```
* and for the encryption/decryption functions:
```
      for bits in input_sizes:
            times = []
            message = "Test message for RSA encryption"
            public_key, private_key = generate_keys(bits)
            encrypted_message = encrypt_message(message, public_key)
            
            # Encrypt message
            time_taken, encrypted_message = run_performance_test(encrypt_message, message, public_key)
            output = f"Time for encrypting message with {bits} bits key: {time_taken:.4f} seconds. Total time: {sum(times):.4f} s."
            print(output)
            file.write(output + "\n")
```

## Coverage Disclaimer

Throughout the course I've had several issues using the coverage module. I had managed to set it up and install on my machine, but after some time, it seems that it didn't want to be consistent anymore.

Code ran unittests with no errors, but the same code that had 95% coverage report, if a comment was added, or the order of two functions was changed, the number of misses would increase, the percentage of coverage and the "ran" lines would decrease.
![image](https://github.com/TheNushu/RSA_Alg_Labs/assets/131345754/94b51c68-aafe-4bc7-bdfb-ce67a6ac4214)\
![image](https://github.com/TheNushu/RSA_Alg_Labs/assets/131345754/b4017048-409e-4176-9382-8acbcccdaf1c)

I had tried using poetry and use it a virtual environment, but it kept acting the same way. As such, I couldn't provide the coverage report of the current unittest file. I have added in the Test_results folder past coverage results. The code shows that with the same code, the tool provided contradictory behaivour.
