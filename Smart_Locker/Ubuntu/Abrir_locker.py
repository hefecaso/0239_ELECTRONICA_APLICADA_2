import tkinter as tk
import csv
import os
import tkinter.messagebox

def ingresar():
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()

    if os.path.exists('.Datos_usuarios/usuarios.csv'):
        with open('.Datos_usuarios/usuarios.csv', 'r') as archivo_csv:
            reader = csv.DictReader(archivo_csv)
            for fila in reader:
                if fila['Username'] == usuario and fila['Contraseña'] == contrasena:
                    tkinter.messagebox.showinfo('Locker', 'Locker abierto')
                    root.destroy()
                    return
    tkinter.messagebox.showerror('Locker', 'Credenciales incorrectas')

root = tk.Tk()
root.title("Acceso a locker")
root.geometry("400x200")

usuario_label = tk.Label(root, text="Usuario:")
usuario_label.pack()

usuario_entry = tk.Entry(root)
usuario_entry.pack()

contrasena_label = tk.Label(root, text="Contraseña:")
contrasena_label.pack()

contrasena_entry = tk.Entry(root, show="*")
contrasena_entry.pack()

ingresar_boton = tk.Button(root, text="Ingresar", command=ingresar)
ingresar_boton.pack()

root.mainloop()
