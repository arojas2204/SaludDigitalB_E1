# scripts/6_Reportes.py
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Leer el archivo limpio
df = pd.read_csv(Path.cwd() / "database" / "pacientes_clean.csv")

# Crear carpeta de reportes si no existe
out = Path.cwd() / "reports"
out.mkdir(parents=True, exist_ok=True)

# 1️⃣ Gráfico de barras: pacientes por servicio
servicios = df['servicio'].value_counts()
plt.figure(figsize=(8,5))
servicios.plot(kind='bar', color='skyblue')
plt.title('Pacientes atendidos por servicio')
plt.ylabel('Cantidad')
plt.tight_layout()
plt.savefig(out / "pacientes_por_servicio.png")
plt.close()

# 2️⃣ Gráfico circular: distribución por sexo
sexos = df['sexo'].value_counts()
plt.figure(figsize=(6,6))
sexos.plot.pie(autopct='%1.1f%%', startangle=90)
plt.title('Distribución de pacientes por sexo')
plt.ylabel('')
plt.tight_layout()
plt.savefig(out / "distribucion_por_sexo.png")
plt.close()

# 3️⃣ Histograma: distribución de edades
plt.figure(figsize=(8,5))
df['edad'].hist(bins=10, color='lightgreen')
plt.title('Distribución de edades de pacientes')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.savefig(out / "distribucion_de_edades.png")
plt.close()

# 4️⃣ Promedio de montos por distrito (CSV)
promedios = df.groupby('distrito')['monto'].mean().reset_index().sort_values(by='monto', ascending=False)
promedios.to_csv(out / "promedio_montos_por_distrito.csv", index=False)

print("✅ Reportes generados correctamente en:", out)
