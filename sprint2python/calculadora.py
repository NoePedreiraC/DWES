# Importa las funciones de operaciones desde otro archivo llamado operaciones.py
from operaciones import suma, resta, multiplicacion, division

# Función para realizar operaciones repetidas
def operaciones():
    while True:
        try:
            # Solicita al usuario que ingrese dos números
            numero1 = float(input("Ingresa el primer número: "))
            numero2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Por favor, ingresa números válidos.")
            continue

        # Pide al usuario que seleccione el tipo de operación
        print("Selecciona el tipo de operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        opcion = input("Escribe el número de la operación deseada (1/2/3/4): ")

        if opcion == '1':
            resultado = suma(numero1, numero2)
        elif opcion == '2':
            resultado = resta(numero1, numero2)
        elif opcion == '3':
            resultado = multiplicacion(numero1, numero2)
        elif opcion == '4':
            resultado = division(numero1, numero2)
        else:
            print("Opción no válida.")
            continue

        print(f"Resultado: {resultado}")

        # Pregunta al usuario si quiere realizar más operaciones
        continuar = input("¿Quieres realizar más operaciones? (s/n): ").lower()
        if continuar != 's':
            break

# Llama a la función para realizar operaciones
operaciones()
