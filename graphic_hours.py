import matplotlib.pyplot as plt
results = [(0,41519), (1,165999), (2,166025), (3,165621), (4,166418), (5,41829),
           (6,41622), (7,41318), (8,41523), (9,41522), (10,41410), (11,41857),
           (12,41716), (13,41829), (14,41665), (15,41705), (16,41407), (17,41423),
           (18,41400), (19,41786), (20,41188), (21,41049), (22,41431), (23,41457)]

# Separar las horas y los valores
horas = [x[0] for x in results]
fraudes = [x[1] for x in results]

# Crear el gráfico
plt.figure(figsize=(12, 6))
plt.plot(horas, fraudes, marker='o', linestyle='-', color='crimson', linewidth=2, markersize=6)

plt.title('Cantidad de fraudes por hora del día', fontsize=16)
plt.xlabel('Hora del día (0-23)', fontsize=12)
plt.ylabel('Número de fraudes', fontsize=12)
plt.xticks(horas)
plt.ylim(bottom=0)  
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

plt.show()
