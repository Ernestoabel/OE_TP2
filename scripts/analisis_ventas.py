import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------
# 0. Configuración inicial
# -----------------------------
os.makedirs('resultados', exist_ok=True)

# Cargar datos
df = pd.read_csv('datos/sales_sample_2024.csv')

print("Primeras filas del dataset:")
print(df.head())

# -----------------------------
# 1. Validación de columnas
# -----------------------------
required_cols = ['sales_amount', 'sales_date']
for col in required_cols:
    if col not in df.columns:
        raise ValueError(f"La columna '{col}' no existe en el dataset")

# -----------------------------
# 2. Ventas totales
# -----------------------------
ventas_totales = df['sales_amount'].sum()
print("\nVentas totales:", ventas_totales)

# -----------------------------
# 3. Día con mayor venta
# -----------------------------
fila_max = df.loc[df['sales_amount'].idxmax()]
dia_max = fila_max['sales_date']
monto_max = fila_max['sales_amount']
print(f"Día con mayor venta: {dia_max} (${monto_max})")

# -----------------------------
# 4. Ventas por mes
# -----------------------------
df['sales_date'] = pd.to_datetime(df['sales_date'])
df['mes'] = df['sales_date'].dt.strftime('%Y-%m')

ventas_por_mes = df.groupby('mes')['sales_amount'].sum()

print("\nVentas por mes:")
print(ventas_por_mes)

ventas_por_mes.to_csv('resultados/ventas_por_mes.csv')

# -----------------------------
# 5. Gráfico de ventas por mes
# -----------------------------
plt.figure(figsize=(10,5))
ventas_por_mes.plot(kind='bar', color='steelblue')
plt.title("Ventas por mes - 2024")
plt.xlabel("Mes")
plt.ylabel("Monto de ventas")
plt.tight_layout()
plt.savefig('resultados/ventas_por_mes.png')
plt.close()

# -----------------------------
# 6. Resumen general
# -----------------------------
resumen = pd.DataFrame({
    "Ventas Totales": [ventas_totales],
    "Día Mayor Venta": [dia_max],
    "Monto Mayor Venta": [monto_max]
})
resumen.to_csv('resultados/resumen.csv', index=False)

print("\n✔ Resultados guardados en /resultados")