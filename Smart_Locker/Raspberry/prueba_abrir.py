import tkinter as tk
import csv
import os
import cv2

dataPath = '.Datos_usuarios/Usuarios' #Cambia a la ruta donde hayas almacenado Data
imagePaths = os.listdir(dataPath)
print('imagePaths=',imagePaths)

face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Leyendo el modelo

face_recognizer.read('modeloLBPHFace.xml')

cap = cv2.VideoCapture(-1)
#cap = cv2.VideoCapture('Video.mp4')

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

while True:
    ret,frame = cap.read()
    if ret == False: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    faces = faceClassif.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        rostro = auxFrame[y:y+h,x:x+w]
        rostro = cv2.resize(rostro,(150,150),interpolation= cv2.INTER_CUBIC)
        result = face_recognizer.predict(rostro)

        cv2.putText(frame,'{}'.format(result),(x,y-5),1,1.3,(255,255,0),1,cv2.LINE_AA)

        # LBPHFace
        if result[1] < 70:
            cv2.putText(frame,'{}'.format(imagePaths[result[0]]),(x,y-25),2,1.1,(0,255,0),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        else:
            cv2.putText(frame,'Desconocido',(x,y-20),2,0.8,(0,0,255),1,cv2.LINE_AA)
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow('frame',frame)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

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
                numero_locker = row["Locker"]
                break

    if existe:
        if os.path.exists(carpeta):
            ventana_abierta = tk.Toplevel(ventana)
            ventana_abierta.geometry("200x100")
            etiqueta = tk.Label(ventana_abierta, text="Locker abierto\nNúmero de locker: " + numero_locker)
            etiqueta.pack()
        else:
            ventana_abierta = tk.Toplevel(ventana)
            ventana_abierta.geometry("200x100")
            etiqueta = tk.Label(ventana_abierta, text="No se encontró la carpeta para reconocimiento biométrico")
            etiqueta.pack()
    else:
        ventana_abierta = tk.Toplevel(ventana)
        ventana_abierta.geometry("200x100")
        etiqueta = tk.Label(ventana_abierta, text="Credenciales incorrectas")
        etiqueta.pack()

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
