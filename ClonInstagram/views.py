#vistas
from django.http import HttpResponse
from datetime import datetime
import json

def hello_world(request):
	#llamo a hello world
	return HttpResponse('Esta es la hora local: {now}'.format(
		now=datetime.now().strftime("%b %dth %Y - %H:%M hrs")
		))

def sorted_numers(request):
	"""Ordena numeros y los combierte a .json"""
	numeros = [int(i) for i in request.GET["numeros"].split(",")]
	numeros_ordenados = sorted(numeros)
	data = {
	"status": "ok",
	"numeros": numeros_ordenados,
	"mensaje": "hola putita"
	}
	return HttpResponse(
		json.dumps(data, indent=4),
	 	content_type="application/json")

def hi(request, name, age):
	if age < 12:
		mensaje = "Perdon {} no puedes entrar a esta pagina.".format(name)
	else:
		mensaje = "Hola {}, bienvenido a tu nueva pagina web.".format(name)
	return HttpResponse(mensaje)

def saludo(request,nombre,edad):
	if edad < 18:
		mensaje = "Hola {} no tienes la edad suficiente para ver p*rn* xd".format(nombre)
	else:
		mensaje = "Hola {} que tipo de porno quieres ver?".format(nombre)
	return HttpResponse(mensaje)
