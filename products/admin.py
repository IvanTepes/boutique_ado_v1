from django.contrib import admin
from .models import Product, Category, Brand, Memory, KeyFeatures

from django.db.models.functions import Lower

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class MemoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class KeyFeaturesAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'feature_1',
        'feature_2',
        'feature_3',
        'feature_4',
        'feature_5',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, CategoryAdmin)
admin.site.register(Memory, CategoryAdmin)
admin.site.register(KeyFeatures, CategoryAdmin)

