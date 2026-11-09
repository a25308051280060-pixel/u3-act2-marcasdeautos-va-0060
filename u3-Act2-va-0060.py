import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# crearemos nuestra tabla y la guardaremos con pandas
# tenemos 5 listas de marcas de autos con 4 elementos por lista
toy = ['Toyota', 'Japón', True, 1937]
tsl = ['Tesla', 'EEUU', True, 2003]
bmw = ['BMW', 'Alemania', True, 1916]
ford = ['Ford', 'EEUU', True, 1903]  # Se usó 'ford' porque 'for' es palabra reservada en Python
fer = ['Ferrari', 'Italia', True, 1939]

# creamos una lista de listas (conformando la tabla)
lista_autos = [toy, tsl, bmw, ford, fer]
print(lista_autos)

# Utilizar pandas para organizar la tabla (dataframe o marco de datos)
# a cada columna le ponemos nombre
df_autos = pd.DataFrame(
    lista_autos,
    columns=[
        'Marca',
        'País_Origen',
        'Fabrica_Eléctricos',
        'Año_Fundación',
    ],
)
print(df_autos)

# creamos el archivo CSV y lo guardamos
df_autos.to_csv('autos.csv', index=False)

# crear grafica de lineas
# donde X es Marca en el eje horizontal
# donde Y es Año_Fundación en el eje vertical
plt.plot(df_autos['Marca'], df_autos['Año_Fundación'])
plt.title('Grafica autos 0060')
plt.xlabel('Marca de los autos')
plt.ylabel('Año de fundación')
plt.title('autos 0060')
plt.xlabel('las marcas')
plt.ylabel('año de fundación')
plt.show()

# creamos una grafica de puntos
plt.scatter(df_autos['Marca'], df_autos['Año_Fundación'])
plt.show()

# grafica de barras
plt.bar(df_autos['Marca'], df_autos['Año_Fundación'])
plt.title('autos 0060')
plt.xlabel('las marcas')
plt.ylabel('año de fundación')
plt.show()

# grafica de barras
plt.bar(df_autos['Marca'], df_autos['Año_Fundación'])
plt.title('autos 0060')
plt.xlabel('las marcas')
plt.ylabel('año de fundación')
plt.show()

# ordenar la grafica de barras de manera descendente
# de la mas grande a la pequeña (por año de fundación)
df_autos_ordenar = df_autos.sort_values('Año_Fundación', ascending=False)
plt.bar(df_autos_ordenar['Marca'], df_autos_ordenar['Año_Fundación'])
plt.show()

# coloreando la grafica
df_autos_ordenar = df_autos.sort_values('Año_Fundación', ascending=False)
plt.bar(
    df_autos_ordenar['Marca'],
    df_autos_ordenar['Año_Fundación'],
    color=['b', 'g', 'c', 'm', 'y'],
)
plt.show()

# grafica de pastel
plt.pie(df_autos['Año_Fundación'], labels=df_autos['Marca'])
plt.show()