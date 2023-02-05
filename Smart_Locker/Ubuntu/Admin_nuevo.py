import csv
import os
import tkinter as tk
from tkinter import filedialog


def register_user():
    user = username_entry.get()
    locker = locker_entry.get()
    dpi = dpi_entry.get()
    password = password_entry.get()

    # Guardar datos en csv
    with open(".Administrator/Admin.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([user, locker, dpi, password])

    # Cerrar ventana de registro
    root.destroy()

# Interfaz gráfica en tkinter
root = tk.Tk()
root.title("Registro de nuevo administrador")

username_label = tk.Label(root, text="Usuario:")
username_label.grid(row=0, column=0)

username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1)

locker_label = tk.Label(root, text="Número de locker:")
locker_label.grid(row=1, column=0)

locker_entry = tk.Entry(root)
locker_entry.grid(row=1, column=1)

dpi_label = tk.Label(root, text="Número de dpi:")
dpi_label.grid(row=2, column=0)

dpi_entry = tk.Entry(root)
dpi_entry.grid(row=2, column=1)

password_label = tk.Label(root, text="Contraseña:")
password_label.grid(row=3, column=0)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=3, column=1)

register_button = tk.Button(root, text="Registrar", command=register_user)
register_button.grid(row=4, column=0, columnspan=2)

root.mainloop()
