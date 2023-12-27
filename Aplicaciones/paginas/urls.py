from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('quienes/', views.quienes),
    path('contacto/', views.contacto),
    path('videos/', views.videos),
    path('cartaasanta/', views.carta_santa),
]
