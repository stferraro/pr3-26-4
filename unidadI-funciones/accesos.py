TARIFA_EXPRESS = 2.50
RECARGO_NOCTURNO = 5.00


def mostrar_menu():
    print("\n===== SISTEMA DE ACCESO =====")
    print("1. Registrar y calcular servicio operativo")
    print("2. Consultar tarifas vigentes")
    print("3. Simular cobro express")
    print("4. Salir")


def leer_horas():
    num_horas = float(input("Ingrese el número de horas de estancia: "))
    while num_horas <= 0:
        print("Las horas deben ser mayores a cero. Intente de nuevo.")
        num_horas = float(input("Ingrese el número de horas de estancia: "))
    return num_horas


def leer_tarifa():
    tarifa = float(input("Ingrese la tarifa base por hora: "))
    while tarifa <= 0:
        print("La tarifa debe ser mayor a cero. Intente de nuevo.")
        tarifa = float(input("Ingrese la tarifa base por hora: "))
    return tarifa


def leer_nocturno():
    respuesta = int(input("¿El servicio es en horario nocturno? (1: Sí, 2: No): "))
    while respuesta != 1 and respuesta != 2:
        print("Respuesta inválida. Escriba 1 o 2.")
        respuesta = int(input("¿El servicio es en horario nocturno? (1: Sí, 2: No): "))
    return respuesta == 1


def calcular_monto(num_horas, tarifa, nocturno):
    total = num_horas * tarifa
    if num_horas > 8:
        total = total * 0.9  # Descuento del 10% por más de 8 horas
    if nocturno:
        total = total + RECARGO_NOCTURNO  # Recargo fijo por servicio nocturno
    return total


def registrar_servicio():
    num_horas = leer_horas()
    tarifa = leer_tarifa()
    nocturno = leer_nocturno()
    total = calcular_monto(num_horas, tarifa, nocturno)
    print("Monto a pagar por el servicio: $", round(total, 2))
    return tarifa


def mostrar_tarifas(tarifa_base):
    print("Tarifas vigentes:")
    if tarifa_base == 0:
        print("- Tarifa base por hora: aún no se ha registrado ningún servicio")
    else:
        print("- Tarifa base por hora: $", tarifa_base)
    print("- Tarifa express por hora: $", TARIFA_EXPRESS)
    print("- Recargo nocturno: $", RECARGO_NOCTURNO, "fijo")
    print("- Descuento: 10% sobre el monto base si la estancia supera las 8 horas")


def simular_cobro_express():
    num_horas = leer_horas()
    total = calcular_monto(num_horas, TARIFA_EXPRESS, False)
    print(f"Monto a pagar por el servicio express: ${total:.2f}")


def main():
    tarifa_base = 0
    opcion = -1
    while opcion != 4:
        mostrar_menu()
        opcion = int(input("Ingrese su opción: "))
        while opcion < 1 or opcion > 4:
            print("Opción inválida. Intente de nuevo.")
            opcion = int(input("Ingrese su opción: "))

        if opcion == 1:
            tarifa_base = registrar_servicio()
        elif opcion == 2:
            mostrar_tarifas(tarifa_base)
        elif opcion == 3:
            simular_cobro_express()

    print("Saliendo del sistema de acceso. ¡Hasta luego!")


main()
