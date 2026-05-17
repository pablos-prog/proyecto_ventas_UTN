import pandas as pd

print("Cargando dataset...")

df = pd.read_csv("datos/ventas.csv")

df["total"] = df["cantidad"] * df["precio"]

print("\nDATA COMPLETA:")
print(df)

ventas_totales = df["total"].sum()
print("\nVentas totales:", ventas_totales)

mas_vendido = df.groupby("producto")["cantidad"].sum().idxmax()
print("Producto más vendido:", mas_vendido)

print("\nVentas por producto:")
print(df.groupby("producto")["total"].sum())
