from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Tcanciones

from django.views.decorators.csrf import csrf_exempt
from .models import Tcanciones, Tcomentarios
import json
# Create your views here.

def pagina_de_prueba(request):
	return HttpResponse("<h1>Hola Mundoooo</h1>")

def devolver_canciones (request):
	lista = Tcanciones.objects.all()
	respuesta_final = []
	for fila_sql in lista:
		diccionario = {}
		diccionario['id'] = fila_sql.id
		diccionario['nombre'] = fila_sql.nombre
		diccionario['url_imagen'] = fila_sql.url_imagen
		diccionario['genero'] = fila_sql.genero
		diccionario['duracion'] = fila_sql.duracion
		respuesta_final.append(diccionario)
	return JsonResponse(respuesta_final, safe=False)

def devolver_canciones_por_id (request, id_solicitado):
	cancion = Tcanciones.objects.get (id= id_solicitado)
	comentarios = cancion.tcomentarios_set.all()
	lista_comentarios = []
	for lista_comentarios_sql in comentarios:
		diccionario = {}
		diccionario['id'] = lista_comentarios_sql.id
		diccionario['comentario'] = lista_comentarios_sql.comentario
		diccionario['cancion_id'] = lista_comentarios_sql.cancion_id
		diccionario['usuario_id'] = lista_comentarios_sql.usuario_id
		diccionario['fecha'] = lista_comentarios_sql.fecha
		lista_comentarios.append(diccionario)
	resultado = {
		'id': cancion.id,
		'comentario': cancion.nombre,
		'cancion_id': cancion.url_imagen,
		'genero': cancion.genero,
		'usuario_id': cancion.duracion,
		'fecha': lista_comentarios
	}
	return JsonResponse(resultado, json_dumps_params={'ensure_ascii':False})

@csrf_exempt
def guardar_comentario(request, cancion_id):
	if request.method != 'POST':
		return None

	json_peticion = json.loads(request.body)
	comentario = Tcomentarios()
	comentario.comentario = json_peticion['nuevo_comentario']
	comentario.cancion = Tcanciones.objects.get(id = cancion_id)
	comentario.save()
	return JsonResponse({"status":"ok"})
