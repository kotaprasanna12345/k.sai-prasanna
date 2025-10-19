import tkinter as tk
from tkinter import messagebox

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def process_text():
    text = entry_text.get()
    try:
        shift = int(entry_shift.get())
        if shift < 1 or shift > 25:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Shift", "Please enter a shift value between 1 and 25.")
        return

    if mode.get() == "Encrypt":
        result = caesar_encrypt(text, shift)
    else:
        result = caesar_decrypt(text, shift)

    output_label.config(text=f"Result: {result}")

# GUI setup
root = tk.Tk()
root.title("Caesar Cipher App")

tk.Label(root, text="Enter text:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_text = tk.Entry(root, width=40)
entry_text.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Shift value (1-25):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_shift = tk.Entry(root, width=5)
entry_shift.grid(row=1, column=1, padx=10, pady=5, sticky="w")

mode = tk.StringVar(value="Encrypt")
tk.Radiobutton(root, text="Encrypt", variable=mode, value="Encrypt").grid(row=2, column=0, padx=10, pady=5)
tk.Radiobutton(root, text="Decrypt", variable=mode, value="Decrypt").grid(row=2, column=1, padx=10, pady=5, sticky="w")

tk.Button(root, text="Process", command=process_text).grid(row=3, column=0, columnspan=2, pady=10)

output_label = tk.Label(root, text="Result: ", fg="blue")
output_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop() 