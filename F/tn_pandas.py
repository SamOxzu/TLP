# dataset: https://www.kaggle.com/datasets/isaienkov/atp-ranking?resource=download
import pandas as pd
import numpy as np

# Leer el archivo CSV
print("\n--- Leer el archivo CSV ---")
df = pd.read_csv("atp_ranking.csv", sep=",")

# Métodos y atributos
print("\n--- Métodos y atributos ---")
print("Forma del DataFrame:")
print(df.shape)  # Imprime la forma del DataFrame
print("Tipos de datos de cada columna:")
print(df.dtypes)  # Imprime los tipos de datos de cada columna
print("Nombres de las columnas:")
print(df.columns)  # Imprime los nombres de las columnas
print("Valores del DataFrame:")
print(df.values)  # Imprime los valores del DataFrame

# Mostrar las primeras y últimas filas del DataFrame
print("\n--- Mostrar las primeras y últimas filas del DataFrame ---")
print("Primeras 5 filas:")
print(df.head(n=5))  # Primeras 5 filas
print("Últimas 5 filas:")
print(df.tail(n=5))  # Últimas 5 filas
print("Últimas 5 filas de las primeras 10 filas:")
print(df.head(n=10).tail(n=5))  # Últimas 5 filas de las primeras 10 filas

# Acceso a columnas específicas
print("\n--- Acceso a columnas específicas ---")
print("Primeras 5 filas de la columna 'player':")
print(df['player'].head(n=5))  # Primeras 5 filas de la columna 'player'
print("Primeras 5 filas de las columnas 'rank', 'player', 'total_points':")
print(df[["rank", "player", "total_points"]].head(n=5))  # Primeras 5 filas de columnas específicas

# Renombrar columnas
print("\n--- Renombrar columnas ---")
print("DataFrame con columnas renombradas:")
print(df.rename(columns={"rank": "posicion", "player": "jugador", "total_points": "puntos_totales"}).head(n=5))

# Selección de filas y columnas
print("\n--- Selección de filas y columnas ---")
print("Filas de la 10 a la 19:")
print(df[10:20])  # Filas de la 10 a la 19
print("Filas de la 10 a la 19 y columnas 1 y 2:")
print(df.iloc[10:20, [1, 2]])  # Filas de la 10 a la 19 y columnas 1 y 2
print("Valor de la fila 1 y columna 'player':")
print(df.loc[1, "player"])  # Valor de la fila 1 y columna 'player'

# Eliminar filas y columnas
print("\n--- Eliminar filas y columnas ---")
print("DataFrame sin la fila 5 - Primeras 7 filas:")
print(df.drop(5).head(n=7))  # Elimina la fila 5 y muestra las primeras 7 filas
df_copy = df.copy()  # Crea una copia del DataFrame
del df_copy["other_points"]  # Elimina la columna 'other_points' de la copia
print("Copia del DataFrame sin la columna 'other_points' - Primeras 5 filas:")
print(df_copy.head(n=5))  # Muestra las primeras 5 filas de la copia

# Cambiar el índice del DataFrame
print("\n--- Cambiar el índice del DataFrame ---")
df = df.set_index("rank")  # Establece la columna 'rank' como índice
print("DataFrame con 'rank' como índice - Primeras 5 filas:")
print(df.head(n=5))  # Muestra las primeras 5 filas
df = df.reset_index()  # Resetea el índice
print("DataFrame con índice reseteado - Primeras 5 filas:")
print(df.head(n=5))  # Muestra las primeras 5 filas

# Operaciones con columnas
print("\n--- Operaciones con columnas ---")
print("Tipos de datos de cada columna:")
print(df.dtypes)  # Imprime los tipos de datos de cada columna
print("Primeras 5 filas de la columna 'total_points':")
print(df['total_points'].head(n=5))  # Primeras 5 filas de la columna 'total_points'
df['total_points'] = df['total_points'] - 200  # Resta 200 a cada valor de 'total_points'
print("Primeras 5 filas de la columna 'total_points' después de la resta:")
print(df['total_points'].head(n=5))  # Primeras 5 filas de la columna 'total_points' después de la resta

# Modificar valores en la copia del DataFrame
print("\n--- Modificar valores en la copia del DataFrame ---")
df_copy = df.copy()  # Crea una copia del DataFrame
df_copy.at[0, 'player'] = 'Pedrito Picapiedra'  # Cambia el valor de la primera fila en la columna 'player'
print("Copia del DataFrame - Primeras 5 filas de la columna 'player':")
print(df_copy['player'].head(n=5))  # Primeras 5 filas de la columna 'player' en la copia
print("DataFrame original - Primeras 5 filas de la columna 'player':")
print(df['player'].head(n=5))  # Primeras 5 filas de la columna 'player' en el DataFrame original

# Filtrado de datos
print("\n--- Filtrado de datos ---")
print("Filas donde la columna 'country' es 'ESP':")
print(df[df['country'] == 'ESP'].head(n=10))  # Filas donde la columna 'country' es 'ESP'
print("Filas donde 'country' es 'RUS' o 'ESP':")
print(df[(df['country'] == 'RUS') | (df['country'] == 'ESP')].head(n=10))  # Filas donde 'country' es 'RUS' o 'ESP'
print("Filas donde 'country' es 'RUS' y 'total_points' > 4000:")
print(df[(df['country'] == 'RUS') & (df['total_points'] > 4000)].head(n=10))  # Filas donde 'country' es 'RUS' y 'total_points' > 4000
print("Cuenta de filas donde 'country' es 'RUS' y 'total_points' > 4000:")
print(df[(df['country'] == 'RUS') & (df['total_points'] > 4000)].count())  # Cuenta las filas que cumplen la condición
print("Cuenta de filas en la columna 'rank' donde 'country' es 'RUS' y 'total_points' > 4000:")
print(df[(df['country'] == 'RUS') & (df['total_points'] > 4000)]['rank'].count())  # Cuenta las filas que cumplen la condición en la columna 'rank'

# Eliminar filas con valores NaN
print("\n--- Eliminar filas con valores NaN ---")
print("DataFrame sin filas con valores NaN - Primeras 10 filas:")
print(df.dropna().head(n=10))  # Elimina filas con valores NaN y muestra las primeras 10 filas

# Filtrado y operaciones con columnas
print("\n--- Filtrado y operaciones con columnas ---")
c25 = df[df['tournaments'] == 25]  # Filtra filas donde 'tournaments' es 25
c25['tournaments'] = c25['tournaments'].astype(int)  # Convierte la columna 'tournaments' a enteros
print("Tipos de datos en el DataFrame filtrado:")
print(c25.dtypes)  # Imprime los tipos de datos de cada columna en el DataFrame filtrado
print("Suma de la columna 'total_points' en el DataFrame filtrado:")
print(np.sum(c25['total_points']))  # Suma de la columna 'total_points' en el DataFrame filtrado
print("Media de la columna 'total_points' en el DataFrame filtrado:")
print(np.mean(c25['total_points']))  # Media de la columna 'total_points' en el DataFrame filtrado