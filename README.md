# repoMiercolesSemana9
Integrantes:
Miguel Angel Gonzalez Vegacruz
Marcelo Alejandro Molina Murillo
Joshua David Muller Castillo



- pila_guiada.py: pila de libros de una biblioteca. Pide los nombres con input(), muestra la pila, retira el libro del tope y vuelve a mostrarla.
- reto1_bodega.py: control de cajas en una bodega con una pila. Menú para apilar, desapilar, consultar el tope, mostrar la pila (dibujada en consola) y salir. Rechaza códigos vacíos o repetidos y no retira si la pila está vacía.
- pila_acciones.py: editor que guarda acciones en una pila para deshacer la última. Tiene menú interactivo y valida que la descripción no esté vacía.
- reto2_navegador.py: simulador de navegación. Cada página visitada se apila; regresar quita la página actual con pop(). Incluye una opción que ejecuta la prueba obligatoria.
- cola_guiada.py: cola de pacientes de una clínica, atendidos en orden de llegada, con menú interactivo.
- reto3_atencion.py: sistema de turnos de atención al cliente con una cola. Registra turno y nombre, atiende al siguiente, consulta al próximo sin retirarlo, muestra la cola (dibujada en consola) y la cantidad de pendientes.

LIFO significa "Last In, First Out": el último elemento que entra es el primero que sale. Funciona como una pila de libros o de cajas: solo se puede poner o quitar desde arriba (el tope). En Python se usa una lista: append() coloca el elemento en el tope y pop() quita el elemento del tope. Para consultar el tope sin quitarlo se usa lista[-1].

FIFO significa "First In, First Out": el primer elemento que entra es el primero que sale. Funciona como la fila de una clínica o de un banco: los que llegan se colocan al final y se atiende al que está al frente. En estos programas la cola se hizo con una lista: append() agrega al final y pop(0) quita el primero. Para consultar el frente sin quitarlo se usa lista[0].
