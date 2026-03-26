import csv

def guardar_csv(inventario, ruta, incluir_header=True):
    """
    Guarda el inventario en un archivo CSV.
    """
    if not inventario:
        print("Inventario vacío, no se puede guardar.")
        return

    try:
        with open(ruta, mode="w", newline="", encoding="utf-8") as archivo:
            writer = csv.writer(archivo)
            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])
            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])
        print(f"Inventario guardado en: {ruta}")
    except Exception as e:
        print(f"Error al guardar: {e}")


def cargar_csv(ruta):
    """
    Carga productos desde un archivo CSV.
    """
    inventario = []
    errores = 0

    try:
        with open(ruta, mode="r", encoding="utf-8") as archivo:
            reader = csv.reader(archivo)
            header = next(reader, None)

            if [h.strip().lower() for h in header] != ["nombre", "precio", "cantidad"]:
                print("Encabezado inválido.")
                return []

            for fila in reader:
                if len(fila) != 3:
                    errores += 1
                    continue
                try:
                    nombre = fila[0]
                    precio = float(fila[1])
                    cantidad = int(fila[2])

                    if precio < 0 or cantidad < 0:
                        errores += 1
                        continue

                    inventario.append({
                        "nombre": nombre,
                        "precio": precio,
                        "cantidad": cantidad
                    })
                except:
                    errores += 1

        print(f"Productos cargados: {len(inventario)} | Filas inválidas: {errores}")
        return inventario

    except FileNotFoundError:
        print("Archivo no encontrado.")
    except UnicodeDecodeError:
        print("Error de codificación.")
    except Exception as e:
        print(f"Error: {e}")

    return []