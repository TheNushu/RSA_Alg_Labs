from tkinter import messagebox, simpledialog
import rsa

def generate_keys():
    public_key, private_key = rsa.newkeys(1024)
    
    messagebox.showinfo("Keys!", 
                        f"Your public key is:\n{public_key}\n\n"
                        f"Your private key is:\n{private_key}\n\n"
                        "Please do not share your private key! :D")

def encrypt_message(entry_text, entry_public_key):
    return f"Hey your text: {entry_text} is encrypted with: {entry_public_key}"

def decrypt_message(entry_text, entry_private_key):
    return f"Hey your private text: {entry_text} is decrypted with: {entry_private_key}"
