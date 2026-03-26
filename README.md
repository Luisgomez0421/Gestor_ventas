# 📦 Sistema de Inventario en Python (CRUD + Persistencia CSV)

## 📖 Descripción
Este proyecto es una aplicación de consola desarrollada en Python que permite gestionar un inventario de productos mediante operaciones CRUD (Crear, Leer, Actualizar y Eliminar), cálculo de estadísticas y persistencia de datos utilizando archivos CSV.

El sistema está diseñado con una arquitectura modular, utilizando múltiples archivos para separar la lógica del negocio, la gestión de archivos y la interfaz de usuario.

---

## 🎯 Objetivo
- Gestionar productos con nombre, precio y cantidad.
- Mantener la información entre sesiones mediante archivos CSV.
- Aplicar estructuras de datos como listas, diccionarios y tuplas.
- Implementar buenas prácticas de programación como modularización, validaciones y manejo de errores.

---

## 🧱 Estructura del Proyecto

📁 proyecto_inventario/
│
├── app.py           # Archivo principal (menú e interacción con el usuario)
├── servicios.py     # Lógica del inventario (CRUD + estadísticas)
├── archivos.py      # Manejo de archivos CSV (guardar y cargar)
└── README.md        # Documentación del proyecto

---

## ⚙️ Funcionalidades

### 📌 CRUD de Inventario
- Agregar productos
- Mostrar inventario
- Buscar productos por nombre
- Actualizar precio y/o cantidad
- Eliminar productos

### 📊 Estadísticas
- Total de unidades
- Valor total del inventario
- Producto más caro
- Producto con mayor stock

### 💾 Persistencia (CSV)
- Guardar inventario en archivo CSV
- Cargar inventario desde CSV
- Validación de formato y datos
- Manejo de errores (archivos inexistentes, datos inválidos, etc.)
- Opción de sobrescribir o fusionar inventario

---

## 🧪 Validaciones Implementadas
- Entradas numéricas (precio y cantidad)
- Valores no negativos
- Opciones válidas del menú (1–9)
- Validación de encabezado CSV (nombre, precio, cantidad)
- Manejo de filas inválidas en archivos

---

## 🖥️ Uso del Programa

1. Ejecuta el archivo principal:
```bash
python app.py

	2.	Selecciona una opción del menú:

1. Agregar
2. Mostrar
3. Buscar
4. Actualizar
5. Eliminar
6. Estadísticas
7. Guardar CSV
8. Cargar CSV
9. Salir


⸻

📂 Formato del Archivo CSV

El archivo debe tener el siguiente formato:

nombre,precio,cantidad
Laptop,2500,5
Mouse,50,10
Teclado,120,7


⸻

🔄 Política de Fusión de Datos

Cuando se carga un archivo CSV sin sobrescribir:
	•	Si el producto ya existe:
	•	Se suma la cantidad
	•	Se actualiza el precio
	•	Si el producto no existe:
	•	Se agrega al inventario

⸻

⚠️ Manejo de Errores

El sistema maneja errores sin cerrarse:
	•	Archivo no encontrado
	•	Error de codificación
	•	Datos inválidos
	•	Problemas de escritura/lectura

⸻

🧠 Tecnologías Utilizadas
	•	Python 3
	•	Módulo csv
	•	Programación modular
	•	Manejo de excepciones (try/except)

⸻

✅ Criterios de Calidad Cumplidos
	•	Código legible y estructurado
	•	Funciones con docstrings
	•	Separación de responsabilidades
	•	Validaciones completas
	•	Interfaz clara por consola

⸻

📌 Notas Finales

Este proyecto es una implementación completa de un sistema de inventario básico, ideal para reforzar conceptos de programación en Python como estructuras de datos, modularidad y persistencia de información.

⸻

👨‍💻 Autor

Desarrollado por: Luis Gómez