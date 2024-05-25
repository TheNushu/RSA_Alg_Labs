from tkinter import messagebox, simpledialog
import rsa

def generate_keys():
    public_key, private_key = rsa.newkeys(512)
    
    messagebox.showinfo("Keys!", 
                        f"Your public key is:\n{public_key}\n\n"
                        f"Your private key is:\n{private_key}\n\n"
                        "Please do not share your private key! :D")

def encrypt_message(entry_text, entry_public_key, output_text):
    
    pass
    '''
    text = entry_text.get()
    public_key = entry_public_key.get()
    
    output_text.set(f"{text[::-1]} {public_key[::-1]}")
    '''

   

def decrypt_message(entry_text, entry_private_key):
    pass