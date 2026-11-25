def pedir_datos():
    nombre = input('Nombre del barista: ')
    apellido = input('Apellido del barista: ')
    cedula = input('Cedula del barista: ')
    return [nombre, apellido, cedula]

def valor_plato():
    costo_plato = float(input('Ingresa el costo del plato: '))
    while costo_plato < 0:
        costo_plato = float(input('Error, el costo del plato no puede ser negativo. Ingresa el costo del plato: '))
    return costo_plato

def get_propina(costo_plato):
    if costo_plato <= 10:
        porcentaje = 0.05
    elif costo_plato > 10 and costo_plato <= 25:
        porcentaje = 0.1
    elif costo_plato > 25 and costo_plato <= 50:
        porcentaje = 0.15
    else:
        porcentaje = 0.2
    return costo_plato * porcentaje

def get_promedio(total_propinas, cantidad_platos):
    if cantidad_platos == 0:
        print('Error no se puede dividir por 0')
        return 0
    return total_propinas/cantidad_platos

def get_puntos(promedio):
    if promedio > 20 and promedio <= 50:
        return 25
    elif promedio > 50 and promedio <= 100:
        return 50
    elif promedio > 100:
        return 100
    return 10

def get_mensaje(puntos):
    if puntos == 10:
        return "Turno Tranquilo"
    if puntos == 25:
        return "Buen ritmo"
    if puntos == 50:
        return "Jornada destacada"
    if puntos == 100:
        return "Barista Estrella"
    
def menu():
    opcion = int(input('Ingresa la opcion: '))
    while opcion < 0 or opcion > 2:
        opcion = int(input('Error, la opcion debe estar entre 0 y 2. Ingresa la opcion: '))
    return opcion

def main():
    datos_barista = None
    promedio_propina = 0
    opcion = menu()
    while opcion != 0:
        match(opcion):
            case 1:
                num_platos = 0
                suma_propinas = 0
                datos_barista = pedir_datos()
                costo_plato = valor_plato()
                while costo_plato != 0:
                    propina = get_propina(costo_plato)
                    suma_propinas += propina
                    num_platos += 1
                    costo_plato = valor_plato()
                promedio_propina = get_promedio(suma_propinas, num_platos)
                print(f'''-Nombre Barista: {datos_barista[0]} 
- Apellido Barista: {datos_barista[1]}
- Cedula Barista: {datos_barista[2]}
- Promedio propinas: {promedio_propina: .2f}
''')
                opcion = menu()
            case 2:
                if datos_barista is None:
                    print('Primero debes ingresar los datos con la opción 1')
                else:
                    puntos = get_puntos(promedio_propina)
                    mensaje = get_mensaje(puntos)
                    print(f'''-Nombre Barista: {datos_barista[0]} 
- Apellido Barista: {datos_barista[1]}
- Cedula Barista: {datos_barista[2]}
- Promedio propinas: {promedio_propina: .2f}
- Puntos: {puntos}
- Calificación {mensaje}
                    ''')
                opcion = menu()
    else:
        print('Hasta luego')

main()
