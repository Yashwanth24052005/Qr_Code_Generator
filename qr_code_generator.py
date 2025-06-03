import qrcode
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import os

def generate_qr():
    link = entry.get()
    if not link.strip():
        messagebox.showerror("Input Error", "Please enter a valid link.")
        return

    qr_code = qrcode.make(link)
    qr_code_path = "link.png"
    qr_code.save(qr_code_path)

    # Display QR in GUI
    img = Image.open(qr_code_path)
    img = img.resize((250, 250))
    img = ImageTk.PhotoImage(img)
    qr_label.config(image=img)
    qr_label.image = img

    messagebox.showinfo("Success", f"QR Code saved as {qr_code_path}")

# GUI Setup
root = tk.Tk()
root.title("Stylish QR Code Generator")
root.geometry("400x550")
root.configure(bg="#f0f4f7")

# Title
tk.Label(root, text="QR Code Generator", font=("Helvetica", 18, "bold"), bg="#f0f4f7", fg="#333").pack(pady=20)

# Frame for Input
frame = tk.Frame(root, bg="#f0f4f7")
frame.pack(pady=10)

tk.Label(frame, text="Enter Link:", font=("Helvetica", 12), bg="#f0f4f7", fg="#333").grid(row=0, column=0, padx=5, pady=5)

entry = ttk.Entry(frame, width=35)
entry.grid(row=1, column=0, padx=10, pady=10)

# Generate Button
style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=6)
generate_btn = ttk.Button(root, text="Generate QR Code", command=generate_qr)
generate_btn.pack(pady=10)

# QR Code Display Label
qr_label = tk.Label(root, bg="#f0f4f7")
qr_label.pack(pady=20)

# Footer
tk.Label(root, text="Created with ❤️ using Python", font=("Helvetica", 10), bg="#f0f4f7", fg="#888").pack(pady=10)

root.mainloop()
