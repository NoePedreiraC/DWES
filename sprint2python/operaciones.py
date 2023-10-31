# Función para realizar una suma
def suma(a, b):
    return a + b

# Función para realizar una resta
def resta(a, b):
    return a - b

# Función para realizar una multiplicación
def multiplicacion(a, b):
    return a * b

# Función para realizar una división con control de división por cero
def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

 #Solicitar al usuario que ingrese dos números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Realizar las operaciones y mostrar los resultados
print(f"Suma: {numero1} + {numero2} = {suma(numero1, numero2)}")
print(f"Resta: {numero1} - {numero2} = {resta(numero1, numero2)}")
print(f"Multiplicación: {numero1} * {numero2} = {multiplicacion(numero1, numero2)}")
print(f"División: {numero1} / {numero2} = {division(numero1, numero2)}")























