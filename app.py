from servicios import *
from archivos import *

inventario = []

while True:
    print("\n1. Agregar\n2. Mostrar\n3. Buscar\n4. Actualizar\n5. Eliminar\n6. Estadísticas\n7. Guardar CSV\n8. Cargar CSV\n9. Salir")
    
    try:
        opcion = int(input("Seleccione una opción: "))
    except:
        print("Opción inválida.")
        continue

    if opcion == 1:
        nombre = input("Nombre: ")
        try:
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))
            if precio < 0 or cantidad < 0:
                print("Valores no negativos.")
                continue
            agregar_producto(inventario, nombre, precio, cantidad)
        except:
            print("Error en datos.")

    elif opcion == 2:
        mostrar_inventario(inventario)

    elif opcion == 3:
        nombre = input("Buscar: ")
        p = buscar_producto(inventario, nombre)
        print(p if p else "No encontrado.")

    elif opcion == 4:
        nombre = input("Actualizar: ")
        try:
            precio = input("Nuevo precio (enter para omitir): ")
            cantidad = input("Nueva cantidad (enter para omitir): ")

            precio = float(precio) if precio else None
            cantidad = int(cantidad) if cantidad else None

            if actualizar_producto(inventario, nombre, precio, cantidad):
                print("Actualizado.")
            else:
                print("No encontrado.")
        except:
            print("Error en datos.")

    elif opcion == 5:
        nombre = input("Eliminar: ")
        print("Eliminado." if eliminar_producto(inventario, nombre) else "No encontrado.")

    elif opcion == 6:
        stats = calcular_estadisticas(inventario)
        if stats:
            print(stats)
        else:
            print("Inventario vacío.")

    elif opcion == 7:
        ruta = input("Ruta archivo: ")
        guardar_csv(inventario, ruta)

    elif opcion == 8:
        ruta = input("Ruta archivo: ")
        datos = cargar_csv(ruta)
        if datos:
            decision = input("¿Sobrescribir inventario? (S/N): ").lower()
            if decision == "s":
                inventario = datos
            else:
                for nuevo in datos:
                    existente = buscar_producto(inventario, nuevo["nombre"])
                    if existente:
                        existente["cantidad"] += nuevo["cantidad"]
                        existente["precio"] = nuevo["precio"]
                    else:
                        inventario.append(nuevo)

    elif opcion == 9:
        print("Saliendo...")
        break

    else:
        print("Opción inválida.")