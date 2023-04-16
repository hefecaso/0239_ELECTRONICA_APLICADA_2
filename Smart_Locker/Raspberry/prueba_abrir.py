import tkinter as tk
import csv
import os
import cv2
import tkinter.messagebox
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# Configuración de los pines de salida para las cerraduras
cerradura_pins = [7, 29, 31, 24, 26]
for pin in cerradura_pins:
    GPIO.setup(pin, GPIO.OUT)

dataPath = '.Datos_usuarios/Usuarios' #Cambia a la ruta donde hayas almacenado Data
imagePaths = os.listdir(dataPath)
#print('imagePaths=',imagePaths)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Leyendo el modelo

face_recognizer.read('modeloLBPHFace.xml')

cap = cv2.VideoCapture(-1)
#cap = cv2.VideoCapture('Video.mp4')

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

def open_locker(locker_number):
    # Activación del servo correspondiente durante 5 segundos
    servo_pin = cerradura_pins[locker_number-1]
    GPIO.output(servo_pin, GPIO.HIGH)
    time.sleep(5)
    GPIO.output(servo_pin, GPIO.LOW)

def verificar_usuario():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    carpeta = f'.Datos_usuarios/Usuarios/{usuario}'
    existe = False

    with open(".Datos_usuarios/usuarios.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Username"] == usuario and row["Contraseña"] == contraseña:
                existe = True
                numero_locker = int(row["Locker"])
                break

    if existe:
        if os.path.exists(carpeta):
            open_locker(numero_locker)
            tkinter.messagebox.showinfo('Abriendo locker', f"Locker abierto!\nNúmero de locker: {numero_locker}")
            ventana.destroy()

        else:
            ventana_abierta = tk.Toplevel(ventana)
            ventana_abierta.geometry("200x100")
            etiqueta = tk.Label(ventana_abierta, text="No se encontró la carpeta para reconocimiento biométrico")
            etiqueta.pack()
    else:
        #ventana_abierta = tk.Toplevel(ventana)
        tkinter.messagebox.showerror('Error', 'Credenciales incorrectas')
        ventana.destroy()

ventana = tk.Tk()
ventana.geometry("400x300")

etiqueta_usuario = tk.Label(ventana, text="Nombre de usuario:")
etiqueta_usuario.pack()

entry_usuario = tk.Entry(ventana)
entry_usuario.pack()

etiqueta_contraseña = tk.Label(ventana, text="Contraseña:")
etiqueta_contraseña.pack()

entry_contraseña = tk.Entry(ventana, show="*")
entry_contraseña.pack()

boton = tk.Button(ventana, text="Verificar", command=verificar_usuario)
boton.pack()

ventana.mainloop()

GPIO.cleanup()
