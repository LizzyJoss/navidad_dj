from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def quienes(request):
    return render(request, 'quienesSomos.html')