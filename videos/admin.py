from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from .models import Video

@admin.register(Video)
class VideoAdmin(TabbedTranslationAdmin):
    list_display = ['title']

