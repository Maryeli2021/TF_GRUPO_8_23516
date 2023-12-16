from django.shortcuts import render

# Create your views here.
def home (request):
    return render (request,"core/home.html")
def destinos (request):
    return render (request,"core/destinos.html")
def buenos_aires (request):
    return render (request,"core/destinos/buenos_aires.html")
def centro (request):
    return render (request,"core/destinos/centro.html")
def noreste (request):
    return render (request,"core/destinos/noreste.html")
def noroeste (request):
    return render (request,"core/destinos/noroeste.html")
def patagonia (request):
    return render (request,"core/destinos/patagonia.html")
def imperdibles (request):
    return render (request,"core/imperdibles.html")
def tips (request):
    return render (request,"core/tips.html")
def contacto (request):
    return render (request,"core/contacto.html")
def consulta_clima (request):
    return render (request,"core/destinos/consulta_clima.html")
