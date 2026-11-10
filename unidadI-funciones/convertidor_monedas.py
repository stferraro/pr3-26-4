def convertir_moneda(cantidad, tasa_cambio):
    """
    Convierte una cantidad de dinero de una moneda a otra utilizando la tasa de cambio proporcionada.
    
    :param cantidad: La cantidad de dinero a convertir.
    :param tasa_cambio: La tasa de cambio entre las dos monedas.
    :return: La cantidad convertida en la nueva moneda.
    """
    return cantidad * tasa_cambio

def main():
    print("===== CONVERTIDOR DE MONEDAS =====")
    cantidad = float(input("Ingrese la cantidad de dinero a convertir: "))
    tasa_cambio = float(input("Ingrese la tasa de cambio: "))
    
    cantidad_convertida = convertir_moneda(cantidad, tasa_cambio)
    print(f"La cantidad convertida es: {cantidad_convertida:.2f}")
    
main()