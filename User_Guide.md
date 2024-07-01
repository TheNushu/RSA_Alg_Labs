# User Guide

## Installation

Clone the repository on your machine in a folder that you desire to run it
```
git clone git@github.com:TheNushu/RSA_Alg_Labs.git
```
To start the app, you will need to run the file app.py. This can be achieved either through the command line, with the following commands once you are located in the root directory:

```
cd RSA_app
```
```
python3 app.py
```
This can be achieved also by opening the directory with an IDE and running the app.py file
## App usage
After running `app.py`, you should be greeted by the following screen:
![image](https://github.com/TheNushu/RSA_Alg_Labs/assets/131345754/c3578690-84bb-482d-a069-681a46789ded)

In order to close the app, use the keys `Alt + F4` or press the X button in the top right corner.\
![image](https://github.com/TheNushu/RSA_Alg_Labs/assets/131345754/9befa350-ba27-45ca-b87b-c641108df2d8)

The first thing you want to do is to choose the key sizes of the key pair by typing in the size and pressing the button.
![image](https://github.com/TheNushu/RSA_Alg_Labs/assets/131345754/1e0b0737-0e59-4186-8632-24baa60ef1f0)

The bigger the keys, the more secure! The current recommended standard length for RSA keys is 1024 bits and this is the size set as default. The downside of bigger keys are the fact that they take a little more to generate and are bigger in size when you take storage into consideration. A bigger key can also encrypt more data at once. When you encrypt something, you will want to ensure that the text you want to encrypt is smaller than the key size. But don't worry, the app informs you if that happens.
![image](https://github.com/TheNushu/RSA_Alg_Labs/assets/131345754/bc6dc743-f1fc-4c48-8b7b-b1509fadc0bc)

After you generate the keys, you'll see the following warning:\
![image](https://github.com/TheNushu/RSA_Alg_Labs/assets/131345754/e0ac437d-c599-4185-a1be-145c7d0f8de2) 
Take into account that once your private key is known by a different party, they can decrypt every single thing encrypted with the public key pair if they know the public key. But even if they do not, it is easier to crack a public key once you know the private one.

After you press ok, the bottom 2 text areas will fill with the generated keys. Note: if you have chosen large keys, this might take a little more time. See the performance area in the test file to have an idea *INSERT LINK TO TEST DOCUMENT HERE*. The generation also depends on your computing power.\
![image](https://github.com/TheNushu/RSA_Alg_Labs/assets/131345754/5aeb1678-0a70-4de9-812a-d4596d2f9887)

![image](https://github.com/TheNushu/RSA_Alg_Labs/assets/131345754/cc11eec9-24f4-4428-b86c-d7fcaf31ec12) 


You can use the buttons at the right to copy each of the keys. Copy 1 key at a time and place them in their required text areas here like this (ensure that text area is empty before pasting):
![image](https://github.com/TheNushu/RSA_Alg_Labs/assets/131345754/5f4633b1-0466-4983-a963-977a39eeb005)

![image](https://github.com/TheNushu/RSA_Alg_Labs/assets/131345754/cc578716-c613-4c9f-9c77-72602275351b)

Proceed similarly with the private key.

After writing your text that you want to encrypt in the top text area, press the `Encrypt` button on the right. You should see a confirmation message in the middle of the screen (bottom in the picture) with black text like this:
![image](https://github.com/TheNushu/RSA_Alg_Labs/assets/131345754/bce89112-d2b5-42ba-a402-66ed546c3e4a)

After encrypting, the encrypted text should be automatically copied to your clipboard. Ensure that the text area of the `Enter string to decrypt` is empty and paste you encrypted text there.
![image](https://github.com/TheNushu/RSA_Alg_Labs/assets/131345754/8c24af00-c1ed-472d-a492-ac7d0a2016b5)

After pressing `Decrypt` button, you should see the original text in the information area.
![image](https://github.com/TheNushu/RSA_Alg_Labs/assets/131345754/eafc6a7c-2063-4ba7-9fe1-8f313c3bc75e)

## Input types

* Enter string to encrypt/decrypt should be a string
* Enter public/private key should be a `key` tuple of the form `(exponent, modulus)`. Exponent and modulus are ints. Check documentation for more details on their requirements.
* Bit size should be a number that is a *power of 2*

## Tip

Don't forget to save your keys somewhere if you want to use them in the future since they are not permamently stored within the app.

