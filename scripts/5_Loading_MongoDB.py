# scripts/5_Loading_MongoDB.py
import pandas as pd
from pymongo import MongoClient
from pathlib import Path

# Archivo limpio
file_clean = Path.cwd() / "database" / "pacientes_clean.csv"
df = pd.read_csv(file_clean)

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["SaludDigital_2025"]   # nombre de la base
collection = db["pacientes"]       # nombre de la colección

# Limpiar colección anterior (opcional)
collection.delete_many({})

# Insertar los registros
data = df.to_dict(orient="records")
collection.insert_many(data)

print("✅ Datos insertados correctamente.")
print("Total de documentos:", collection.count_documents({}))
