import tkinter as tk
import random
from tkinter import *


def generate_license_key():
    weights = {
        "A": 2,
        "B": 3,
        "C": 4,
        "D": 5,
        "E": 6,
        "F": 7,
        "G": 8,
        "H": 9,
        "I": 10,
        "J": 11,
        "K": 12,
        "L": 13,
        "M": 14,
        "N": 15,
        "O": 16,
        "P": 17,
        "Q": 18,
        "R": 19,
        "S": 20,
        "T": 21,
        "U": 22,
        "V": 23,
        "W": 24,
        "X": 25,
        "Y": 26,
        "Z": 27,
        "1": 28,
        "2": 29,
        "3": 30,
        "4": 31,
        "5": 32,
        "6": 33,
        "7": 34,
        "8": 35,
        "9": 36,
        "0": 37
    }

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"

    generation_steps = 3
    current_step = 1
    result_key = list()

    start_limit = 80
    end_limit = 84

    while current_step <= generation_steps:
        key = "".join(random.choices(alphabet, k=4))
        weight_sum = sum(weights[char] for char in key)

        while weight_sum < start_limit or weight_sum > end_limit:
            key = "".join(random.choices(alphabet, k=4))
            weight_sum = sum(weights[char] for char in key)

        formatted_key = "-".join([key[i:i+4] for i in range(0, len(key), 4)])
        result_key.append(formatted_key)

        current_step += 1

    key_to_send = f'{result_key[0]}-{result_key[1]}-{result_key[2]}'
    key_code_entry.delete(1.0, tk.END)
    key_code_entry.insert(tk.END, key_to_send)


window = tk.Tk()
window.geometry("500x200")
window.title("Stronghold 2 License Key Generator")

bg = PhotoImage(file="bg.png")

key_code_label = tk.Label(
    window, text="License Key Code:", font=("Arial", 12), image=bg)

key_code_label.pack()
key_code_entry = tk.Text(window, font=("Arial", 12), height=1, width=15)
key_code_entry.pack()

generate_button = tk.Button(window, text="Generate Key", font=(
    "Arial", 12), command=generate_license_key)
generate_button.pack()

window.mainloop()
