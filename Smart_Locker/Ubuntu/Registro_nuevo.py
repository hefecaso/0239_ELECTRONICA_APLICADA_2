import csv
import os
import tkinter as tk
from tkinter import filedialog
import cv2

import imutils
import time


def register_user():
    user = username_entry.get()
    locker = locker_entry.get()
    dpi = dpi_entry.get()
    password = password_entry.get()

    # Guardar datos en csv
    with open(".Datos_usuarios/usuarios.csv", "a") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([user, locker, dpi, password])

    # Crear carpeta para almacenar las fotos biométricas
    os.makedirs(f".Datos_usuarios/Usuarios/{user}")

    # Capturar fotos biométricas con OpenCV
    #########################################
    personName = user
    dataPath = '.Datos_usuarios/Usuarios'#Cambia a la ruta donde hayas almacenado Data
    personPath = dataPath + '/' + personName

    if not os.path.exists(personPath):
        print('Carpeta creada: ',personPath)
        os.makedirs(personPath)

    cap = cv2.VideoCapture(-1)
    #cap = cv2.VideoCapture('Video.mp4')

    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
    count = 0

    while True:
        ret, frame = cap.read()
        if ret == False: break
        frame =  imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()
        faces = faceClassif.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
            rostro = auxFrame[y:y+h,x:x+w]
            rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(personPath + '/rotro_{}.jpg'.format(count),rostro)
            count = count + 1
        cv2.imshow('frame',frame)

        k =  cv2.waitKey(1)
        if k == 27 or count >= 50:
            break

    cap.release()
    cv2.destroyAllWindows()
    exec(open("entrenandoRF.py").read())
    # Cerrar ventana de registro
    root.destroy()

# Interfaz gráfica en tkinter
root = tk.Tk()
root.title("Registro de usuarios")

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
