import math

def get_radio(diametro):
    return diametro/2

def get_area(radio):
    return math.pi * radio ** 2

def get_perimetro(radio):
    return math.pi * radio * 2

def imprimir_datos(diametro, radio, area, perimetro):
    print(f'''El circulo de diametro {diametro: .2f} cm y radio {radio: .2f} cm tiene:
          - Perimetro: {perimetro: .2f} cm
          - Area: {area: .2f} cm²
          ''')

def main():
    diametro = float(input('Ingresa el valor del diametro del circulo en cm: '))
    while diametro < 0:
        diametro = float(input('Error, Ingresa el valor del diametro del circulo en cm, no puede ser igual a 0: '))
    radio = get_radio(diametro)
    area = get_area(radio)
    perimetro = get_perimetro(radio)
    imprimir_datos(diametro, radio, area, perimetro)
    
main()
    