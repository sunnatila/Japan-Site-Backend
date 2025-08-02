from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import Product

@admin.register(Product)
class ProductAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'description', 'price')

