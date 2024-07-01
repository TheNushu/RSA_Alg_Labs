* used gpt4 for debugging and questions about code if I didn't omit anything. it was decently helpful.
* question: do you think that this is good use of gpt? or should I spend more of my time and energy trying to debug on my own and spending time in frustration (more time spent like this now, the easier it will become in the future I assume)
	* will I miss to develop my programming skills by asking help from gpt too much in this area?

* hours spent: 8 this week I had very many working hours at work, and was very tired most of the time. didn't have much energy to work on the project, sorry

* This week I:
	* implemented encryptiong and decryption functionality to the app
	* updated UI commands to support proper management of the user input so it can be used accordingly by the encryption logic
	* tried to add new tests to the rsa_functionality, but most of them error (probably will need to fix the code to be good enough)

* How did the project progress:
	* I feel like I spent too little time in the project this week, not developing it enough
	* I still tried to progress on what I found to be most important

* What did you learn this week:
	* this week I looked up "extensively" (just an hour or two, but around 25% of the total time) on how to make sure the encryption and decryption work effectively
	* looked into security of rsa and what are its weakpoints in the encryption proccess.
	* I found a project where a person predicted random numbers generated with python random library. 
		* more incentive to change the random library to secrets library (which I learned that it is considered cryptographically secure)

* What has been problematic:
	* unittesting issues
	* making the UI be consistent
	* there is a bug, you can encrypt only once per session of the app. I think some variables might not be updated accordingly/some are left with values from previous tries, need to look it up to solve it

* What's next:
	* almost all points from last week such as: pylint, coverage, padding, use secrets library instead of random library (for better security)
	* solve bug such that the app can encrypt and decrypt consistently
	* make unittests run fine (i.e. make the code proper such that the tests find it adequate)
