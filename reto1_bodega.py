#Devuelve True si la pila no tiene cajas.
def esta_vacia(pila):
    return len(pila) == 0


#Devuelve cuántas cajas hay en la pila.
def cantidad_cajas(pila):
    return len(pila)


#Valida el código y, si es correcto, coloca la caja en el tope.
#Devuelve True si se apiló y False si se rechazó.
def apilar(pila, codigo):
    #strip() quita espacios al inicio y al final;
    #upper() pasa a mayúsculas para que "c001" y "C001" sean el mismo código
    codigo = codigo.strip().upper()

    #Regla 3: se rechazan códigos vacíos
    if codigo == "":
        print("Error: el código no puede estar vacío.")
        return False

    #Regla 2 y 3: cada caja tiene un código único, se rechazan duplicados
    if codigo in pila:
        print(f"Error: ya existe una caja con el código {codigo}.")
        return False

    #append() agrega la caja al final de la lista, que es el tope
    pila.append(codigo)
    print(f"Caja {codigo} apilada correctamente.")
    return True


#Retira la caja del tope. Regla 4: no retira si la pila está vacía.
#Devuelve el código retirado o None si no se pudo retirar.
def desapilar(pila):
    if esta_vacia(pila):
        print("No se puede desapilar: la pila está vacía.")
        return None

    #pop() quita y devuelve el último elemento (la caja del tope)
    caja = pila.pop()
    print(f"Caja retirada: {caja}")
    return caja


#Muestra la caja del tope sin retirarla.
def consultar_tope(pila):
    if esta_vacia(pila):
        print("La pila está vacía, no hay caja en el tope.")
    else:
        # pila[-1] es el último elemento de la lista (el tope)
        print(f"Caja en el tope: {pila[-1]}")


#Dibuja la pila en la consola (simulación gráfica) de arriba hacia abajo.
def dibujar_pila(pila):
    #El ancho de cada caja se ajusta al código más largo
    ancho = 12
    for caja in pila:
        if len(caja) + 4 > ancho:
            ancho = len(caja) + 4

    margen = " " * 10
    borde = margen + "+" + "-" * ancho + "+"
    print(borde)

    #Se recorre la lista desde el final (tope) hasta el inicio (fondo)
    for i in range(len(pila) - 1, -1, -1):
        if i == len(pila) - 1:
            etiqueta = "  TOPE -> "
        else:
            etiqueta = margen
        #center() centra el código dentro del ancho de la caja
        fila = etiqueta + "|" + pila[i].center(ancho) + "|"
        if i == 0:
            fila = fila + " <- FONDO"
        print(fila)
        print(borde)


#Muestra la pila completa y la cantidad de cajas (regla 5).
def mostrar_pila(pila):
    if esta_vacia(pila):
        print("La pila está vacía.")
    else:
        print("\nEstado de la bodega (de arriba hacia abajo):")
        dibujar_pila(pila)
    print(f"Cantidad de cajas: {cantidad_cajas(pila)}")


#Funciones del menú

#Imprime las opciones del menú.
def mostrar_menu():
    print("\n========== BODEGA: CONTROL DE CAJAS ==========")
    print("1. Apilar caja")
    print("2. Desapilar caja")
    print("3. Consultar tope")
    print("4. Mostrar pila")
    print("5. Salir")


#Pide una opción y la repite hasta que sea válida (del 1 al 5).
def leer_opcion():
    opcion = input("Seleccione una opción (1-5): ").strip()
    while opcion not in ("1", "2", "3", "4", "5"):
        print("Opción no válida, intente de nuevo.")
        opcion = input("Seleccione una opción (1-5): ").strip()
    return opcion


#Función principal: crea la pila vacía y repite el menú hasta salir.
def main():
    bodega = []
    opcion = ""

    while opcion != "5":
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == "1":
            codigo = input("Código de la caja: ")
            if apilar(bodega, codigo):
                print(f"Cantidad de cajas: {cantidad_cajas(bodega)}")
        elif opcion == "2":
            if desapilar(bodega) is not None:
                print(f"Cantidad de cajas: {cantidad_cajas(bodega)}")
        elif opcion == "3":
            consultar_tope(bodega)
        elif opcion == "4":
            mostrar_pila(bodega)

    print("Programa finalizado. ¡Hasta luego!")

