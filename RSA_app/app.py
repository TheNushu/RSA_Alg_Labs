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
    OUTPUT_LABEL.config(fg='black')
    OUTPUT_TEXT.set("Your key has been copied to your clipboard.\n\n"
                    "Please save it somewhere to not lose it.")

def encrypt_wrapper():
    """Wraps the text and public key to send to the encryption function in RSA logic.
    Retrieves the result that is the encrypted text and copies it to clipboard."""
    OUTPUT_LABEL.config(fg='black')
    input_text = ENTRY_ENCRYPT.get("1.0","end-1c")
    text_bits = len(input_text.encode('utf-8'))
    key_bits = int(KEY_BITS.get('1.0', 'end-1c'))

    if text_bits >= key_bits:
        OUTPUT_LABEL.config(fg='red')
        OUTPUT_TEXT.set(f"Input text is {text_bits} bits, which a {key_bits} bit key cannot encrypt."
                        f"Please decrease input text or use bigger keys.")
        return

    public_key_str = ENTRY_PUB_KEY.get("1.0","end-1c") #This is a string, for example "65537 12345678901234567890"

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
        OUTPUT_LABEL.config(fg='red')
        OUTPUT_TEXT.set(f"Invalid public key format.")

def decrypt_wrapper():
    """Wraps the encrypted text and private key to send to the decryption function in RSA logic.
    Retrieves the result that is the decrypted text."""

    OUTPUT_LABEL.config(fg='black')
    encrypted_text = ENTRY_DECRYPT.get("1.0","end-1c")
    private_key_str = ENTRY_PRIV_KEY.get("1.0","end-1c")

    try:
        d_str, n_str = private_key_str.split()
        priv_exponent = int(d_str)
        modulus = int(n_str)
        private_key = (priv_exponent, modulus)
        encrypted_int = int(encrypted_text)
        decrypted_message = decrypt_message(encrypted_int, private_key)
        OUTPUT_TEXT.set(decrypted_message)

    except ValueError as value_error:
        OUTPUT_LABEL.config(fg='red')
        OUTPUT_TEXT.set(f"Invalid private key or ciphertext format."
                        f"Please ensure proper format.")

def generate_and_show_keys():
    """Calls the key generation functions of the RSA logic and returns the keys."""
    OUTPUT_LABEL.config(fg='black')
    bits = int(KEY_BITS.get("1.0","end-1c"))
    if bits % 2 != 0:
        OUTPUT_LABEL.config(fg='red')
        OUTPUT_TEXT.set(f"Key size should be a power of 2.")
        return
    ROOT.public_key, ROOT.private_key = generate_keys(bits)
    messagebox.showinfo("Warning!", "Please do not share your private key!")

    ENTRY_PUB.delete('1.0', 'end')
    ENTRY_PRIV.delete('1.0', 'end')

    ENTRY_PUB.insert('end', ROOT.public_key)
    ENTRY_PRIV.insert('end', ROOT.private_key)

# Create the main window
ROOT = tk.Tk()
ROOT.title("Save my secret!!")

OUTPUT_TEXT = tk.StringVar(ROOT, "Your text to be encrypted must have a smaller size (in bits) than the key size.")
OUTPUT_LABEL = tk.Label(ROOT, textvariable=OUTPUT_TEXT)

# Create widgets
ENCRYPT_TEXT = tk.Label(ROOT, text="Enter a string to encrypt:")
ENTRY_ENCRYPT = tk.Text(ROOT, width=60, height=7)

PUBLIC_KEY = tk.Label(ROOT, text="Enter public key:")
ENTRY_PUB_KEY = tk.Text(ROOT, width=60, height=7)

# Button for encryption, sending text to encrypt and public key
ENCRYPT_BUTTON = tk.Button(ROOT, text="Encrypt", command=encrypt_wrapper)

DECRYPT_TEXT = tk.Label(ROOT, text="Enter string to decrypt:")
ENTRY_DECRYPT = tk.Text(ROOT, width=60, height=7)

PRIV_KEY_TEXT = tk.Label(ROOT, text="Enter private key:")
ENTRY_PRIV_KEY = tk.Text(ROOT, width=60, height=7)

PUB_KEY_LABEL = tk.Label(ROOT, text="Your Public key:")
ENTRY_PUB = tk.Text(ROOT, width=60, height=5)

PRIV_KEY_LABEL = tk.Label(ROOT, text="Your Private key:")
ENTRY_PRIV = tk.Text(ROOT, width=60, height=5)

DECRYPT_BUTTON = tk.Button(ROOT, text="Decrypt", command=decrypt_wrapper)

COPY_PUB_KEY_BUTTON = tk.Button(ROOT,
                                text="Copy Public Key",
                                command=lambda: copy_to_clipboard(ENTRY_PUB.get("1.0","end-1c")))
COPY_PRIV_KEY_BUTTON = tk.Button(ROOT,
                                 text="Copy Private Key",
                                 command=lambda: copy_to_clipboard(ENTRY_PRIV.get("1.0","end-1c")))

GENERATE_KEYS_BUTTON = tk.Button(ROOT,
                                 text="Generate Encryption Keys with size (in bits): ",
                                 command=generate_and_show_keys)

KEY_BITS = tk.Text(ROOT, width=6, height=1)
KEY_BITS.insert('end', '1024') # default key size is 1024 bits

# Layout widgets
ENCRYPT_TEXT.grid(row=0, column=0, padx=10, pady=10)
ENTRY_ENCRYPT.grid(row=0, column=1, padx=10, pady=5, sticky="ew")
PUBLIC_KEY.grid(row=1, column=0, padx=10, pady=10)
ENTRY_PUB_KEY.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
DECRYPT_TEXT.grid(row=2, column=0, padx=10, pady=10)
ENTRY_DECRYPT.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")
PRIV_KEY_TEXT.grid(row=3, column=0, padx=10, pady=10)
ENTRY_PRIV_KEY.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

ENCRYPT_BUTTON.grid(row=0, column=2, padx=10, pady=10)
DECRYPT_BUTTON.grid(row=2, column=2, padx=10, pady=10)
GENERATE_KEYS_BUTTON.grid(row=4, column=1, padx=(10, 0), pady=10, sticky='w')
KEY_BITS.grid(row=4, column=1, padx=(350, 10), pady=10, sticky='w')


PUB_KEY_LABEL.grid(row=6, column=0, padx=10, pady=10)
ENTRY_PUB.grid(row=6, column=1, padx=10, pady=10,sticky="nsew")
COPY_PUB_KEY_BUTTON.grid(row=6, column=2, padx=10, pady=10)
PRIV_KEY_LABEL.grid(row=7, column=0, padx=10, pady=10)
ENTRY_PRIV.grid(row=7, column=1, padx=10, pady=10,sticky="nsew")
COPY_PRIV_KEY_BUTTON.grid(row=7, column=2, padx=10, pady=10)

OUTPUT_LABEL.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

# Make the application full-screen

screen_width = ROOT.winfo_screenwidth()
screen_height = ROOT.winfo_screenheight()
ROOT.geometry(f'{screen_width}x{screen_height}+0+0')

for i in range(8):
    ROOT.grid_rowconfigure(i, weight=1)
for j in range(3):
    ROOT.grid_columnconfigure(j, weight=1)

# Start the GUI event loop
ROOT.mainloop()
