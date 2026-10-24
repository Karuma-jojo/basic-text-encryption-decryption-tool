import tkinter as tk
from tkinter import ttk, messagebox
import caeser


def encrypt_message():
    result_box.delete("1.0", "end")

    try:
        shift = int(shift_box.get())
    except ValueError:
        messagebox.showerror("Invalid shift", "Enter a whole number, such as 6.")
        shift_box.focus_set()
        return

    text = message_box.get("1.0", "end-1c")
    result = caeser.encrypt(text, shift)
    result_box.insert("1.0", result)


window = tk.Tk()
window.title("Text Encryption Tool")
window.geometry("640x560")
window.minsize(500, 480)

panel = ttk.Frame(window, padding=24)
panel.pack(fill="both", expand=True)

ttk.Label(panel, text="Caesar cipher", font=("Segoe UI", 20, "bold")).pack(
    anchor="w", pady=(0, 18)
)

ttk.Label(panel, text="Your message").pack(anchor="w")
message_box = tk.Text(panel, height=5, wrap="word", font=("Segoe UI", 11))
message_box.pack(fill="both", expand=True, pady=(6, 16))

ttk.Label(panel, text="Shift").pack(anchor="w")
shift_box = ttk.Entry(panel)
shift_box.insert(0, "6")
shift_box.pack(fill="x", pady=(6, 16))

ttk.Button(panel, text="Encrypt", command=encrypt_message, padding=8).pack(
    fill="x", pady=(0, 16)
)

ttk.Label(panel, text="Encrypted result").pack(anchor="w")
result_box = tk.Text(panel, height=5, wrap="word", font=("Segoe UI", 11))
result_box.pack(fill="both", expand=True, pady=(6, 0))

message_box.focus_set()
window.mainloop()
