from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import ProductModel, ProductTagModel, ProductColorModel, ProductSizeModel, CategoryModel, BrandModel
from .forms import ColorForms


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'real_price', 'price', 'discount']
    list_display_links = ['id', 'title', 'real_price', 'price', 'discount']
    list_filter = ['created_at']
    search_fields = ['title']
    readonly_fields = ['real_price']


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    list_filter = ['created_at']
    search_fields = ['name']


@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


@admin.register(ProductSizeModel)
class ProductSizeModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


@admin.register(ProductColorModel)
class ProductColorModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_code', 'code']
    list_display_links = ['id', 'code']
    search_fields = ['code']
    form = ColorForms

    def get_code(self, obj):
        text = '&nbsp' * 10
        return mark_safe(f'<p style="background-color: {obj.code}; width:100px;">{text}</p>')



