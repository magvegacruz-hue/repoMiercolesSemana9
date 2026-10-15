acciones = []
# Guarda una acción nueva en el tope de la pila.
def registrar_accion(descripcion):
    # append() agrega la acción al final de la lista (tope)
    acciones.append(descripcion)
    print("Acción registrada:", descripcion)

# Deshace la última acción registrada.
def deshacer():
    # Si no hay acciones se avisa y se sale de la función con return
    if not acciones:
        print("No existen acciones para deshacer")
        return
    # pop() quita la última acción, que es la que se deshace
    ultima = acciones.pop()
    print("Se deshizo:", ultima)

#Muestra las acciones que todavía se pueden deshacer.
def historial():
    print("Acciones pendientes:", acciones)
    # Además se listan desde la más reciente hasta la más antigua
    if acciones:
        print("Orden en que se desharían:")
        posicion = 1
        for i in range(len(acciones) - 1, -1, -1):
            print(f"  {posicion}. {acciones[i]}")
            posicion = posicion + 1

# Pide la descripción de la acción y no acepta textos vacíos.
def leer_descripcion():
    descripcion = input("Describa la acción: ").strip()
    while descripcion == "":
        print("La descripción no puede estar vacía.")
        descripcion = input("Describa la acción: ").strip()
    return descripcion

# Imprime las opciones del menú interactivo.
def mostrar_menu():
    print("\n========== EDITOR: DESHACER ACCIONES ==========")
    print("1. Registrar acción")
    print("2. Deshacer última acción")
    print("3. Ver historial")
    print("4. Salir")

# Pide una opción y la repite hasta que sea válida (del 1 al 4).
def leer_opcion():
    opcion = input("Seleccione una opción (1-4): ").strip()
    while opcion not in ("1", "2", "3", "4"):
        print("Opción no válida, intente de nuevo.")
        opcion = input("Seleccione una opción (1-4): ").strip()
    return opcion

# Función principal: repite el menú hasta que se elija salir.
def main():
    opcion = ""
    while opcion != "4":
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == "1":
            registrar_accion(leer_descripcion())
        elif opcion == "2":
            deshacer()
        elif opcion == "3":
            historial()
    print("Editor cerrado.")

# Seis operaciones de prueba sugeridas:
# 1) Registrar "Escribir título"
# 2) Registrar "Agregar párrafo"
# 3) Registrar "Cambiar formato"
# 4) Ver historial -> se ven las tres acciones
# 5) Deshacer -> se deshace "Cambiar formato" (la última)
# 6) Ver historial -> quedan "Escribir título" y "Agregar párrafo"
# Extra: deshacer hasta vaciar la pila para comprobar el mensaje
# "No existen acciones para deshacer".


