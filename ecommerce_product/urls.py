from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.home, name='home'),
    path('render_category', views.render_category, name='render_category'),
    path('products/', views.list_products.as_view(), name='list_product'),
    path('products/sale', views.sale_products.as_view(), name='sale_product'),
    path('products/<category_name>', views.category_products.as_view(), name='category_product'),
    path('products/search/', views.search_products.as_view(), name='search_product'),
    path('detail/<id_product>/<slug_product>', views.detail_products, name='detail_product'),
]
