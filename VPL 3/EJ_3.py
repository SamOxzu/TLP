# dataset: https://www.kaggle.com/datasets/shreyanshverma27/imdb-horror-chilling-movie-dataset?resource=download
import pandas as pd
# Importar el Dataset
df = pd.read_csv("Horror Movies IMDb.csv", sep=",")

# Imprimir los primeros 5 datos
print("Primeros 5 datos del dataset: ")
print(df.head(5))
print("---------------------------------------------------------------")
# Encontrar la longitud del dataset
print(f"Longitud del dataset: {len(df)}")
print("---------------------------------------------------------------")
# Imprimir los encabezados
print(f"Encabezados: {', '.join(df.columns)}")
print("---------------------------------------------------------------")
# Obtener un sub-dataframe con películas desde 1980 hasta la actualidad
df_1980 = df[df["Movie Year"] >= 1980]
print(f"Sub-dataFrame con películas desde 1980: ")
# Dado el sub dataFrame anterior:
# Encontrar la película más corta
shortest_movie = df_1980.loc[df_1980["Runtime"].idxmin()]
print(f"- Película más corta: {shortest_movie['Movie Title']} con duración de {shortest_movie['Runtime']} minutos")

# Encontrar la película menos rentable
df_1980.loc[:, "Gross"] = df_1980["Gross"].replace({'\$': '', 'M': ''}, regex=True).astype(float) * 1e6
least_profitable_movie = df_1980.loc[df_1980["Gross"].idxmin()]
print(f"- Película menos rentable: {least_profitable_movie['Movie Title']} con ingresos de {least_profitable_movie['Gross']}")

# Encontrar el promedio de duración
average_duration = df_1980["Runtime"].mean()
print(f"- Duración promedio: {average_duration}")

# Encontrar la desviación estándar de las calificaciones
std_rating = df_1980["Rating"].std()
print(f"- Desviación estándar de las calificaciones: {std_rating}")
print("---------------------------------------------------------------")
# Encontrar el promedio de votos por género
def convert_votes(votes_str):
    parts = votes_str.split(',')
    if len(parts) == 3:
        millions, thousands, units = parts
        return int(millions) * 1_000_000 + int(thousands) * 1_000 + int(units)
    elif len(parts) == 2:
        thousands, units = parts
        return int(thousands) * 1_000 + int(units)
    else:
        return int(parts[0])

df.loc[:, "Votes"] = df["Votes"].apply(convert_votes)

df.loc[:, "Single Genres"] = df["Genre"].str.split(", ")

df_exploded = df.explode("Single Genres")
average_votes_by_single_genre = df_exploded.groupby("Single Genres")["Votes"].mean()

print("Promedio de votos por género: ")
print(average_votes_by_single_genre)
print("---------------------------------------------------------------")
# Encontrar los directores y el número de ocurrencias en el dataset, ordenados descendentemente
directors = df["Director"].value_counts()
print("Directores y número de ocurrencias:")
print(directors)
print("---------------------------------------------------------------")
# 5 péliculas mejor calíficadas cuyo género es Horror, Mystery, Sci-Fi
df_filtered = df[df["Genre"] == "Horror, Mystery, Sci-Fi"]
top_5_movies = df_filtered.nlargest(5, "Rating")
print("Mejores 5 películas de Horror, Mystery, Sci-Fi:")
print(top_5_movies[["Movie Title", "Movie Year", "Rating"]])