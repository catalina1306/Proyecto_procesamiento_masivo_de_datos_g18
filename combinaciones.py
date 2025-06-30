import pandas as pd

# Leer el archivo como texto plano y procesarlo
df = pd.read_csv("fraude_por_comb.txt", header=None, names=["raw"])

# Elimina los paréntesis y separa por coma
df = df["raw"].str.strip("()").str.split(",", n=6, expand=True)

# Renombra columnas
df.columns = ["pais", "categoria", "canal", "tipo_tarjeta", "total_fraudes", "total_tx", "tasa_fraude"]

# Limpia posibles espacios
for col in df.columns:
    df[col] = df[col].str.strip() if df[col].dtype == "object" else df[col]

# Convierte a numérico las columnas correspondientes
df["total_fraudes"] = pd.to_numeric(df["total_fraudes"])
df["total_tx"] = pd.to_numeric(df["total_tx"])
df["tasa_fraude"] = pd.to_numeric(df["tasa_fraude"])

# Mostrar los primeros resultados
print(df.head())