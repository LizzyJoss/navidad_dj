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

def historia(request):
    return render(request, 'historia.html')

def cuentos(request):
    return render(request, 'cuentos.html')

def villancicos(request):
    return render(request, 'villancicos.html')

def cocina(request):
    return render(request, 'cocina.html')

def actividades(request):
    return render(request, 'actividades.html')

def carta_santa(request):
    return render(request, 'cartaSanta.html')

def regalos(request):
    return render(request, 'regalos.html')

def decoracion(request):
    return render(request, 'decoracion.html')

def juegos(request):
    return render(request, 'juegos.html')

def bajarimagenes(request):
    return render(request, 'bajarimagenes.html')

def navidadenelmundo(request):
    return render(request, 'navidadenelmundo.html')
