from django.contrib import admin

from webapp.models import Product, Review


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_display_links = ['name']
    list_filter = ['name', 'category']
    search_fields = ['category']
    fields = ['name', 'category', 'description', 'image']


admin.site.register(Product, ProductAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'rating']
    list_display_links = ['product']
    list_filter = ['product', 'rating']
    search_fields = ['product', 'moderated']
    fields = ['author', 'product', 'text', 'moderated', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Review, ReviewAdmin)
