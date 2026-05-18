# 📊 Proyecto Excel Automation Tool

Herramienta CLI desarrollada en Python para automatizar la limpieza, procesamiento y generación de reportes en archivos Excel.

---

## 🚀 Funcionalidades

* Lectura de archivos Excel mal estructurados
* Limpieza de datos (columnas, tipos, valores nulos)
* Conversión de datos a formatos correctos
* Cálculo de precios con descuento
* Generación de estadísticas básicas
* Identificación de productos más caros
* Exportación automática a Excel limpio
* 📊 Generación de gráficos (Top productos)
* Creación automática de archivos sin sobrescribir

---

## ⚙️ Requisitos

* Python 3.10+
* Librerías:

```bash
pip install -r requirements.txt
```

---

## ▶️ Uso

```bash
python main.py --config config.json
```

---

## 📁 Configuración (config.json)

Ejemplo:

```json
{
  "input_file": "Example.xlsx",
  "output_file": "resultado_limpio.xlsx",
  "header_row": 1,
  "columns": {
    "price": "PRECIO LISTA",
    "discount": "DESCUENTO VARIABLE ENERO 2023"
  },
  "chart": {
    "enabled": true,
    "type": "bar",
    "x_column": "DESCRIPCION",
    "y_column": "PRECIO LISTA",
    "top_n": 5
  }
}
```

---

## 📊 Output

El programa genera:

* Hoja **Data** → datos completos procesados
* Hoja **Top** → top productos
* 📈 Gráfico automático dentro del Excel
* Archivos con nombre incremental (sin sobrescribir)

---

## 🧠 Tecnologías utilizadas

* Python
* pandas
* xlsxwriter

---

## 💼 Caso de uso

Automatización de reportes para análisis de precios en entornos comerciales (retail, inventario, ventas).

---

## 📌 Autor

Proyecto desarrollado como parte de portafolio profesional orientado a backend y automatización de datos.
