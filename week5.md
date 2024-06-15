* I used chat gpt 4 for help in a few situations:
	* code feedback (if it looks good according to pep8 standard and if it caught any shortcomings of code logic)
	* bug fixing help after using google and stackoverflow
	* for test_rsa_functionality I asked it to rewrite the same code in pep8 format (I fixed myself the format for the app.py and rsa_functionality.py)
	* for the peer review, at the end, after I made all the research of the code, and tried bugfixing, I had asked it if it sees a method of improving the person's code. It mentioned an initialisation in their trie struture.
		* I mentioned to the person I peer reviews what comment was made by chat gpt and I advised to use it with care.

* hours:
	* project: 12
	* peer review: 4

* This week I did:
	* bugfixed a major bug that didn't let user encrypt and decrypt multiple times in a single session or with multiple pairs of keys in the same session
	* made pylint and coverage finally work
	* as a consequence of the previous point, a good portion of the time was spent reformatting the codes for app.py and rsa_functionality.py to be pep8 standard suitable and get grades 10 by pylint
		* I also structured the codes more logically, especially in the app.py which was quite messy
		* I asked chat gpt 4 to rewrite the test code in pep8 format, but I ended up refactoring it anyway
		* test code will be quite hard to get 10 since a few prime numbers are bigger than the character limit per line;
			* I will look into ways to split such numbers on multiple lines so it can be approved
	* improved unittesting:
		* most functions should have extensive testing now, with multiple tests per function.
		* according to feedback, functions that use big prime numbers are tested with big prime numbers
		* in some cases the prime numbers to check are hardcoded (googled or found from a website that it is sourced at the end of this document)
		* at first I tried a check for assertFalse in prime numbers as "generated prime number -+2" because i believed that way the odd numbers are very unlikely to be prime and thus the tests would be robust
			* this made me discover "twin prime numbers", prime numbers that have a difference of 2 between them
			* now the tests for big non prime numbers is generated prime * generated prime
	* quality of life improvements in the UI
	* code reviewing:
		* I enjoyed the detective work of inspecting someone else's code
			* debugging (and documenting)
			* bug fixing

* This week I learned:
	* about nice file structure and saw an example of clear instruction on the project I peer reviewed
		* their github front page of the app was very user friendly too
	* different methods of unittesting
	* pep8 standard more in depth
	* debugging tecniques and steps
	* valuable information about my current project from the peer review I got and from the one I gave

* What has been problematic:
	* when giving the peer review and writing it, I first wrote it in microsoft word, for constant back up.
		* I had some issues transferring it from word to markdown and the final product didn't look as great as if I were to write it in markdown from the start
	* I didn't have any other major issues, everything else needs/needed more time and determintion
		* there still is a function that doesn't work when unittested, but works normal in production. this needss investigated
* What's next:
	* implement UI improvements as recommended in the peer review
	* implement padding in the encrypted text and move from random module to secrets module
	* make unittests cover at least 80% of the logic code
	* maybe devide the rsa logic code into at least 2 files for better readability
	* improve github page of the project:
		* better installing instructions
		* file management
		* add coverage and pylint reports on the page
		* implement poetry virtual environment and needed libraries for the project for easier install of the next peer reviewer
	* improve UI such that text and encrypted text are easier to read
		* add text constraints and better feedback to the user
