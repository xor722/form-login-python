import tkinter as tk
from PIL import Image, ImageTk
import base64

def check_credentials():
    username = username_entry.get()
    password = password_entry.get()
    if username == "xor722":
        login_status.config(text="Login Berhasil", fg="green")
    else:
        login_status.config(text="Username atau Password Salah", fg="red")

def toggle_password_visibility():
    global show_password
    show_password = not show_password
    password_entry.config(show="" if show_password else "*")
    show_hide_button.config(image=hide_icon if show_password else show_icon)

window = tk.Tk()
window.title("Form Login")

# Buat label Username dan input
username_label = tk.Label(window, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
username_entry = tk.Entry(window)
username_entry.grid(row=0, column=1, padx=5, pady=5)

# Buat label Password dan input
password_label = tk.Label(window, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
password_entry = tk.Entry(window, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

# Buat tombol Show/Hide Password
show_password = False
show_image = Image.open("E:/New folder/show_password.png").resize((25, 25))
hide_image = Image.open("E:/New folder/hide_password.png").resize((25, 25))
show_icon = ImageTk.PhotoImage(show_image)
hide_icon = ImageTk.PhotoImage(hide_image)
show_hide_button = tk.Button(window, image=show_icon, command=toggle_password_visibility, bd=0)
show_hide_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Buat tombol login
login_button = tk.Button(window, text="Login", command=check_credentials)
login_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# buat status login
login_status = tk.Label(window, text="")
login_status.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# konversi gambar menjadi base64
with open("E:/New folder/show_password.png", "rb") as f:
    show_icon_base64 = base64.b64encode(f.read())
with open("E:/New folder/hide_password.png", "rb") as f:
    hide_icon_base64 = base64.b64encode(f.read())

# simpan gambar dalam format base64
with open("show_icon_base64.txt", "wb") as f:
    f.write(show_icon_base64)
with open("hide_icon_base64.txt", "wb") as f:
    f.write(hide_icon_base64)

window.mainloop()
