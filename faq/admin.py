from django.contrib import admin
from .models import FAQ
from modeltranslation.admin import TabbedTranslationAdmin

@admin.register(FAQ)
class FaqAdmin(TabbedTranslationAdmin):
    list_display = ('question', 'answer')