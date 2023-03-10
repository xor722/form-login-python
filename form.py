import tkinter as tk

def check_credentials():
    username = username_entry.get()
    password = password_entry.get()
    if username == "xor722" and password == "follow":
        login_status.config(text="Login Berhasil", fg="green")
    else:
        login_status.config(text="Username atau Password Salah", fg="red")


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

# Buat tombol login
login_button = tk.Button(window, text="Login", command=check_credentials)
login_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# buat status login
login_status = tk.Label(window, text="")
login_status.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()