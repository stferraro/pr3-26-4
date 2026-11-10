def mostrar_menu():
    print("\n===== SISTEMA DE ESTACIONAMIENTO =====")
    print("1. Registrar vehículo y mostrar tarifa")
    print("2. Ganancia total del día")
    print("3. Total de vehículos por tipo")
    print("0. Salir")


def leer_opcion():
    opcion = int(input("Ingrese su opción: "))
    while opcion < 0 or opcion > 3:
        print("Opción inválida. Intente de nuevo.")
        opcion = int(input("Ingrese su opción: "))
    return opcion


def leer_tipo_vehiculo():
    tipo = int(input("Tipo de vehículo (1: Moto, 2: Carro, 3: Camión): "))
    while tipo < 1 or tipo > 3:
        print("Tipo de vehículo inválido. Intente de nuevo.")
        tipo = int(input("Tipo de vehículo (1: Moto, 2: Carro, 3: Camión): "))
    return tipo


def calcular_tarifa(tipo):
    if tipo == 1:
        tarifa = 5
    elif tipo == 2:
        tarifa = 10
    else:
        tarifa = 20
    return tarifa


def mostrar_ganancia(ganancia_total):
    print("Ganancia total del día: $", ganancia_total)


def mostrar_totales(total_motos, total_carros, total_camiones):
    print("Motos:", total_motos)
    print("Carros:", total_carros)
    print("Camiones:", total_camiones)


def main():
    # Contadores y acumulador
    total_motos = 0
    total_carros = 0
    total_camiones = 0
    ganancia_total = 0

    opcion = -1
    while opcion != 0:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            codigo = int(input("Ingrese el código del vehículo: "))
            tipo = leer_tipo_vehiculo()
            tarifa = calcular_tarifa(tipo)

            if tipo == 1:
                total_motos = total_motos + 1
            elif tipo == 2:
                total_carros = total_carros + 1
            else:
                total_camiones = total_camiones + 1

            ganancia_total = ganancia_total + tarifa
            print("Vehículo", codigo, "registrado. Monto a pagar: $", tarifa)

        elif opcion == 2:
            mostrar_ganancia(ganancia_total)

        elif opcion == 3:
            mostrar_totales(total_motos, total_carros, total_camiones)

    print("Saliendo del sistema de estacionamiento. ¡Hasta luego!")


main()
