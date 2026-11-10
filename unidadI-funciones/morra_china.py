import random


def nombre_jugada(jugada):
    if jugada == 1:
        return "Piedra"
    elif jugada == 2:
        return "Papel"
    else:
        return "Tijeras"


def leer_jugada():
    jugada_jugador = int(input("Tu jugada (1: Piedra, 2: Papel, 3: Tijeras): "))
    while jugada_jugador < 1 or jugada_jugador > 3:
        print("Jugada inválida. Intenta de nuevo.")
        jugada_jugador = int(input("Tu jugada (1: Piedra, 2: Papel, 3: Tijeras): "))
    return jugada_jugador


def leer_continuar():
    respuesta = int(input("¿Deseas jugar? (1: Sí, 2: No): "))
    while respuesta != 1 and respuesta != 2:
        print("Respuesta inválida. Escribe 1 o 2.")
        respuesta = int(input("¿Deseas jugar? (1: Sí, 2: No): "))
    return respuesta


# Retorna 0 si hay empate, 1 si gana el jugador y 2 si gana la computadora
def verificar_jugada(jugada_jugador, jugada_computadora):
    print("Tu jugada:", nombre_jugada(jugada_jugador), "- Computadora:", nombre_jugada(jugada_computadora))
    if jugada_jugador == jugada_computadora:
        print("¡Empate! Ambos eligieron lo mismo.")
        resultado = 0
    elif (jugada_jugador == 1 and jugada_computadora == 3) or \
         (jugada_jugador == 2 and jugada_computadora == 1) or \
         (jugada_jugador == 3 and jugada_computadora == 2):
        print("¡Ganaste!")
        resultado = 1
    else:
        print("¡Perdiste!")
        resultado = 2
    return resultado


def mostrar_resultados(nombre_jugador, ganadas_jugador, ganadas_computadora, empates):
    print("\nResultados finales:")
    print("Partidas ganadas por", nombre_jugador, ":", ganadas_jugador)
    print("Partidas ganadas por la computadora:", ganadas_computadora)
    print("Partidas empatadas:", empates)


def jugar_morra_china():
    ganadas_jugador = 0
    ganadas_computadora = 0
    empates = 0

    nombre_jugador = input("Ingresa tu nombre: ")
    print("¡Hola,", nombre_jugador, "! Bienvenido al juego de Morra China.")

    jugar = leer_continuar()
    while jugar == 1:
        jugada_jugador = leer_jugada()
        jugada_computadora = random.randint(1, 3)
        resultado = verificar_jugada(jugada_jugador, jugada_computadora)

        if resultado == 0:
            empates = empates + 1
        elif resultado == 1:
            ganadas_jugador = ganadas_jugador + 1
        else:
            ganadas_computadora = ganadas_computadora + 1

        jugar = leer_continuar()

    mostrar_resultados(nombre_jugador, ganadas_jugador, ganadas_computadora, empates)


jugar_morra_china()
