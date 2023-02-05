import pandas as pd

#Username = input("Escriba su nombre de usuario: ")
#df = pd.read_csv(f'.Datos_usuarios/usuarios.csv', header=0)
# print(datos)
# print("")
#Locker = df['Locker']
#print(Locker)
#print(datos.ix[0:1])




import getpass
from numpy import *
import matplotlib.pyplot as plt
import pandas as pd

Username = input("Escriba su nombre de usuario: ")
Contraseña = getpass.getpass("Ingrese su contraseña: ")
df = pd.read_csv(f'.Datos_usuarios/usuarios.csv', header=0)

busqueda = df.isin([Username, Contraseña]).any()

print(busqueda)


locker_info = str(locker.get())