from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def lei(request):
    return render(request, 'home/leiaprendiz.html')

def parceiros(request):
    return render(request, 'home/parceiros.html')

def sobre(request):
    return render(request, 'home/sobrenos.html')

def dicas(request):
    return render(request, 'home/dicas.html')

def op(request):
    return render(request, 'home/op.html')

def gerador(request):
    return render(request, 'home/gerador.html')












