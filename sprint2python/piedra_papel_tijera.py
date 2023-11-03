import random

# Inicializar las puntuaciones
puntuacion_usuario = 0
puntuacion_maquina = 0
victorias_necesarias = 5

# Crear un diccionario para las opciones del juego
opciones = {"piedra": "tijera", "papel": "piedra", "tijera": "papel"}

# Bucle para jugar hasta que haya 5 victorias o 5 derrotas y que los empates no se cuenten como ronda
while puntuacion_usuario < victorias_necesarias and puntuacion_maquina < victorias_necesarias:
    # Solicitar la elección del usuario
    eleccion_usuario = input("Elige una opción (piedra, papel o tijera): ").lower()

    # Generar una elección aleatoria para la máquina
    eleccion_maquina = random.choice(list(opciones.keys()))

    # Comprobar quién gana
    if eleccion_usuario in opciones:
        if eleccion_usuario == eleccion_maquina:
            print(f"Empate, ambos eligieron {eleccion_usuario}.")
        elif opciones[eleccion_usuario] == eleccion_maquina:
            print(f"Has ganado, {eleccion_usuario} gana a {eleccion_maquina}.")
            puntuacion_usuario += 1
        else:
            print(f"Has perdido, {eleccion_maquina} gana a {eleccion_usuario}.")
            puntuacion_maquina += 1
    else:
        print("Elección no válida. Debes elegir piedra, papel o tijera.")

# Mostrar el resultado final
if puntuacion_usuario == victorias_necesarias:
    print("¡Has ganado el juego!")
else:
    print("Has perdido el juego. La máquina gana.")