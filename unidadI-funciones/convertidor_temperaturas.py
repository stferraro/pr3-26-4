def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def menu():
    print("===== CONVERTIDOR DE TEMPERATURAS =====")
    print("1. Convertir Celsius a Fahrenheit")
    print("2. Convertir Fahrenheit a Celsius")
    print("3. Salir")
    opcion = int(input("Ingrese su opción: "))
    while opcion < 1 or opcion > 3:
        print("Opción inválida. Intente de nuevo.")
        opcion = int(input("Ingrese su opción: "))
    return opcion

def main():
    opcion = -1
    while opcion != 3:
        opcion = menu()
        if opcion == 1:
            celsius = float(input("Ingrese la temperatura en Celsius: "))
            fahrenheit = celsius_a_fahrenheit(celsius)
            print(f"{celsius}°C son {fahrenheit:.2f}°F")
        elif opcion == 2:
            fahrenheit = float(input("Ingrese la temperatura en Fahrenheit: "))
            celsius = fahrenheit_a_celsius(fahrenheit)
            print(f"{fahrenheit}°F son {celsius:.2f}°C")
    print("Saliendo del convertidor de temperaturas. ¡Hasta luego!")
    
main()