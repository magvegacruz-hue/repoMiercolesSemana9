from collections import deque

def pause():
    input("\nPresione enter o cualquier tecla para continuar...")

def attention():
    line = deque()
    turncount = 1

    while True:
        try:
            print("="*13)
            print("--Atencion al Cliente--")
            print("1. Registrar Cliente")
            print("2. Atender al Siguiente Cliente.")
            print("3. Consultar Proximo Cliente.")
            print("4. Mostrar Linea de Espera")
            print("5. Mostrar Cantidad de Pendientes")
            print("0. Salir")
            print("="*13)
            
            opcion = int(input("ELija una opcion: "))
            
            
            if opcion == 1:
                name = input("Ingrese el nombre del cliente: ").strip()
                if not name:
                    print("Error: el nombre no puede estar vacio, intente de nuevo.")
                else:
                    line.append((turncount, name))
                    print(f"Cliente Registrado: Turno #{turncount} - {name}")
                    turncount += 1
                    pause()

        
            elif opcion == 2:
                if not line:
                    print("Error: Sin clientes que atender.")
                else:
                    turn, name = line.popleft()
                    print(f"Atendiendo al cliente: Turno #{turn} - {name}")
                    pause()
        
            
            elif opcion == 3:
                if not line:
                    print("Error: No hay clientes que atender.")
                else:
                    turn, name = line[0]
                    print(f"Proximo cliente a atender: Turno #{turn} - {name}")  
                    pause()
       
            
            elif opcion == 4:
                if not line:
                    print("Error: La cola esta vacia.")
                else:
                    print ("\n--Lista de Espera--")
                    for turn, name in line:
                        print(f"- Turno #{turn}: {name}")
                    pause()

            
            elif opcion == 5:
               print(f"Clientes pendientes en la cola: {len(line)}")
               pause()

            elif opcion == 0:
                print("Programa Terminado, buenas noches :P.")
                break

            else:
                print("Error: las opciones validas son del 0 a 5, pruebe de nuevo. :v")

        except ValueError:
            print("Error: Opcion no valida, intente de nuevo.")

if __name__ == "__main__":
    attention()
                    


