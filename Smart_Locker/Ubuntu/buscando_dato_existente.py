import getpass
from numpy import *
import matplotlib.pyplot as plt
import pandas as pd

Username = input("Escriba su nombre de usuario: ")
Contraseña = getpass.getpass("Ingrese su contraseña: ")
Dpi = input("Ingrese su número de DPI: ")
df = pd.read_csv(f'.Datos_usuarios/usuarios.csv', columns = ['Username', 'Contraseña'], header=0)

busqueda = df.isin([Username, Contraseña]).any()

print(busqueda)