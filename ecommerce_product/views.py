from django.shortcuts import render, get_object_or_404, Http404
from django.views.generic import ListView
from .models import StoreProducts, CategoryProducts
from .utils import my_grouper


def home(request):
    return render(request, 'product/home.html')


class list_products(ListView):
    queryset = StoreProducts.objects.filter(is_active=True)
    paginate_by = 9
    template_name = 'product/list_product.html'
    ordering = ['-id']


def detail_products(request, id_product, slug_product):
    item = get_object_or_404(StoreProducts,id=id_product,slug=slug_product,is_active=True)
    related = StoreProducts.objects.filter(category=item.category).exclude(id=id_product)
    return render(request, 'product/detail_product.html', context={'detail': item,'related':related})


class category_products(ListView):
    template_name = 'product/list_product.html'
    paginate_by = 9
    ordering = ['-id']
    queryset = StoreProducts.objects.filter(is_active=True)

    def get_queryset(self):
        cat_name = self.kwargs['category_name']
        category = CategoryProducts.objects.filter(title__iexact=cat_name).first()
        if category is None:
            return Http404()
        return StoreProducts.objects.filter(category__title__iexact=cat_name, is_active=True)


def render_category(request):
    category = CategoryProducts.objects.filter(is_active=True)
    return render(request, 'product/render_category.html', context={'category': category})
