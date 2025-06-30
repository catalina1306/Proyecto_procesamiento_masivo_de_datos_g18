import pandas as pd

# Cargar el dataset original (puede ser un CSV u otro formato)
# Reemplaza 'ruta/dataset.csv' con la ruta a tu archivo
df = pd.read_csv('synthetic_fraud_data.csv')

# Verificamos que haya al menos 20.000 filas
if len(df) < 15000:
    raise ValueError("El dataset tiene menos de 20.000 filas")

# Seleccionar 20.000 filas al azar
df_sample = df.sample(n=15000, random_state=42)
#df_sample = df

df_sample = df_sample.drop(columns=['velocity_last_hour'])
# Guardar el nuevo dataset en un archivo (puede ser CSV, Parquet, etc.)
df_sample.to_csv('datos_fraude_no_vel.csv', index=False)
