# mi_app/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'roson_tercera_pre_entrega/home.html')
