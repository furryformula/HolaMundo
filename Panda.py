import os
import time
import numpy as np
import pandas as pd

# Crear un array de datos utilizando NumPy
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Crear un DataFrame utilizando Pandas
df = pd.DataFrame(data, columns=['A', 'B', 'C'])

contador = 0

while True:
    # Limpiar la consola
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Incrementar el contador
    contador += 1
    
    # Imprimir el contador
    print(f"Actualización #{contador}")
    print("---------------------------------")
    
    # Imprimir "Hola Mundo"
    print("Hola Mundo")

    # Imprimir el DataFrame
    print("\nDataFrame:")
    print(df)

    # Calcular la media de cada columna
    media = df.mean()
    print("\nMedia de cada columna:")
    print(media)

    # Calcular la suma de cada fila
    suma_filas = df.sum(axis=1)
    print("\nSuma de cada fila:")
    print(suma_filas)

    # Pausar durante 5 segundos
    time.sleep(5)
