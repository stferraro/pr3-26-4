def calcular_imc(peso, estatura):
    return peso/estatura**2

def condicion_persona(imc):
    if imc < 18.50:
        return 'Bajo Peso'
    elif imc >= 18.50 and imc < 24.90:
        return 'Peso Saludale'
    elif imc >= 24.90 and imc < 29.90:
        return 'Sobrepeso'
    return 'Obesidad'

def main():
    peso = float(input('Peso de la persona: '))
    while peso < 0:
        peso = float(input('Peso de la persona: '))
    estatura = float(input('Estatura de la persona: '))
    while estatura < 0:
        estatura = float(input('Estatura de la persona: '))
    imc = calcular_imc(peso, estatura)
    print(f'Tu indice de masa corporea es: {imc: .2f}')
    print('La condicion de la persona es: ', condicion_persona(imc))
    
main()