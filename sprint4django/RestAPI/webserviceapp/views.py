from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Tcanciones

# Importando decorador csrf_exempt para permitir solicitudes POST sin CSRF
from django.views.decorators.csrf import csrf_exempt
from .models import Tcanciones, Tcomentarios
import json

# Definición de vistas

def pagina_de_prueba(request):
    return HttpResponse("<h1>Hola Mundoooo</h1>")

def devolver_canciones(request):
    # Obtener todas las canciones de la base de datos
    lista = Tcanciones.objects.all()
    respuesta_final = []

    # Iterar sobre las canciones y agregar la información relevante a la lista de respuesta
    for fila_sql in lista:
        diccionario = {
            'id': fila_sql.id,
            'nombre': fila_sql.nombre,
            'url_imagen': fila_sql.url_imagen,
            'genero': fila_sql.genero,
            'duracion': fila_sql.duracion
        }
        respuesta_final.append(diccionario)

    # Devolver la lista de canciones en formato JSON
    return JsonResponse(respuesta_final, safe=False)

def devolver_canciones_por_id(request, id_solicitado):
    # Obtener una canción por su ID
    cancion = Tcanciones.objects.get(id=id_solicitado)
    comentarios = cancion.tcomentarios_set.all()
    lista_comentarios = []

    # Iterar sobre los comentarios de la canción y agregar la información a la lista de comentarios
    for lista_comentarios_sql in comentarios:
        diccionario = {
            'id': lista_comentarios_sql.id,
            'comentario': lista_comentarios_sql.comentario,
            'cancion_id': lista_comentarios_sql.cancion_id,
            'usuario_id': lista_comentarios_sql.usuario_id,
            'fecha': lista_comentarios_sql.fecha
        }
        lista_comentarios.append(diccionario)

    # Crear un diccionario con la información de la canción y los comentarios asociados
    resultado = {
        'id': cancion.id,
        'comentario': cancion.nombre,
        'cancion_id': cancion.url_imagen,
        'genero': cancion.genero,
        'usuario_id': cancion.duracion,
        'fecha': lista_comentarios
    }

    # Devolver la información en formato JSON
    return JsonResponse(resultado, json_dumps_params={'ensure_ascii': False})

@csrf_exempt
def guardar_comentario(request, cancion_id):
    # Verificar que la solicitud sea de tipo POST
    if request.method != 'POST':
        return None

    # Convertir el cuerpo de la solicitud a un objeto JSON
    json_peticion = json.loads(request.body)

    # Crear un nuevo comentario y asignarle la información proporcionada
    comentario = Tcomentarios()
    comentario.comentario = json_peticion['nuevo_comentario']
    comentario.cancion = Tcanciones.objects.get(id=cancion_id)
    comentario.save()

    # Devolver una respuesta en formato JSON
    return JsonResponse({"status": "ok"})
