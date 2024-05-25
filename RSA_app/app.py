
import tkinter as tk
from rsa_functionality import generate_keys, encrypt_message, decrypt_message

def function1():
    input_text = entry1.get()
    result = input_text[::-1]
    output_text.set(result)

def function2():
    input_text1 = entry2.get()
    input_text2 = entry3.get()
    result = input_text1 + " " + input_text2  
    output_text.set(result)



# Create the main window
root = tk.Tk()
root.title("Save my secret!!")

output_text = tk.StringVar()
output_label = tk.Label(root, textvariable=output_text)

# Create widgets
label1 = tk.Label(root, text="Enter a string to encrypt:")
entry1 = tk.Entry(root, width=50)

label2 = tk.Label(root, text="Enter public key:") 
entry2 = tk.Entry(root, width=25) 

#button for encryption, sending text to encrypt and public key
button1 = tk.Button(root, text="Encrypt", command=encrypt_message(entry1, entry2, output_text)) 

label3 = tk.Label(root, text="Enter string to decrypt:")
entry3 = tk.Entry(root, width=25)

label4 = tk.Label(root, text="Enter private key:")
entry4 = tk.Entry(root, width=25)

button2 = tk.Button(root, 
                    text="Decrypt", 
                    command=decrypt_message(entry3, entry4))

button3 = tk.Button(root, 
                    text="Generate pair of keys", 
                    command=generate_keys)


# Layout widgets
label1.grid(row=0, column=0, padx=10, pady=10)
entry1.grid(row=0, column=1, padx=10, pady=10)
button1.grid(row=0, column=2, padx=10, pady=10)

label2.grid(row=1, column=0, padx=10, pady=10)
entry2.grid(row=1, column=1, padx=10, pady=10)

label3.grid(row=2, column=0, padx=10, pady=10)
entry3.grid(row=2, column=1, padx=10, pady=10)

label4.grid(row=4, column=0, padx=10, pady=10)
entry4.grid(row=4, column=1, padx=10, pady=10)


button2.grid(row=1, column=2, rowspan=2, padx=10, pady=10)

button3.grid(row=5, column=1, padx=10, pady=10)  

output_label.grid(row=3, column=0, 
                  columnspan=3, padx=10, 
                  pady=10)

# Start the GUI event loop
root.mainloop()



'''import tkinter as tk
from tkinter import messagebox
import rsa

class RSAApp:
    def __init__(self, master):
        self.master = master
        self.master.title("RSA Encryption Tool")
        self.public_key = None
        self.private_key = None

        self.txt_message = tk.Text(master, height=5, width=50)
        self.txt_message.pack(pady=5)

        self.txt_encrypted = tk.Text(master, height=5, width=50)
        self.txt_encrypted.pack(pady=5)

        self.txt_decrypted = tk.Text(master, height=5, width=50)
        self.txt_decrypted.pack(pady=5)

        tk.Button(master, text="Generate Keys", command=self.generate_keys_command).pack(pady=5)
        tk.Button(master, text="Encrypt", command=self.encrypt_message).pack(pady=5)
        tk.Button(master, text="Decrypt", command=self.decrypt_message).pack(pady=5)

    def generate_keys_command(self):
        self.public_key, self.private_key = rsa.newkeys(512)
        print(self.private_key)
        print(self.public_key)
        messagebox.showinfo("Keys", "Keys generated successfully!")

    def encrypt_message(self):
        encoded = message.encode("utf8")
        message = encoded.get("1.0", "end-1c")
        if not self.public_key:
            messagebox.showerror("Error", "Generate keys first!")
            return
        encrypted_msg = rsa.encrypt(message, self.public_key)
        self.txt_encrypted.delete("1.0", tk.END)
        self.txt_encrypted.insert(tk.END, encrypted_msg)

    def decrypt_message(self):
        encrypted_message = self.txt_encrypted.get("1.0", "end-1c")
        if not self.private_key:
            messagebox.showerror("Error", "Generate keys first!")
            return
        decrypted_msg = rsa.decrypt(encrypted_message, self.private_key)
        self.txt_decrypted.delete("1.0", tk.END)
        self.txt_decrypted.insert(tk.END, decrypted_msg)

app = tk.Tk()
rsa_app = RSAApp(app)
app.mainloop()
'''