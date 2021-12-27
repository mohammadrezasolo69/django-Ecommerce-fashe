from django.shortcuts import render
from .models import StoreProducts


def home(request):
    return render(request, 'product/home.html')
