
import tkinter as tk
from tkinter import messagebox
from rsa_functionality import generate_keys, encrypt_message, decrypt_message

def copy_to_clipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update() 

    output_text.set("Your key has been copied to your clipboard.\n\n"
                        "Please save it somewhere to not lose it.")

def encrypt_wrapper():
    input_text = entry1.get()
    public_key_str = entry2.get()  # This is a string, for example "65537 12345678901234567890"
    
    try:
        # Splitting the string into components and converting to integers
        e_str, n_str = public_key_str.split()
        e = int(e_str)
        n = int(n_str)
        public_key = (e, n)

        encrypted_message = encrypt_message(input_text, public_key)
        
        #we copy the encrypted text now for testing
        #later specific ui to copy encrypted text
        root.clipboard_clear()
        root.clipboard_append(encrypted_message)
        root.update() 
        
        output_text.set(f"The text has been encrypted and copied to your clipboard: {str(encrypted_message)[0:15]}")
    except ValueError as ve:
        output_text.set(f"Invalid public key format. Please enter as 'e n'. Error: {str(ve)}")
    except Exception as e:
        output_text.set(f"Error: {str(e)}")


def decrypt_wrapper():
    encrypted_text = entry3.get()  # This is the encrypted integer as a string
    private_key_str = entry4.get()  # This is a string, for example "d n"

    try:
        # Splitting the string into components and converting to integers
        d_str, n_str = private_key_str.split()
        d = int(d_str)
        n = int(n_str)
        private_key = (d, n)

        # Convert the encrypted text back to integer
        encrypted_int = int(encrypted_text)  

        decrypted_message = decrypt_message(encrypted_int, private_key)
        output_text.set(decrypted_message)
    except ValueError as ve:
        output_text.set(f"Invalid private key or ciphertext format. Please ensure proper format. Error: {str(ve)}")
    except Exception as e:
        output_text.set(f"Error: {str(e)}")


def generate_and_show_keys():
    root.public_key, root.private_key = generate_keys()

    messagebox.showinfo("Warning!", 
                           "Please do not share your private key!")
    
    entry_pub.insert(0, root.public_key)
    entry_priv.insert(0, root.private_key)
    

# Create the main window
root = tk.Tk()
root.title("Save my secret!!")

output_text = tk.StringVar()
output_label = tk.Label(root, textvariable=output_text)

# Create widgets
label1 = tk.Label(root, text="Enter a string to encrypt:")
entry1 = tk.Entry(root, width=40)

label2 = tk.Label(root, text="Enter public key:") 
entry2 = tk.Entry(root, width=40) 

#button for encryption, sending text to encrypt and public key
button1 = tk.Button(root, 
                    text="Encrypt", 
                    command=encrypt_wrapper) 

label3 = tk.Label(root, text="Enter string to decrypt:")
entry3 = tk.Entry(root, width=40)

label4 = tk.Label(root, text="Enter private key:")
entry4 = tk.Entry(root, width=40)

label_pub = tk.Label(root, text="Your Public key:")
entry_pub = tk.Entry(root, width=40)

label_priv = tk.Label(root, text="Your Private key:")
entry_priv = tk.Entry(root, width=40)

button2 = tk.Button(root, 
                    text="Decrypt", 
                    command=decrypt_wrapper)

button_copy_public_key = tk.Button(root, 
                                   text="Copy Public Key", 
                                   command=lambda: 
                                    copy_to_clipboard(
                                         entry_pub.get()
                                         )
                                    )

button_copy_private_key = tk.Button(root, 
                                    text="Copy Private Key", 
                                    command=lambda: 
                                     copy_to_clipboard(
                                         entry_priv.get()
                                         )
                                    )

button3 = tk.Button(root, 
                    text="Generate Encryption Keys", 
                    command=generate_and_show_keys
                    )


# Layout widgets
label1.grid(row=0, column=0, padx=10, pady=10)
entry1.grid(row=0, column=1, padx=10, pady=10)

label2.grid(row=1, column=0, padx=10, pady=10)
entry2.grid(row=1, column=1, padx=10, pady=10)

label3.grid(row=2, column=0, padx=10, pady=10)
entry3.grid(row=2, column=1, padx=10, pady=10)

label4.grid(row=3, column=0, padx=10, pady=10)
entry4.grid(row=3, column=1, padx=10, pady=10)

button1.grid(row=0, column=2, padx=10, pady=10)

button2.grid(row=2, column=2, padx=10, pady=10)

button3.grid(row=4, column=1, padx=10, pady=10)

label_pub.grid(row=6, column=0, padx=10, pady=10)
entry_pub.grid(row=6, column=1, padx=10, pady=10)

button_copy_public_key.grid(row=6, column=2, padx=10, pady=10)

label_priv.grid(row=7, column=0, padx=10, pady=10)
entry_priv.grid(row=7, column=1, padx=10, pady=10)

button_copy_private_key.grid(row=7, column=2, padx=10, pady=10)

output_label.grid(row=5, column=0, 
                  columnspan=3, padx=10, 
                  pady=10)

# Placeholder for dynamic widgets to prevent AttributeError
root.label_pub = None
root.entry_pub = None
root.label_priv = None
root.entry_priv = None

# Start the GUI event loop
root.mainloop()
