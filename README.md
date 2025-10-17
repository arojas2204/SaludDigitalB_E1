# 🩺 Proyecto SaludDigitalB_E1

## 📘 Descripción General

Este proyecto corresponde a la **Práctica Calificada del curso de Sistemas Digitales**.
El objetivo es **automatizar el proceso de gestión y análisis de datos de pacientes** para la empresa ficticia *Salud Digital*, aplicando los conceptos vistos en clase: Git, Python, MongoDB y visualización de datos.

El flujo de trabajo se desarrolló siguiendo las fases del **Caso Práctico Integrador (Big Data, Git, GitHub, VS Code, Python, MongoDB y Jenkins)** adaptado al contexto de *Salud Digital*.

---

## ⚙️ Fases del Proyecto

### 🧩 Fase 1 — Creación del entorno y estructura de carpetas

* Se creó la carpeta principal `SaludDigitalB_E1` y las subcarpetas:

  ```
  data/
  database/
  reports/
  scripts/
  ci/
  git/
  ```
* Se configuró el entorno virtual `myenv`.
* Se instalaron las librerías necesarias:

  ```bash
  pip install pandas numpy matplotlib pymongo seaborn
  ```

---

### 🧩 Fase 2 — Creación del archivo base (`base.csv`)

* Se definió la estructura del dataset:

  ```
  id_paciente,nombre,edad,sexo,distrito,servicio,fecha_atencion,monto
  ```
* El archivo se guardó en la carpeta `data/`.

---

### 🧩 Fase 3 — Generación del dataset (`pacientes.csv`)

* Se generaron **3000 registros simulados** con datos aleatorios y casos con valores nulos o duplicados.
* Script utilizado:

  ```
  scripts/3_Generar_Data_Pacientes.py
  ```
* Resultado: `data/pacientes.csv`

---

### 🧩 Fase 4 — Proceso ETL (Limpieza de datos)

* Se aplicaron operaciones de:

  * Eliminación de duplicados.
  * Relleno de valores nulos.
  * Normalización de fechas y tipos de datos.
* Script utilizado:

  ```
  scripts/4_Proceso_ETL.py
  ```
* Resultado: `database/pacientes_clean.csv`

---

### 🧩 Fase 5 — Carga en MongoDB

* Se creó la base de datos **SaludDigital_2025** en MongoDB local.
* Se insertaron los registros limpios en la colección **pacientes**.
* Script utilizado:

  ```
  scripts/5_Loading_MongoDB.py
  ```
* Comando de verificación en `mongosh`:

  ```bash
  use SaludDigital_2025
  db.pacientes.countDocuments()
  ```

---

### 🧩 Fase 6 — Visualización y Reportes

* Se generaron gráficos automáticos con `matplotlib`:

  * 📊 Pacientes por servicio
  * 🟣 Distribución por sexo
  * 🧓 Distribución de edades
  * 💰 Promedio de montos por distrito
* Script utilizado:

  ```
  scripts/6_Reportes.py
  ```
* Resultados guardados en `reports/`:

  ```
  pacientes_por_servicio.png
  distribucion_por_sexo.png
  distribucion_de_edades.png
  promedio_montos_por_distrito.csv
  ```

---

## 🗂️ Estructura del Proyecto

```
SaludDigitalB_E1/
│
├── data/
│   ├── base.csv
│   └── pacientes.csv
│
├── database/
│   └── pacientes_clean.csv
│
├── reports/
│   ├── pacientes_por_servicio.png
│   ├── distribucion_por_sexo.png
│   ├── distribucion_de_edades.png
│   └── promedio_montos_por_distrito.csv
│
├── scripts/
│   ├── 3_Generar_Data_Pacientes.py
│   ├── 4_Proceso_ETL.py
│   ├── 5_Loading_MongoDB.py
│   └── 6_Reportes.py
│
├── myenv/
│
└── README.md
```

---

## 🧠 Tecnologías Utilizadas

* **Python 3.10+**
* **Pandas**, **NumPy**, **Matplotlib**, **Seaborn**
* **MongoDB** (local)
* **Git & GitHub**
* **Visual Studio Code**
* *(Opcional)* Jenkins para automatización CI/CD

---

## 🚀 Cómo ejecutar el proyecto

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/arojas2204/SaludDigitalB_E1.git
   cd SaludDigitalB_E1
   ```

2. **Activar el entorno virtual:**

   ```bash
   .\myenv\Scripts\Activate.ps1   # en PowerShell
   # o
   source myenv/Scripts/activate  # en Git Bash
   ```

3. **Instalar dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar las fases:**

   ```bash
   python scripts/3_Generar_Data_Pacientes.py
   python scripts/4_Proceso_ETL.py
   python scripts/5_Loading_MongoDB.py
   python scripts/6_Reportes.py
   ```

5. **Ver resultados:**

   * Datos limpios en `database/`
   * Gráficos y reportes en `reports/`
   * Base de datos `SaludDigital_2025` creada en MongoDB

---

## 👩‍💻 Autora
```bash
Proyecto desarrollado aplicando conceptos de Big Data, Vs Code, Python,
MongoDB y Jenkins.
Alejandra Nicole Rojas Arévalo
Fecha: 17.10.2025
