def pedir_sueldo():
    sueldo_base = float(input('Ingresa el sueldo del trabajador: '))
    while sueldo_base <= 0:
        sueldo_base = float(input('Error, el sueldo debe ser superior a 0. Ingresa el sueldo del trabajador: '))    
    return sueldo_base

def pedir_horas_extras():
    horas_extras = float(input('Indica las horas extras trabajadas: '))
    while horas_extras < 0:
        horas_extras = float(input('Error las horas extras no pueden ser negativas. Indica las horas extras trabajadas: '))
    return horas_extras

def get_bono(horas_extras):
    if horas_extras < 5:
        bono = 15
    elif horas_extras >= 5 and horas_extras <= 25:
        bono =  20
    elif horas_extras > 25 and horas_extras <= 35:
        bono = 25
    else:
        bono = 50
    return bono * horas_extras

def calcula_salario(sueldo, bono):\
    return sueldo + bono

def get_categoria(salario):
    if salario > 3000 and salario <= 4000:
        mensaje = "Bueno"
    elif salario > 4000:
        mensaje = "Meritorio"
    else:
        mensaje = "Aceptable"
    return mensaje

def imprimir_datos(sueldo_base, horas_extras, bono, salario, categoria_empleado):
    print(f'''El empleado tiene un sueldo base de : 
    - sueldo base: {sueldo_base: .2f} $$
    - ha realizado {horas_extras: .2f} horas
    - ha obtenido un bono de {bono: .2f} $$
    - su sueldo total es {salario: .2f} $$
    - y su categoria es {categoria_empleado}
    ''')

def main():
    sueldo_base = pedir_sueldo()
    horas_extras = pedir_horas_extras()
    bono = get_bono(horas_extras)
    salario = calcula_salario(sueldo_base, bono)
    categoria_empleado = get_categoria(salario)
    imprimir_datos(sueldo_base, horas_extras, bono, salario, categoria_empleado)
    
main()
    



