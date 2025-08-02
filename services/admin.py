from django.contrib import admin
from .models import Service
from modeltranslation.admin import TabbedTranslationAdmin


@admin.register(Service)
class ServiceAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'description')
