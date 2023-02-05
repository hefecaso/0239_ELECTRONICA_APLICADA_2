# Truzz Blogg | Python + Tkinter | How to create a GUI
# How to create a registration form using Python + Tkinter

# Let's import tkinter 
from tkinter import *
#import tkinter as tk
import cv2
import os

# Manipulate data from registration fields 
def send_data():

	username_info = username.get()
	password_info = password.get()
	locker_info = locker.get()
	dpi_info = dpi.get()
	print(username_info,"\t", password_info,"\t", locker_info,"\t", dpi_info)
 
	#  Open and write data to a file
	#file = open(f".Datos_usuarios/{username_info}.csv", "a" agregar información al final de lo que ya exista en el archivo)
	#file = open(f".Datos_usuarios/{username_info}.csv", "w" para escribir en el archivo)
	file = open(f".Datos_usuarios/usuarios.csv", "a")
	file.write(username_info)
	file.write(",")
	# la \t es para dar un tabulado
	file.write(password_info)
	file.write(",")
	file.write(locker_info)
	file.write(",")
	file.write(dpi_info)
	file.write("\n")
	file.close()
	print("Nuevo usuario registrado. \nUsername: {} | Locker: #{}   ".format(username_info, locker_info))

	#  Delete data from previous event
	username_entry.delete(0, END)
	password_entry.delete(0, END)
	locker_entry.delete(0, END)
	dpi_entry.delete(0, END)

# Create new instance - Class Tk()  
ventana = Tk()
ventana.geometry("650x550")
ventana.title("Modo usuario | SMART LOCKER")
ventana.resizable(False,False)
ventana.config(background = "#e6e8e7")
main_title = Label(text = "Prueba de formulario | SMART LOCKER", font = ("Cambria", 14), bg = "#bbbdbc", fg = "black", width = "500", height = "2")
main_title.pack()

# Define Label Fields 
username_label = Label(text = "Usuario", bg = "#FFEEDD")
username_label.place(x = 22, y = 70)
password_label = Label(text = "Contraseña", bg = "#FFEEDD")
password_label.place(x = 22, y = 130)
locker_label = Label(text = "Número de locker", bg = "#FFEEDD")
locker_label.place(x = 22, y = 190)
dpi_label = Label(text = "Número de dpi", bg = "#FFEEDD")
dpi_label.place(x = 22, y = 250)
 
# Get and store data from users 
username = StringVar()
password = StringVar()
locker = StringVar()
dpi = StringVar()
#dpi = IntVar()
 
username_entry = Entry(textvariable = username, width = "40")
password_entry = Entry(textvariable = password, width = "40",  show = "*")
locker_entry = Entry(textvariable = locker, width = "40")
dpi_entry = Entry(textvariable = dpi, width = "40")
 
username_entry.place(x = 22, y = 100)
password_entry.place(x = 22, y = 160)
locker_entry.place(x = 22, y = 220)
dpi_entry.place(x = 22, y = 280)
 
# Submit Button
submit_btn = Button(ventana,text = "Aceptar", width = "30", height = "2", command = send_data, background ="#bbbdbc")
salir = Button(ventana,text = "Salir", width = "30", height = "2", command = ventana.destroy, background ="#bbbdbc")


submit_btn.place(x = 22, y = 320)
salir.place(x = 22, y = 381)


ventana.mainloop()

