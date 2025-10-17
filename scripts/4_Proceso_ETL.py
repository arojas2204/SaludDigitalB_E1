# scripts/4_Proceso_ETL.py
import pandas as pd
from pathlib import Path

input_file = Path.cwd() / "data" / "pacientes.csv"
output_dir = Path.cwd() / "database"
output_dir.mkdir(parents=True, exist_ok=True)
output_file = output_dir / "pacientes_clean.csv"

df = pd.read_csv(input_file)

print("Registros iniciales:", len(df))
print("Nulos por columna:\n", df.isnull().sum())

# Reemplazos y normalizaciones
df['nombre'] = df['nombre'].fillna('SIN_NOMBRE').replace('', 'SIN_NOMBRE')
df['sexo'] = df['sexo'].fillna('ND').replace('', 'ND')
df['monto'] = pd.to_numeric(df['monto'], errors='coerce').fillna(0)
df['edad'] = pd.to_numeric(df['edad'], errors='coerce').fillna(0).astype(int)
df['fecha_atencion'] = pd.to_datetime(df['fecha_atencion'], errors='coerce').dt.strftime('%Y-%m-%d')
df['fecha_atencion'] = df['fecha_atencion'].fillna('1900-01-01')

# Eliminar duplicados
df = df.drop_duplicates()

# Guardar limpio
df.to_csv(output_file, index=False, encoding='utf-8')
print("Guardado:", output_file)
print("Registros finales:", len(df))
