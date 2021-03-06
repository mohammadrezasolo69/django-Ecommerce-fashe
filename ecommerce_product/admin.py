from django.contrib import admin
from .models import StoreProducts, CategoryProducts, SizeProducts, Slider


@admin.register(SizeProducts)
class SizeAndColor(admin.ModelAdmin):
    list_display = ('size_name',)


@admin.register(CategoryProducts)
class CategoryProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active',)
    list_editable = ('is_active',)
    list_filter = ('title', 'is_active')
    search_fields = ('title',)


@admin.register(StoreProducts)
class StoreProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'show_discount_and_price', 'label', 'is_active', 'available_count')
    list_editable = ('is_active', 'label',)
    list_filter = ('title', 'category', 'is_active', 'price', 'label',)
    search_fields = ('title', 'label', 'category',)

    @admin.display(description='price')
    def show_discount_and_price(self, obj):
        return f'{obj.price} $'


@admin.register(Slider)
class Slider(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)
