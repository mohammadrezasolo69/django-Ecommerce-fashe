from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import StoreProducts, CategoryProducts


def home(request):
    return render(request, 'product/home.html')


def category_products(request):
    category = CategoryProducts.objects.filter(is_active=True)
    return render(request, 'product/list_product.html', context={'category': category})


class list_products(ListView):
    queryset = StoreProducts.objects.filter(is_active=True)
    paginate_by = 9
    template_name = 'product/list_product.html'
    ordering = ['-id']


def detail_products(request, id_product, slug_product):
    item = get_object_or_404(StoreProducts, id=id_product, slug=slug_product, is_active=True)
    return render(request, 'product/detail_product.html', context={'detail': item})
