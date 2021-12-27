from django.contrib import admin
from .models import StoreProducts, CategoryProducts


@admin.register(CategoryProducts)
class CategoryProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active',)
    list_editable = ('is_active',)
    list_filter = ('title', 'is_active')
    search_fields = ('title',)


@admin.register(StoreProducts)
class StoreProductsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'show_dollars_in_panel', 'label', 'is_active', 'available_count')
    list_editable = ('is_active', 'label',)
    list_filter = ('title', 'is_active', 'category', 'price', 'label',)
    search_fields = ('title', 'category', 'label',)

    @admin.display(description='price')
    def show_dollars_in_panel(self, obj):
        return f'{obj.price} $'
