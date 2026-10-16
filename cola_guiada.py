cola = []


def registrar_paciente(nombre):
    cola.append(nombre)
    print(f"Registrado: {nombre}")

def atender_paciente():
    if not cola:
        print("No hay pacientes en espera")
    else:
        paciente = cola.pop(0)
        print(f"Atendiendo a: {paciente}")

def mostrar_cola():
    if not cola:
        print("La cola está vacía")
    else:
        print("Pacientes en espera:")
        for posicion, paciente in enumerate(cola, 1):
            print(f"{posicion}. {paciente}")

def leer_nombre():
    nombre = input("Nombre del paciente: ").strip()
    while nombre == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Nombre del paciente: ").strip()
    return nombre

def mostrar_menu():
    print("\n========== CLÍNICA: COLA DE PACIENTES ==========")
    print("1. Registrar paciente")
    print("2. Atender paciente")
    print("3. Mostrar cola")
    print("4. Salir")

def leer_opcion():
    opcion = input("Seleccione una opción (1-4): ").strip()
    while opcion not in ("1", "2", "3", "4"):
        print("Opción no válida, intente de nuevo.")
        opcion = input("Seleccione una opción (1-4): ").strip()
    return opcion

def main():
    opcion = ""
    while opcion != "4":
        mostrar_menu()
        opcion = leer_opcion()
        if opcion == "1":
            registrar_paciente(leer_nombre())
        elif opcion == "2":
            atender_paciente()
        elif opcion == "3":
            mostrar_cola()
    print("Sistema de la clínica cerrado.")
