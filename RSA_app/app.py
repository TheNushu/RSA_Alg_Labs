
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
button1 = tk.Button(root, 
                    text="Encrypt", 
                    command=encrypt_message(entry1, entry2, output_text)) 

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
