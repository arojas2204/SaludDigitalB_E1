# scripts/3_Generar_Data_Pacientes.py
from pathlib import Path
import csv, random
from datetime import datetime, timedelta

out = Path.cwd() / "data" / "pacientes.csv"
out.parent.mkdir(parents=True, exist_ok=True)

n = 3000
servicios = ["Odontología","Pediatría","Cardiología","Medicina General","Ginecología"]
distritos = ["Miraflores","Surco","San Isidro","La Molina","Cajamarca","Callao"]
sexos = ["F","M"]

def rand_date(start_year=2018, end_year=2025):
    inicio = datetime(start_year,1,1)
    fin = datetime(end_year,12,31)
    delta = fin - inicio
    d = inicio + timedelta(days=random.randint(0, delta.days))
    return d.strftime("%Y-%m-%d")

with open(out, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["id_paciente","nombre","edad","sexo","distrito","servicio","fecha_atencion","monto"])
    for i in range(1, n+1):
        pid = f"P{str(i).zfill(4)}"
        nombre = random.choice(["Ana Torres","Luis Pérez","María Gómez","Carlos Ruiz","Sofía Díaz"]) if random.random()>0.02 else ""
        edad = random.randint(0,90) if random.random()>0.01 else ""
        sexo = random.choice(sexos) if random.random()>0.03 else ""
        distrito = random.choice(distritos)
        servicio = random.choice(servicios)
        fecha = rand_date()
        monto = round(random.uniform(50,500),2) if random.random()>0.02 else ""
        if random.random() < 0.01:
            pid = "P0001"  # duplicado ocasional
        w.writerow([pid,nombre,edad,sexo,distrito,servicio,fecha,monto])

print("pacientes.csv generado en:", out)
