import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Datos
data = [
    ("Dentro del país", "No es fraude", 4947262),
    ("Fuera del país", "Es fraude", 1368376),
    ("Dentro del país", "Es fraude", 126343),
    ("Fuera del país", "No es fraude", 1041785)
]

# Crear DataFrame
df = pd.DataFrame(data, columns=["Lugar", "Fraude", "Cantidad"])

heatmap_data = df.pivot(index="Lugar", columns="Fraude", values="Cantidad")

plt.figure(figsize=(6, 4))
sns.heatmap(heatmap_data, annot=True, fmt="d", cmap="BuPu")

# Etiquetas
plt.title("Transacciones según Fraude y Ubicación")
plt.xlabel("¿La transacción fue un fraude?")
plt.ylabel("¿Dónde se realizó la transacción?")
plt.yticks(rotation=0)
plt.show()
