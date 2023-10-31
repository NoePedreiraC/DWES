 # Definimos las adivinanzas y las opciones en un diccionario
adivinanzas = {
    1: {
        'pregunta': "¿Qué animal camina en cuatro patas por la mañana, en dos patas al mediodía y en tres patas por la noche?",
        'opciones': {
            'a': 'Un perro',
            'b': 'Un gato',
            'c': 'Un elefante'
        },
        'respuesta_correcta': 'b'
    },
    2: {
        'pregunta': "Tiene dientes y no puede comer, ¿qué es?",
        'opciones': {
            'a': 'Un peine',
            'b': 'Un cuchillo',
            'c': 'Un tenedor'
        },
        'respuesta_correcta': 'a'
    },
    3: {
        'pregunta': "Es redonda como la luna, pero siempre llena de estrellas, ¿qué es?",
        'opciones': {
            'a': 'Una ventana',
            'b': 'Una puerta',
            'c': 'Una mesa'
        },
        'respuesta_correcta': 'a'
    }
}

# Inicializamos la puntuación del usuario
puntuacion = 0

# Iteramos a través de las adivinanzas
for num_adivinanza, adivinanza_info in adivinanzas.items():
    pregunta = adivinanza_info['pregunta']
    opciones = adivinanza_info['opciones']

    # Imprimimos la adivinanza y las opciones
    print(f"\nAdivinanza {num_adivinanza}:\n{pregunta}")
    for opcion, descripcion in opciones.items():
        print(f'({opcion}) {descripcion}')

    # Solicitamos la respuesta al usuario
    respuesta = input("Elige la opción correcta (a, b o c): ").lower()

    # Verificamos si la respuesta es correcta
    if respuesta == adivinanza_info['respuesta_correcta']:
        print("¡Correcto! Has ganado 10 puntos.")
        puntuacion += 10
    else:
        print(f"Respuesta incorrecta. La respuesta correcta es ({adivinanza_info['respuesta_correcta']}). Has perdido 5 puntos.")
        puntuacion -= 5

# Imprimimos la puntuación final del usuario
print(f"\nPuntuación final: {puntuacion} puntos")
