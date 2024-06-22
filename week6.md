* I used chat gpt 4 for some quick formating
	* according to several feedback points received in labtool, I have stopped using chat gpt 4 for any logic/reasoning tasks.
	* this has made me slower, but entrusting myself with these aspects seems like the wiser decision
	* I am and will be using this kind of tool only for boiler plate code

* hours:
	* project: 9
	* peer review: 3

* This week I did:
	* improved UI: (many thanks to peer reviewers)
		* UI is now full screen for better readability
		* error messages are shown in red compared to everything in black
	* improved security:
		* used random.SystemRandom() instead of random.randrange
			* the initial plan was to use secrets library, but that proved to be troublesome
				* had only upperbound functionality, without lowerbound parameter for generating a random number (needed to have random numbers with specific number of bits)
			* after frustration of trying to implement such behaivour, I stumbled upon the following StackOverflow post: [Ranged secure random number](https://stackoverflow.com/questions/20936993/how-can-i-create-a-random-number-that-is-cryptographically-secure-in-python)!
				* tl;dr: random.SystemRandom is secure and has range functionalityhttps://stackoverflow.com/questions/20936993/how-can-i-create-a-random-number-that-is-cryptographically-secure-in-python
	* improved roboustness:
		* not accepting empty strings for encryption/decryption
	* code readability:
		* thanks to a peer review comment, some code redudancy got removed
	* tried to implement padding using OAEP padding from cryptography library to test first, with later plans to implement my own version of padding system
		* NOTE:  because this was not yet functional, I didn't include it in the pushed version of the project
		* QUESTION: should this functionality also be implemented by me (as in, using own code instead of already written code), or is it fine to use a library function given the aims of the project and course's
			* if I invest enough time before the demo, I think that this should be doable

* This week I learned:
	* from the peer review:
		* data compression methods
		* good README, github page hierarchy and pseudocode implementation
	* from own study/project:
		* different functionalities of tkinter
		* OAEP padding algorithm in RSA and why it makes RSA more secure
		* limits of my project:
			* there is a bug currently that seems to dissallow strings bigger than a specific amount of characters that I am investigating now
		
* What has been problematic:
	* trying to implement secrets random number generator
	* trying to implement padding
	* trying to test peer review project
		* had an older version of Python
		* tried to install a newer version of python in a virtual environment, but wasn't successful
	* making tests fully cover the logic code

* What's next:
	* I currently see that my project might have quite a few holes to fix up before the final deadline and presentation, so I plan to spend as much time as possible to make it adequate and finish everything in time

	* Proper github page, README, test instructions and the required documentation from the course
	* fully covered by tests
	* finish UI (some qol change, not high priority)
	* add padding
	* fix bugs
	* better communication of errors

* Question:
	* Are my weekly reports and peer reviews too long? Should I be more concise/less detailed?
	* The question mentioned about OAEP implementation in "This week I did" last line
