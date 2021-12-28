from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.home, name='home'),
    path('list_products/', views.list_products.as_view(), name='list_product'),
    path('category_products/', views.category_products, name='category_product'),
    path('detail/<id_product>/<slug_product>', views.detail_products, name='detail_product'),
]
