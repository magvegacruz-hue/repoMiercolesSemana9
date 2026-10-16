def esta_vacio(historial):
    return len(historial) == 0

def visitar(historial, pagina):
    pagina = pagina.strip().lower()
    if pagina == "":
        print("Error: la dirección no puede estar vacía.")
        return False
    if " " in pagina or "." not in pagina:
        print("Error: escriba una dirección válida, por ejemplo python.org")
        return False
    if not esta_vacio(historial) and historial[-1] == pagina:
        print(f"Ya se encuentra en {pagina}.")
        return False
    historial.append(pagina)
    print(f"Visitando: {pagina}")
    return True

def regresar(historial):
    if len(historial) < 2:
        print("No existen páginas anteriores")
        return None
    historial.pop()
    print(f"Regresó a: {historial[-1]}")
    return historial[-1]

def pagina_actual(historial):
    if esta_vacio(historial):
        print("Todavía no ha visitado ninguna página.")
    else:
        print(f"Página actual: {historial[-1]}")

def mostrar_historial(historial):
    if len(historial) < 2:
        print("No hay páginas pendientes de retroceso.")
        return
    print("Historial pendiente de retroceso (de la más reciente a la más antigua):")
    posicion = 1
    for i in range(len(historial) - 2, -1, -1):
        print(f"  {posicion}. {historial[i]}")
        posicion = posicion + 1
    print(f"Páginas para regresar: {len(historial) - 1}")

def prueba_obligatoria():
    print("\n----- PRUEBA OBLIGATORIA -----")
    prueba = []
    visitar(prueba, "uam.edu.ni")
    visitar(prueba, "python.org")
    visitar(prueba, "github.com")
    for vez in range(1, 4):
        print(f"Regreso {vez}:", end=" ")
        regresar(prueba)
    print("----- FIN DE LA PRUEBA -----")

def mostrar_menu():
    print("\n========== SIMULADOR DE NAVEGACIÓN ==========")
    print("1. Visitar página nueva")
    print("2. Regresar a la página anterior")
    print("3. Consultar página actual")
    print("4. Mostrar historial de retroceso")
    print("5. Ejecutar prueba obligatoria")
    print("6. Salir")

def leer_opcion():
    opcion = input("Seleccione una opción (1-6): ").strip()
    while opcion not in ("1", "2", "3", "4", "5", "6"):
        print("Opción no válida, intente de nuevo.")
        opcion = input("Seleccione una opción (1-6): ").strip()
    return opcion

def main():
    historial = []
    opcion = ""
    while opcion != "6":
        mostrar_menu()
        opcion = leer_opcion()
        if opcion == "1":
            pagina = input("Dirección de la página: ")
            visitar(historial, pagina)
        elif opcion == "2":
            regresar(historial)
        elif opcion == "3":
            pagina_actual(historial)
        elif opcion == "4":
            mostrar_historial(historial)
        elif opcion == "5":
            prueba_obligatoria()
    print("Navegador cerrado.")

if __name__ == "__main__":
    main()