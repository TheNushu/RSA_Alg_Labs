## Process

The app encrypts and decrypts certain length messages (message bit size < key bit size) through the method of RSA encryption/decryption. RSA is done with a public key system, in which a message can be encrypted with an `encryption key` that is public and decrypted with a `decryption key` that is meant to be kept private. [[1]](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

The security and roboustness of the RSA method relies heavily on the process through which the keys are generated. "Every public key matches only one private key" [[2]](https://www.preveil.com/blog/public-and-private-key/#:~:text=In%20public%20key%20cryptography%2C%20every,using%20their%20corresponding%20private%20key.), this unique pairing is ensured by the mathematical properties of prime factorization. The security of RSA is a consequence of the difficulty of factoring the product of two large prime numbers, a process that is computationally impossible with current technology for sufficiently large key sizes to solve in any reasonable amount of time (see [[3]](https://www.preveil.com/blog/public-and-private-key/#:~:text=In%20public%20key%20cryptography%2C%20every,using%20their%20corresponding%20private%20key.), where it took the 'equivalent of almost 2000 years of computing on a single-core 2.2 GHz AMD Opteron-based computer' to crack a 768 bit key).

Generating a pair of keys is not computationally heavy, as we can see in `*insert reference to testing document where you show the performance times*` and is mathematically pretty simple. We multiply two *large prime numbers* to produce a `modulus`, and using it with a chosen public exponent (usually set as = `65537`) to form the public key (tuple of the form (`exponent`, `modulus`) and private keys using the `modular exponentiation` with a value `phi` to get the `private exponent`. The private key is a tuple of the form (`private exponent`, `modulus`). It is important for `phi` to not be a divisor of the `public exponent`, as that would provide an easier time cracking the prime numbers. (see [[4]](https://en.wikipedia.org/wiki/Modular_exponentiation) for explanation on modular exponentiation and [[1]](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) to see how it is used in generating the keys in more detail. The code line before `return` in the `generate_keys` function shows the python process of doing so)

Most of the *heavy lifting* here is done generating large prime numbers effectively. Because we want to generate such big number that cannot be predicted, we cannot produce them deterministically (taking "life times"). In order to generate this kind of numbers, we will use a *probabilistic* approach instead by using the [Miller Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test), which is an algorithm that tells us if a number is *likely* to be prime. It does so by test checking whether a specific property, which is known to hold for prime values, holds for the number under testing. (To see the properties in depth, check this section [[5] Strong Probable Primes](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Strong_probable_primes_)

The process used in this app for generating such primes involves random number generation. First, after the app takes as input the key size that the user wishes to receive, it generates a random number of the desired bit size in `generate_n_bit_random(bit_length)`. It does so by generating a random number within the desired size range with the method: `random.SystemRandom()`. This method is considered *cryptographically secure*. 
> ("random.SystemRandom is a class that uses the os.urandom() function to generate random numbers from sources provided by the operating system. This class does not rely on software state and the generated number sequences are not reproducible. This means that the seed() method has no effect and is ignored." [[6]](https://interactivechaos.com/en/python/function/randomsystemrandom)).

After we generate a random number, we check to see if it is divisible with the first 70 prime numbers. If it is not, we can put it through the Miller-Rabin test for 20 iterations. This number was chosen arbitrarily, according to Warren MacEvoy and SquareRootOfTwentyThree users on StackOverflow and the paper "Average case error estimates for the strong probable prime test" by Damgard-Landrock-Pomerance (see [[7]](https://stackoverflow.com/a/21450484/20081651) and [[8]](https://math.dartmouth.edu/~carlp/PDF/paper88.pdf) ), after 6 iterations on a 1024 bit number, the probability of error of Miller-Rabin test is 10^(-40). Less likely than a bit flip error in your hardware machine, according to Warren MacEvoy.

See `*insert reference to user guide*` if you want to see how this logic is executed with the program.

## Big-O Analysis according to the pseudocode

The following time complexities are for the pseudocode of the `rsa_functionality.py`:

* `generate_n_bit_random(bit)` : O(1) - constant
* should provide the next bit address, which is a constant time operation
* `generate_prime_candidate(bit_length)` : O(b^ n) or O(1)
* this is tricky, we could say that it depends on the likelyhood that a number is prime, but also we can say it is constant because generation of a random number is constant and going through each prime in the 70 primes array is also constant
* the [likelyhood of a random number to be prime](https://t5k.org/glossary/page.php?sort=PrimeNumberThm#:~:text=The%20prime%20number%20theorem%20implies,to%201%2Flog%20n) is log n, where n is the number dependent on the number of bits
* `is_miller_rabin_passed(candidate_prime)` : O(k * log^3 n )
* where n is the prime number we test (that depends on the number of bits) and k is the number of iterations
* `generate_prime(bits)`: O(b^n) * O(k * log^3 n) * O (1) = O(k *log^4 * b^ n)
* it depends on: the same exponential likelyhood of a random number being prime as in `generate_prime_candidate` once we increase the number of bits, the functions `is_miller_rabin_passed`, `generate_prime_candidate`
Note: `generate_keys` calls the function `generate_prime` 2 times with the argument (bits // 2), thus, both in the pseudocode analysis and performance analysis, we should consider that `generate_keys` depends on the `generate_prime` function with the multiplier of 1/2.
* `generate_keys(bits)`: 1/2 * O(k * log^4 n) * O(b) = 1/2 * O(b * k * log^4 n)
* O(k * log^4 n) comes from the calls on `generate_prime` and b is the likelyhood of two n bit numbers to not result in a 2*n bit number. I couldn't find any experiments on this to include as a time complexity formula, but it should be quite rare.
* `encrypt_message(message, public_key)` and `decrypt_message(ciphertext, private_key)`: O (log^3 n)
* where n is the modulus

The following are the space complexities for the pseudocodes:

* `generate_n_bit_random(bit)`: O(1)
* `generate_prime_candidate(bit_length)`: O(1)
* `is_miller_rabin_passed(candidate_prime)`: O(1)
* it stores a fixed amount of variables, not dependent on bit size
* `generate_prime(bits)`: O (log n)
* the likelyhood of a random number being prime will dictate how many random numbers will be generated
* `generate_keys(bits)`: O(n)
* the space complexity increases linearly with n = bits
* `encrypt_message(message, public_key)`: O(n)
* where n = bits. each message will have to be stored with a size of the bits of modulus n
* `decrypt_message(ciphertext, private_key)`: O(n)
* this depends on the size of the encrypted text

## Comparison of Big O with Performance results:

The following are the results of the performance test. 
Note: generate_keys() has been outside the functions encrypt and decrypt to be able to see their performances individually. As we can see, if we were to have included `generate_keys()` within the encryption and decryption testing, we wouldn't have gotten very useful information.

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


* Given that we tested the functions with exponential input, the results seem to hold our assumptions. `generate_n_bit_random` and `gen_prime_candidate` are constant throughout all sizes, `encrypt_message`, `decrypt_message` and `is_miller_rabin_passed` growing somewhat linearly and `generate_primes` is indeed exponential.

## Shortcomings

Currently I think that the generation of numbers and computations themselves are fairly efficient, but there is a current issue of bit loss. When we generate the keys, due to the different multiplications and modular exponentiation, sometimes a few bits get lost. A past experiment showed that the range of bits lost was from 1-10, with the 1 bit loses having a likelyhood of 80% and the bigger bit loses had a smaller chances of existing with a hyperbolic decay. Ranging from 1 to 10 bits on 1024 keys. The modulus n loses at most 1 bit. But as such, the project currently cannot support keys that are smaller than 16 bits for testing purposes for example.

The biggest flaw is the coverage not working consistently. I have tried to also use poetry for dependencies and to use coverage in a virtual environment, but it didn't work. The issue is explained in more detail in the Testing file. I still do not know the cause of the issue, but the method of testing seemed comprehensive enough for the 2-3 times coverage worked.

As for the security of the encryptions, we might want to decide to use a padding system. Currently, an encrypted message could be susceptible to a [frequency analysis attack](https://en.wikipedia.org/wiki/Frequency_analysis) especially if the original language of the encrypted message is known.

Improvements to the user interface to be easier to use would be desired, but the current state is satisfactory.

## Use of Language Models

I have used the help of chat gpt 4 throughout the project. Most details are in the beginning of each weekly report, but I have used it in the beginning as a code reviewer and with help in debugging. By the end of the course, through feedback from labtool I stopped using it for logic/reasoning questions. This proved to slow me down, but I can already see that it makes me improve faster as a programmer.

I have also used chat gpt 4 to write boiler plate code, and some prompts of the form "please rewrite this function to include `some format instruction`".

It proved to be a very useful tool throughout the course.

## Sources

1. [RSA, Wikipedia, May 2024](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
2. [Orlee Berlove, "Public – Private Key Pairs & How they work", Jan 2024](https://www.preveil.com/blog/public-and-private-key/#:~:text=In%20public%20key%20cryptography%2C%20every,using%20their%20corresponding%20private%20key.)
3. [RSA-768, Wikipedia, March 2024](https://en.wikipedia.org/wiki/RSA_numbers#RSA-768)
4. [Modular Exponentiation, Wikipedia, March 2024](https://en.wikipedia.org/wiki/Modular_exponentiation)
5. [Miller-Rabin Test, Strong Probable Primes, Wikipedia, May 2024](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Strong_probable_primes)
6. [Interactive Chaos, 2021](https://interactivechaos.com/en/python/function/randomsystemrandom)
7. [SquareRootOfTwentyThree, Nov 2014](https://stackoverflow.com/a/21450484/20081651)
8. [Damgard-Landrock-Pomerance, Average case error estimates for the strong probable prime test, July 1993](https://math.dartmouth.edu/~carlp/PDF/paper88.pdf)
9. [Prime glossary, "prime number theorem"](https://t5k.org/glossary/page.php?sort=PrimeNumberThm#:~:text=The%20prime%20number%20theorem%20implies,to%201%2Flog%20n).
10. [Frequency analysis, Wikipedia, April 2024](https://en.wikipedia.org/wiki/Frequency_analysis).
