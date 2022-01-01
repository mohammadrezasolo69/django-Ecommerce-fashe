from django.shortcuts import render
from .models import AboutUs


def about(request):
    item = AboutUs.objects.last()
    return render(request, 'about/about.html', context={'item': item})
