import os
import tkinter as tk

def abrir_administrator():
    os.system("xdg-open .Administrator")
    
def abrir_usuarios():
    os.system("xdg-open .Datos_usuarios")

def admin_nuevo():
    # Código para abrir el script de registro de nuevo usuario
    #exec(open("Admin_nuevo.py").read())
    system(f"lxterminal -e python3 Admin_nuevo.py")
    pass

def cerrar_todo():
    os.system("python3 Cerrar_todo.py")
    
root = tk.Tk()
root.title("Ventana admin")
root.geometry("200x200")

administrator_button = tk.Button(root, text="Abrir Administrator", command=abrir_administrator)
administrator_button.pack()

usuarios_button = tk.Button(root, text="Abrir Usuarios", command=abrir_usuarios)
usuarios_button.pack()

Admin_nuevo_button = tk.Button(root, text="Agregar nuevo administrador", command=admin_nuevo)
Admin_nuevo_button.pack()

cerrar_todo_button = tk.Button(root, text="Cerrar Todo", command=cerrar_todo)
cerrar_todo_button.pack()

root.mainloop()