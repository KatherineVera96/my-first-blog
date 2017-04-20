from django.shortcuts import render
from django.http import HttpResponse
from .utilidades import conversores, ecuaciones, funciones
from .utilidades.integralesfin import *
from .utilidades.retangulos import *
from .utilidades.simpson import *
from json import JSONEncoder
from sympy import diff
import pdb

# Create your views here.

def index (request):
	context = {}
	return render(request, 'logictree/index.html', context)

def bases(request):
	context = {}
	return render(request, 'logictree/bases.html', context)

def ieee (request):
	context = {}
	return render(request, 'logictree/ieee.html', context)

def evaluador (request):
	context = {}
	return render(request, 'logictree/evaluador.html', context)

def graficador (request):
	context = {}
	return render(request, 'logictree/graficador.html', context)

def derivador (request):
	context = {}
	return render(request, 'logictree/derivador.html', context)

def biseccion (request):
	context = {}
	return render(request, 'logictree/biseccion.html', context)

def reglafalsa (request):
	context = {}
	return render(request, 'logictree/reglafalsa.html', context)

def newtonraphson (request):
	context = {}
	return render(request, 'logictree/newtonraphson.html', context)

def secante (request):
	context = {}
	return render(request, 'logictree/secante.html', context)

def raices (request):
	context = {}
	return render(request, 'logictree/raices.html', context)

def rectangulosview (request):
	if (request.method=='POST'):
		 funcion=request.POST['funcion']
		 a=request.POST['intervaloa']
		 b=request.POST['intervalob']
		 particiones=request.POST['npart']
		 mostrar=Rectangulos()
		 enviarIz=mostrar.recIzquierda(funcion,float(a),float(b),int(particiones))
		 enviarDe=mostrar.recDerecha(funcion,float(a),float(b),int(particiones))
		 enviarMe=mostrar.recMedios(funcion,float(a),float(b),int(particiones))
		 return render(request,'logictree/rectangulos.html',{"enviarIz":enviarIz,"enviarDe":enviarDe,"enviarMe":enviarMe} )
	else:
		enviarIz=""
		enviarDe=""
		enviarMe=""
	return render(request, 'logictree/rectangulos.html', {"enviarIz":enviarIz,"enviarDe":enviarDe,"enviarMe":enviarMe})

def trapecioview (request):
	if(request.method=='POST'):
		funcion=request.POST['funcion']
		a=request.POST['intervaloa']
		b=request.POST['intervalob']
		particiones=request.POST['npart']
		mostrar=Trap()
		print(funcion)
		print(a)
		print(b)
		print(particiones)
		enviar=mostrar.trapecios(funcion,float(a),float(b),int(particiones))
		return render(request,'logictree/trapecio.html',{"enviar":enviar})
	else:
		enviar=""
	return render(request, 'logictree/trapecio.html',{"enviar":enviar})

def simpson13view (request):
	if (request.method=='POST'):
		funcion=request.POST['funcion']
		a=request.POST['intervaloa']
		b=request.POST['intervalob']
		particiones=request.POST['npart']
		mostrar=Simp13()
		enviar=mostrar.simpin13(int(particiones),float(a),float(b),funcion)
		return render(request, 'logictree/simpson13.html', {"enviar":enviar})
	else:
		enviar=""
	return render(request, 'logictree/simpson13.html', {"enviar":enviar})

def simpson38 (request):
	context = {}
	return render(request, 'logictree/simpson38.html', context)

def montecarlo (request):
	context = {}
	return render(request, 'logictree/montecarlo.html', context)

def conocenos (request):
	context = {}
	return render(request, 'logictree/conocenos.html', context)


json = {'"nada"'}
#CALCULOOOOS
def basescalc(request):
	if request.method == 'POST':
		numero = request.POST['numero']
		base = request.POST['base']
		numeros = []
		numeros.append(base)
		if base == 'decimal':
			numeros.append(numero)
			numeros.append(conversores.decimalABinario(numero, 20))
			numeros.append(conversores.decimalAOctal(numero, 20))
			numeros.append(conversores.decimalAHexa(numero, 20))
		if base == 'binaria':
			numeros.append(conversores.binarioADecimal(numero))
			numeros.append(numero)
			numeros.append(conversores.decimalAOctal(conversores.binarioADecimal(numero), 20))
			numeros.append(conversores.decimalAHexa(conversores.binarioADecimal(numero), 20))
		if base == 'octal':
			numeros.append(conversores.octalADecimal(numero))
			numeros.append(conversores.decimalABinario(conversores.octalADecimal(numero), 20))
			numeros.append(numero)
			numeros.append(conversores.decimalAHexa(conversores.octalADecimal(numero), 20))
		if base == 'hexadecimal':
			numeros.append(conversores.hexaADecimal(numero))
			numeros.append(conversores.decimalABinario(conversores.hexaADecimal(numero), 20))
			numeros.append(conversores.decimalAOctal(conversores.hexaADecimal(numero), 20))
			numeros.append(numero)

		json = JSONEncoder().encode(numeros)

	return HttpResponse(json)

def ieeecalc (request):

	if request.method == 'POST':
		numero = request.POST['numero']
		representacion = request.POST['representacion']
		numeros = []
		numeros.append(representacion)
		if representacion == 'decimal':
			numeros.append(numero)
			numeros.append(conversores.binarioAPuntoFlotante32(conversores.decimalABinario(numero , 20)))
			numeros.append(conversores.binarioAPuntoFlotante64(conversores.decimalABinario(numero , 20)))
		if representacion == 'ieee32':
			numeros.append(conversores.binarioADecimal(conversores.puntoFlotanteABinario32(numero[0], numero[1:9], numero[9:32])))
			numeros.append(numero)
			numeros.append(conversores.binarioAPuntoFlotante64(conversores.puntoFlotanteABinario32(numero[0], numero[1:9], numero[9:32])))
		if representacion == 'ieee64':
			numeros.append(conversores.binarioADecimal(conversores.puntoFlotanteABinario64(numero[0], numero[1:12], numero[12:64])))
			numeros.append(conversores.binarioAPuntoFlotante32(conversores.puntoFlotanteABinario64(numero[0], numero[1:12], numero[12:64])))
			numeros.append(numero)

		json = JSONEncoder().encode(numeros)
	return HttpResponse(json)

def evaluadorcalc (request):
	resultado = []
	if request.method == 'POST':
		funcion = request.POST['funcion']
		x = request.POST['x']
		resultado.append(str(diff(funcion, 'x', 0).subs('x', x).evalf()))

		json = JSONEncoder().encode(resultado)

	return HttpResponse(json)

def graficadorcalc (request):
	context = {}
	return HttpResponse(json)

def derivadorcalc (request):
	resultado = []
	if request.method == 'POST':
		funcion = request.POST['funcion']
		x = request.POST['x']
		resultado.append(str(diff(funcion, 'x', 1)))
		resultado.append(str(diff(funcion, 'x', 1).subs('x', x).evalf()))
		resultado.append(str(diff(funcion, 'x', 2)))
		resultado.append(str(diff(funcion, 'x', 2).subs('x', x).evalf()))

		json = JSONEncoder().encode(resultado)

	return HttpResponse(json)

def biseccioncalc (request):
	if request.method == 'POST':
		funcion = request.POST['funcion']
		a = request.POST['a']
		b = request.POST['b']
		tolerancia = request.POST['tolerancia']
		print(funcion)
		print(a)
		print(b)
		print(tolerancia)
		resultado = ecuaciones.biseccion(str(funcion), a, b, tolerancia)

		json = JSONEncoder().encode(resultado)

	return HttpResponse(json)

def reglafalsacalc (request):
	if request.method == 'POST':
		funcion = request.POST['funcion']
		a = request.POST['a']
		b = request.POST['b']
		tolerancia = request.POST['tolerancia']
		print(funcion)
		print(a)
		print(b)
		print(tolerancia)
		resultado = ecuaciones.reglaFalsa(str(funcion), a, b, tolerancia)

		print(resultado)
		json = JSONEncoder().encode(resultado)

	return HttpResponse(json)

def newtonraphsoncalc (request):
	if request.method == 'POST':
		funcion = request.POST['funcion']
		x0 = request.POST['x0']
		error = request.POST['error']
		print(funcion)
		print(x0)
		print(error)
		resultado = ecuaciones.newtonRaphson(str(funcion), x0, error)

		print(resultado)
		json = JSONEncoder().encode(resultado)

	return HttpResponse(json)

def secantecalc (request):
	if request.method == 'POST':
		funcion = request.POST['funcion']
		a = request.POST['a']
		b = request.POST['b']
		tolerancia = request.POST['tolerancia']
		print(funcion)
		print(a)
		print(b)
		print(tolerancia)
		resultado = ecuaciones.secante(str(funcion), a, b, tolerancia)

		json = JSONEncoder().encode(resultado)
	return HttpResponse(json)

def raicescalc (request):
	if request.method == 'POST':
		funcion = request.POST['funcion']
		print(funcion)
		resultado = ecuaciones.raicesPolinomicas(str(funcion))
		json = JSONEncoder().encode(resultado)
	return HttpResponse(json)


def simpson38calc (request):
	context = {}
	return HttpResponse(json)

def montecarlocalc (request):
	context = {}
	return HttpResponse(json)
