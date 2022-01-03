from . import views
from django.urls import path

app_name = 'cart'
urlpatterns = [
    path('detail/', views.detail_cart, name='detail_cart'),
    path('add/<product_id>', views.add_cart, name='add_cart'),
    path('remove/<product_id>', views.remove_cart, name='remove_cart'),
]
