* used gpt4 for feedback if code format looks okay until I look into pylint.
	* also in some debugging after spent more than 30m on certain bugs and errors in interface

* hours spent: 15

* This week I:
	* bug fixed interface and now is fully finished
	* tried to implement functionality of:
		* after generating keys, the buttons and fields for the private and public keys appears
			* after copying the keys, the fields and buttons specific to them to dissapear
		* unfortunately, this caused constant bugs so I decided to remove them
	* implementation of the prime generation code for the rsa. 
		* random prime number using probabilistic methods
		* miller rabin test for prime numbers
	* implemented unit testing for the rsa implementation. should also the interface have unittesting?
	* tried to use coverage, but errored. looking more into it now.

* How did the project progress:
	* fairly well. I am happy wit the progress made for the program logic and that i finally managed to finish the interface.
		* not satisfied with the interface implementation since I couldn't do it exactly how I wanted to.
* What did you learn this week:
	* I spent a good amount of time checking the security of random number generation function from the python random library and found out different things on how to use more secure techniques and libraries.
	* Got to understand  the prime generation algorithm for rsa better
	* I read more about unittesting
* What has been problematic:
	* coverage using
	* tkinter widget system when you want to "hide-show" different widgets
* What's next:
	* Full implementation of unittesting
	* Coverage working
	* setting up pylint
	* completing the core functionality of rsa of encrypting text now that:
		* UI works well and the keys are generated well
	* probably padding of the text such that the encryption would be safer against counting "most common" characters to figure out the encryption
	* setting up more "random" number generation
