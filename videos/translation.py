from modeltranslation.translator import translator, TranslationOptions
from .models import Video


class VideoTranslationOptions(TranslationOptions):
    fields = ('title', )

translator.register(Video, VideoTranslationOptions)