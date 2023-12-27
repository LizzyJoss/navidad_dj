from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def quienes(request):
    return render(request, 'quienesSomos.html')

def contacto(request):
    return render(request, 'contacto.html')

def videos(request):
    return render(request, 'videos.html')

def carta_santa(request):
    return render(request, 'cartaSanta.html')