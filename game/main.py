import random

# Opciones del juego
opciones = ["Piedra", "Papel", "Tijera"]

# Puntuación inicial
puntos_usuario = 0
puntos_computadora = 0

# Bucle hasta que alguien gane 2 veces
while puntos_usuario < 2 and puntos_computadora < 2:
    # Elección del usuario
    usuario = input("Elige Piedra, Papel o Tijera: ").capitalize()
    
    # Validar entrada del usuario
    if usuario not in opciones:
        print("Opción no válida. Intenta de nuevo.")
        continue
    
    # Elección de la computadora
    computadora = random.choice(opciones)
    
    # Imprimir elecciones
    print(f"Tú elegiste: {usuario}")
    print(f"La computadora eligió: {computadora}")
    
    # Determinar el ganador de la ronda
    if usuario == computadora:
        print("¡Es un empate!")
    elif (usuario == "Piedra" and computadora == "Tijera") or \
         (usuario == "Papel" and computadora == "Piedra") or \
         (usuario == "Tijera" and computadora == "Papel"):
        print("¡Ganaste esta ronda!")
        puntos_usuario += 1
    else:
        print("¡La computadora ganó esta ronda!")
        puntos_computadora += 1
    
    # Mostrar puntuaciones
    print(f"Puntuación: Tú {puntos_usuario} - {puntos_computadora} Computadora\n")

# Declarar al ganador final
if puntos_usuario == 2:
    print("🎉 ¡Felicidades, ganaste el juego! 🎉")
else:
    print("🤖 La computadora ganó el juego. ¡Suerte para la próxima!")