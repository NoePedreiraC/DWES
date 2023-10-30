# Definimos la adivinanza y las opciones
adivinanza = "¿Qué animal camina en cuatro patas por la mañana, en dos patas al mediodía y en tres patas por la noche?"
opciones = {
    'a': 'Un perro',
    'b': 'Un gato',
    'c': 'Un elefante'
}

# Imprimimos la adivinanza y las opciones
print(adivinanza)
for opcion, descripcion in opciones.items():
    print(f'({opcion}) {descripcion}')

# Solicitamos la respuesta al usuario
respuesta = input("Elije la opción correcta (a, b o c): ").lower()

# Verificamos si la respuesta es correcta
if respuesta == 'b':
    print("¡Correcto! La respuesta es un gato.")
else:
    print("Respuesta incorrecta. La respuesta correcta es (b) Un gato.")