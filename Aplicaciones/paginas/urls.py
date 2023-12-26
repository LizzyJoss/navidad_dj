from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('quienes/', views.quienes),
    path('contacto/', views.contacto)
]
