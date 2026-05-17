# PROY-2: Análisis de ventas - UTN TUP

import pandas as pd

print("Iniciando análisis de ventas...")

# Ejemplo de dataset simple 
data = {
    "producto": ["A", "B", "A", "C"],
    "cantidad": [2, 1, 3, 5],
    "precio": [100, 200, 100, 300]
}

df = pd.DataFrame(data)

# Ventas totales
df["total"] = df["cantidad"] * df["precio"]

print("\nDataFrame:")
print(df)

print("\nVentas totales:", df["total"].sum())
print("\nProducto más vendido:", df.groupby("producto")["cantidad"].sum().idxmax())
