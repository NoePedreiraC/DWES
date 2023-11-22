from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Tcanciones
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
