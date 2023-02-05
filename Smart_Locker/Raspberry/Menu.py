import tkinter as tk
import csv
import os
import tkinter.messagebox
from os import system

def abrir_locker():
    # Código para abrir el locker
    system(f"lxterminal -e python3 Abrir_locker.py")
    pass

def registro_nuevo():
    # Código para abrir el script de registro de nuevo usuario
    system(f"lxterminal -e python3 Registro_nuevo.py")
    pass

def admin():
    usuario = admin_usuario_entry.get()
    contrasena = admin_contrasena_entry.get()

    if os.path.exists('.Administrator/Admin.csv'):
        with open('.Administrator/Admin.csv', 'r') as archivo_csv:
            reader = csv.DictReader(archivo_csv)
            for fila in reader:
                if fila['Username'] == usuario and fila['Contraseña'] == contrasena:
                    exec(open("Admin.py").read())
                    #system(f"lxterminal -e python3 Admin.py")
                    return
    tkinter.messagebox.showerror('Admin', 'Credenciales incorrectas')

root = tk.Tk()
root.title("Menú principal")
root.attributes('-fullscreen', True)

abrir_locker_boton = tk.Button(root, text="Abrir locker", command=abrir_locker)
abrir_locker_boton.pack()

registro_nuevo_boton = tk.Button(root, text="Registro nuevo", command=registro_nuevo)
registro_nuevo_boton.pack()

admin_label = tk.Label(root, text="Usuario (Admin):")
admin_label.pack()

admin_usuario_entry = tk.Entry(root)
admin_usuario_entry.pack()

admin_contrasena_label = tk.Label(root, text="Contraseña (Admin):")
admin_contrasena_label.pack()

admin_contrasena_entry = tk.Entry(root, show="*")
admin_contrasena_entry.pack()

admin_boton = tk.Button(root, text="Modo Admin", command=admin)
admin_boton.pack()

root.mainloop()