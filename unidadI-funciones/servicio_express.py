def menu():
    print("\n===== SISTEMA DE ENCOMIENDAS =====")
    print("1. Registrar y calcular encomienda")
    print("2. Mostrar reporte estadístico del día")
    print("3. Salir")
    opcion = int(input("Ingrese su opción: "))
    while opcion < 1 or opcion > 3:
        print("Opción inválida. Intente de nuevo.")
        opcion = int(input("Ingrese su opción: "))
    return opcion


def leer_tipo_servicio():
    tipo = int(input("Tipo de servicio (1: Documento/Sobre, 2: Paquete Mediano, 3: Carga pesada/Industrial): "))
    while tipo < 1 or tipo > 3:
        print("Tipo de servicio inválido. Intente de nuevo.")
        tipo = int(input("Tipo de servicio (1: Documento/Sobre, 2: Paquete Mediano, 3: Carga pesada/Industrial): "))
    return tipo


def leer_peso():
    peso = float(input("Peso de la encomienda en kg: "))
    while peso <= 0:
        print("Peso inválido. Intente de nuevo.")
        peso = float(input("Peso de la encomienda en kg: "))
    return peso


def leer_zona():
    zona = int(input("Zona de entrega (1: Urbana, 2: Periférica, 3: Foránea/Rural): "))
    while zona < 1 or zona > 3:
        print("Zona inválida. Intente de nuevo.")
        zona = int(input("Zona de entrega (1: Urbana, 2: Periférica, 3: Foránea/Rural): "))
    return zona


def tarifa_por_tipo(tipo):
    if tipo == 1:
        return 2
    elif tipo == 2:
        return 6
    else:
        return 15


def recargo_zona(zona):
    if zona == 1:
        return 0.0
    elif zona == 2:
        return 0.15
    else:
        return 0.30


def descuento_fact_alt(costo):
    if costo > 25:
        return costo * 0.10
    return 0


def calcular_monto(tipo, peso, zona):
    costo = tarifa_por_tipo(tipo) * peso
    costo = costo + costo * recargo_zona(zona)
    costo = costo - descuento_fact_alt(costo)
    return costo


def registrar_encomienda():
    tipo = leer_tipo_servicio()
    peso = leer_peso()
    zona = leer_zona()
    monto = calcular_monto(tipo, peso, zona)
    if tipo == 1:
        print(f"Tipo de servicio: Documento/Sobre - Peso: {peso} kg")
    elif tipo == 2:
        print(f"Tipo de servicio: Paquete Mediano - Peso: {peso} kg")
    else:
        print(f"Tipo de servicio: Carga pesada/Industrial - Peso: {peso} kg")
    print(f"Monto a pagar: $ {monto:.2f}")
    return tipo, peso, zona, monto


def reporte_estadistico(total_documentos, total_medianos, total_carga_pesada,
                        total_zona1, total_zona2, total_zona3,
                        peso_total, monto_total_dia):
    cantidad_paquetes = total_documentos + total_medianos + total_carga_pesada
    if cantidad_paquetes > 0:
        promedio_peso = peso_total / cantidad_paquetes
    else:
        promedio_peso = 0

    print("\n===== REPORTE ESTADÍSTICO DEL DÍA =====")
    print("Paquetes procesados por tipo:")
    print(f"  Documentos: {total_documentos}")
    print(f"  Medianos: {total_medianos}")
    print(f"  Carga Pesada: {total_carga_pesada}")
    print("Recaudación por zona de destino:")
    print(f"  Zona 1 (Urbana): $ {total_zona1:.2f}")
    print(f"  Zona 2 (Periférica): $ {total_zona2:.2f}")
    print(f"  Zona 3 (Foránea/Rural): $ {total_zona3:.2f}")
    print(f"Promedio de peso: {promedio_peso:.2f} kg")
    print(f"Monto global acumulado del día: $ {monto_total_dia:.2f}")


def main():
    # Contadores por tipo
    total_documentos = 0
    total_medianos = 0
    total_carga_pesada = 0
    # Acumuladores por zona
    total_zona1 = 0
    total_zona2 = 0
    total_zona3 = 0
    # Acumuladores generales
    peso_total = 0
    monto_total_dia = 0

    opcion = -1
    while opcion != 3:
        opcion = menu()
        if opcion == 1:
            tipo, peso, zona, monto = registrar_encomienda()

            if tipo == 1:
                total_documentos = total_documentos + 1
            elif tipo == 2:
                total_medianos = total_medianos + 1
            else:
                total_carga_pesada = total_carga_pesada + 1

            if zona == 1:
                total_zona1 = total_zona1 + monto
            elif zona == 2:
                total_zona2 = total_zona2 + monto
            else:
                total_zona3 = total_zona3 + monto

            peso_total = peso_total + peso
            monto_total_dia = monto_total_dia + monto

        elif opcion == 2:
            reporte_estadistico(total_documentos, total_medianos, total_carga_pesada,
                                total_zona1, total_zona2, total_zona3,
                                peso_total, monto_total_dia)

    print("Saliendo del sistema de encomiendas. ¡Hasta luego!")


main()
