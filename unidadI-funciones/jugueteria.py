PESO_PAYASO = 112
PESO_MUNECA = 75

def calcular_peso_total(num_payasos, num_munecas):
    return (PESO_PAYASO*num_payasos)+(PESO_MUNECA*num_munecas)

numeroPayasos = int(input('Indica el numero de payasos del paquete: '))
peso_total=calcular_peso_total(numeroPayasos, num_munecas=4)
print(f'El peso del paquete es: {peso_total}')