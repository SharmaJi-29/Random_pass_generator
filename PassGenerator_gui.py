import tkinter as tk
from tkinter import messagebox
import random



class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
        self.uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.digits = '1234567890'
        self.special_characters = '`~!@#$%^&*()-_=+[]{}\|;:,.></?'

        self.create_widgets()


    def create_widgets(self):
        self.root.geometry("400x500")

        self.entry_label = tk.Label(self.root, text="Enter Length of Password:", font=('verdana', 20, 'bold'))
        self.entry_label.pack(pady=60)

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.create_password)
        self.submit_button.pack(pady=10)

        self.pass_label = tk.Label(self.root, text="")
        self.pass_label.pack(pady=10)

    def create_password(self):
        try:

            length = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Length must be an integer.")
            return

        if length <= 5 :
            messagebox.showerror("Invalid input", "Password is too short.")
            return

        self.password = [random.choice(self.lowercase_letters),
                         random.choice(self.uppercase_letters),
                         random.choice(self.digits),
                         random.choice(self.special_characters)]

        self.all_string = self.lowercase_letters + self.uppercase_letters + self.digits + self.special_characters
        self.password += random.choices(self.all_string, k = length - 4)
        random.shuffle(self.password)

        self.pass_label.config(text=f"Your Generated Password is: {''.join(self.password)}")


if __name__ == "__main__":
    root = tk.Tk()
    game = PasswordGenerator(root)
    root.mainloop()