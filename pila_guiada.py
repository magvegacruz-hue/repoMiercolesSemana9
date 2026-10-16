pila = []

# Agrega un libro en el tope de la pila.
def apilar(libro):
    # append() coloca el libro al final de la lista, es decir, en el tope
    pila.append(libro)
    print(f"Libro agregado: {libro}")

# Retira el libro que está en el tope de la pila.
def desapilar():
    # Antes de retirar se revisa que la pila no esté vacía
    if len(pila) == 0:
        print("La pila está vacía")
    else:
        # pop() quita y devuelve el último elemento de la lista (el tope)
        libro = pila.pop()
        print(f"Libro retirado: {libro}")

# Muestra todos los libros de la pila y el que está en el tope.
def mostrar_pila():
    if not pila:
        print("No hay libros")
    else:
        print("Pila actual:", pila)
        # pila[-1] consulta el último elemento sin retirarlo
        print("Libro en el tope:", pila[-1])

# Paso 4: pregunta cuántos libros se van a apilar.
# Repite la pregunta hasta que se escriba un número entero mayor que cero.
def leer_cantidad():
    cantidad = input("¿Cuántos libros desea apilar?: ").strip()
    # isdigit() revisa que el texto solo tenga dígitos
    while not cantidad.isdigit() or int(cantidad) == 0:
        print("Debe escribir un número entero mayor que cero.")
        cantidad = input("¿Cuántos libros desea apilar?: ").strip()
    return int(cantidad)

# Paso 4: solicita el nombre de un libro con input().
# No acepta nombres vacíos.
def leer_libro(numero):
    libro = input(f"Nombre del libro {numero}: ").strip()
    while libro == "":
        print("El nombre del libro no puede estar vacío.")
        libro = input(f"Nombre del libro {numero}: ").strip()
    return libro

# Función principal: reúne los pasos de la práctica.
# Paso 2 (versión original): se apilaban "Matemáticas", "Programación"
# y "Base de Datos" escritos directamente en el código.
# Paso 4: ahora los nombres se piden al usuario con input().
def main():
    cantidad = leer_cantidad()
    for numero in range(1, cantidad + 1):
        apilar(leer_libro(numero))

    mostrar_pila()
    desapilar()
    mostrar_pila()

if __name__ == "__main__":
    main()


# Paso 3 - Respuestas:
# ¿Qué libro se retira primero? El último que se apiló (en el ejemplo
# original, "Base de Datos").
# ¿Por qué? Porque la pila trabaja con LIFO (último en entrar, primero
# en salir): pop() siempre saca el elemento que está en el tope.
# ¿Qué sucede si se intenta retirar de una pila vacía? El programa
# muestra "La pila está vacía" gracias a la validación. Sin esa
# validación, pop() sobre una lista vacía produce el error
# IndexError: pop from empty list y el programa se detiene.
