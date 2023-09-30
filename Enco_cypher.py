import tkinter as tk
from tkinter import ttk
import base64
import random

class EncoderDecoderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Encoder and Decoder")

        self.create_widgets()

    def create_widgets(self):
        # Text input
        self.input_label = ttk.Label(self.root, text="Enter Text:")
        self.input_label.grid(row=0, column=0, padx=5, pady=5)
        self.input_text = ttk.Entry(self.root, width=40)
        self.input_text.grid(row=0, column=1, columnspan=2, padx=5, pady=5)

        # Algorithm selection
        self.algorithm_label = ttk.Label(self.root, text="Select Algorithm:")
        self.algorithm_label.grid(row=1, column=0, padx=5, pady=5)
        self.algorithm_var = tk.StringVar()
        self.algorithm_dropdown = ttk.Combobox(self.root, textvariable=self.algorithm_var, values=["Base64", "Caesar Cipher", "Custom"])
        self.algorithm_dropdown.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

        # Encode and Decode buttons
        self.encode_button = ttk.Button(self.root, text="Encode", command=self.encode_text)
        self.encode_button.grid(row=2, column=1, padx=5, pady=5)
        self.decode_button = ttk.Button(self.root, text="Decode", command=self.decode_text)
        self.decode_button.grid(row=2, column=2, padx=5, pady=5)

        # Output display
        self.output_label = ttk.Label(self.root, text="Result:")
        self.output_label.grid(row=3, column=0, padx=5, pady=5)
        self.output_text = tk.Text(self.root, height=5, width=40)
        self.output_text.grid(row=3, column=1, columnspan=2, padx=5, pady=5)

    def encode_text(self):
        input_text = self.input_text.get()
        algorithm = self.algorithm_var.get()

        if algorithm == "Base64":
            encoded_text = base64.b64encode(input_text.encode()).decode()
        elif algorithm == "Caesar Cipher":
            shift = random.randint(1, 25)  # Random shift for demonstration purposes
            encoded_text = self.caesar_cipher(input_text, shift)
        elif algorithm == "Custom":
            # Implement your custom encoding algorithm here
            encoded_text = "Custom Encoding: " + input_text
        else:
            encoded_text = "Invalid algorithm"

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, encoded_text)

    def decode_text(self):
        input_text = self.input_text.get()
        algorithm = self.algorithm_var.get()

        if algorithm == "Base64":
            try:
                decoded_text = base64.b64decode(input_text).decode()
            except Exception as e:
                decoded_text = f"Error decoding: {str(e)}"
        elif algorithm == "Caesar Cipher":
            shift = random.randint(1, 25)  # Same shift used for encoding
            decoded_text = self.caesar_cipher(input_text, -shift)
        elif algorithm == "Custom":
            # Implement your custom decoding algorithm here
            decoded_text = "Custom Decoding: " + input_text
        else:
            decoded_text = "Invalid algorithm"

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, decoded_text)

    @staticmethod
    def caesar_cipher(text, shift):
        result = ""
        for char in text:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            else:
                result += char
        return result

if __name__ == "__main__":
    root = tk.Tk()
    app = EncoderDecoderApp(root)
    root.mainloop()
