"""
This module implements a graphical user interface (GUI)
for an RSA encryption and decryption tool using Tkinter.

The application provides functionality to:
- Generate RSA public and private keys.
- Encrypt messages using a given RSA public key.
- Decrypt messages using a corresponding RSA private key.
- Copy the generated keys to the clipboard for external and easier internal use.

Users can input strings directly and perform encryption or decryption operations.
Keys are displayed in the GUI and can be regenerated as needed.
This tool is intended for educational purposes to demonstrate RSA operations.

Functions:
- COPY_TO_CLIPBOARD(text): Copies the provided text to the clipboard.
- ENCRYPT_WRAPPER(): Fetches user inputs and encrypts the text using the RSA public key.
- DECRYPT_WRAPPER(): Decrypts the encrypted message using the RSA private key.
- GENERATE_AND_SHOW_KEYS(): Generates RSA keys and updates the GUI with these keys.

Author: Daniel-Ioan Mlesnita
Date: 11.06.2024
Version: 0.5
"""

import tkinter as tk
from tkinter import messagebox
from rsa_functionality import generate_keys, encrypt_message, decrypt_message

def copy_to_clipboard(text):
    """Copies a key (public or private) to user clipboard for easier save and use."""
    ROOT.clipboard_clear()
    ROOT.clipboard_append(text)
    ROOT.update()
    OUTPUT_TEXT.set("Your key has been copied to your clipboard.\n\n"
                    "Please save it somewhere to not lose it.")

def encrypt_wrapper():
    """Wraps the text and public key to send to the encryption function in RSA logic.
    Retrieves the result that is the encrypted text and copies it to clipboard."""

    input_text = ENTRY_ENCRYPT.get()
    public_key_str = ENTRY_PUB_KEY.get() #This is a string, for example "65537 12345678901234567890"

    try:
        e_str, n_str = public_key_str.split()
        pub_exponent = int(e_str)
        modulus = int(n_str)
        public_key = (pub_exponent, modulus)

        encrypted_message = encrypt_message(input_text, public_key)
        ROOT.clipboard_clear()
        ROOT.clipboard_append(encrypted_message)
        ROOT.update()
        OUTPUT_TEXT.set(f"The text has been encrypted and copied to your clipboard:"
                        f"{str(encrypted_message)[:15]}...")
    except ValueError as val_err:
        OUTPUT_TEXT.set(f"Invalid public key format."
                        f"Please enter as 'e n'. Error: {str(val_err)}")

def decrypt_wrapper():
    """Wraps the encrypted text and private key to send to the decryption function in RSA logic.
    Retrieves the result that is the decrypted text."""

    encrypted_text = ENTRY_DECRYPT.get()
    private_key_str = ENTRY_PRIV_KEY.get()

    try:
        d_str, n_str = private_key_str.split()
        priv_exponent = int(d_str)
        modulus = int(n_str)
        private_key = (priv_exponent, modulus)
        encrypted_int = int(encrypted_text)
        decrypted_message = decrypt_message(encrypted_int, private_key)
        OUTPUT_TEXT.set(decrypted_message)

    except ValueError as value_error:
        OUTPUT_TEXT.set(f"Invalid private key or ciphertext format."
                        f"Please ensure proper format. Error: {str(value_error)}")

def generate_and_show_keys():
    """Calls the key generation functions of the RSA logic and returns the keys."""
    ROOT.public_key, ROOT.private_key = generate_keys()
    messagebox.showinfo("Warning!", "Please do not share your private key!")

    ENTRY_PUB.delete(0, 'end')
    ENTRY_PRIV.delete(0, 'end')

    ENTRY_PUB.insert(0, ROOT.public_key)
    ENTRY_PRIV.insert(0, ROOT.private_key)

# Create the main window
ROOT = tk.Tk()
ROOT.title("Save my secret!!")

OUTPUT_TEXT = tk.StringVar()
OUTPUT_LABEL = tk.Label(ROOT, textvariable=OUTPUT_TEXT)

# Create widgets
ENCRYPT_TEXT = tk.Label(ROOT, text="Enter a string to encrypt:")
ENTRY_ENCRYPT = tk.Entry(ROOT, width=40)

PUBLIC_KEY = tk.Label(ROOT, text="Enter public key:")
ENTRY_PUB_KEY = tk.Entry(ROOT, width=40)

# Button for encryption, sending text to encrypt and public key
ENCRYPT_BUTTON = tk.Button(ROOT, text="Encrypt", command=encrypt_wrapper)

DECRYPT_TEXT = tk.Label(ROOT, text="Enter string to decrypt:")
ENTRY_DECRYPT = tk.Entry(ROOT, width=40)

PRIV_KEY_TEXT = tk.Label(ROOT, text="Enter private key:")
ENTRY_PRIV_KEY = tk.Entry(ROOT, width=40)

PUB_KEY_LABEL = tk.Label(ROOT, text="Your Public key:")
ENTRY_PUB = tk.Entry(ROOT, width=40)

PRIV_KEY_LABEL = tk.Label(ROOT, text="Your Private key:")
ENTRY_PRIV = tk.Entry(ROOT, width=40)

DECRYPT_BUTTON = tk.Button(ROOT, text="Decrypt", command=decrypt_wrapper)

COPY_PUB_KEY_BUTTON = tk.Button(ROOT,
                                text="Copy Public Key",
                                command=lambda: copy_to_clipboard(ENTRY_PUB.get()))
COPY_PRIV_KEY_BUTTON = tk.Button(ROOT,
                                 text="Copy Private Key",
                                 command=lambda: copy_to_clipboard(ENTRY_PRIV.get()))

GENERATE_KEYS_BUTTON = tk.Button(ROOT,
                                 text="Generate Encryption Keys",
                                 command=generate_and_show_keys)

# Layout widgets
ENCRYPT_TEXT.grid(row=0, column=0, padx=10, pady=10)
ENTRY_ENCRYPT.grid(row=0, column=1, padx=10, pady=10)
PUBLIC_KEY.grid(row=1, column=0, padx=10, pady=10)
ENTRY_PUB_KEY.grid(row=1, column=1, padx=10, pady=10)
DECRYPT_TEXT.grid(row=2, column=0, padx=10, pady=10)
ENTRY_DECRYPT.grid(row=2, column=1, padx=10, pady=10)
PRIV_KEY_TEXT.grid(row=3, column=0, padx=10, pady=10)
ENTRY_PRIV_KEY.grid(row=3, column=1, padx=10, pady=10)

ENCRYPT_BUTTON.grid(row=0, column=2, padx=10, pady=10)
DECRYPT_BUTTON.grid(row=2, column=2, padx=10, pady=10)
GENERATE_KEYS_BUTTON.grid(row=4, column=1, padx=10, pady=10)

PUB_KEY_LABEL.grid(row=6, column=0, padx=10, pady=10)
ENTRY_PUB.grid(row=6, column=1, padx=10, pady=10)
COPY_PUB_KEY_BUTTON.grid(row=6, column=2, padx=10, pady=10)
PRIV_KEY_LABEL.grid(row=7, column=0, padx=10, pady=10)
ENTRY_PRIV.grid(row=7, column=1, padx=10, pady=10)
COPY_PRIV_KEY_BUTTON.grid(row=7, column=2, padx=10, pady=10)

OUTPUT_LABEL.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

# Start the GUI event loop
ROOT.mainloop()
