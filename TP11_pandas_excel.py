import pandas as pd

# --- 1) Lectura de archivos Excel ---

# Ejercicio 1
df_2000 = pd.read_excel("movies.xls", sheet_name="2000s")
print("Cantidad de filas:", len(df_2000))

# Ejercicio 2
df_2010 = pd.read_excel("movies.xls", sheet_name="2010s", usecols=["Title", "Year", "IMDB Score"])
print(df_2010.head())

# Ejercicio 3
df_1900 = pd.read_excel("movies.xls", sheet_name="1900s")
df_movies = pd.concat([df_1900, df_2000, df_2010])
print(df_movies.head())


# --- 2) head() y tail() ---

# Ejercicio 1
print(df_2000.head(5))

# Ejercicio 2
print(df_2010.tail(3))

# Ejercicio 3
primeras_12 = df_1900.head(12)
print(primeras_12)


# --- 3) value_counts() ---

# Ejercicio 1
print(df_2000["Country"].value_counts())

# Ejercicio 2
print(df_2010["Director"].value_counts().head(5))

# Ejercicio 3
print(df_movies["Year"].value_counts().sort_index())


# --- 4) sort_values() ---

# Ejercicio 1
print(df_movies.sort_values(by="IMDB Score", ascending=False).head(5))

# Ejercicio 2
print(df_movies.sort_values(by="User Votes", ascending=True).head())

# Ejercicio 3
print(df_movies.sort_values(by=["Country", "Year"]).head())


# --- 5) groupby() ---

# Ejercicio 1
print(df_movies.groupby("Country")["IMDB Score"].mean())

# Ejercicio 2
col = "Gross Earnings" if "Gross Earnings" in df_movies.columns else "Country"
print(df_movies.groupby(col)["IMDB Score"].sum())

# Ejercicio 3
df_movies["Decade"] = (df_movies["Year"] // 10) * 10
print(df_movies.groupby("Decade")["Title"].count())


# --- 6) Limpieza de datos ---

# Ejercicio 1
print(df_movies.info())

# Ejercicio 2
df_limpio = df_movies.dropna(subset=["IMDB Score"])

# Ejercicio 3
df_movies["Country"] = df_movies["Country"].fillna("Unknown")


# --- 7) Exportar a Excel ---

df_movies.to_excel("movies_completo.xlsx", index=False)

promedio_pais = df_movies.groupby("Country")["IMDB Score"].mean()
promedio_pais.to_excel("analisis_por_pais.xlsx")
