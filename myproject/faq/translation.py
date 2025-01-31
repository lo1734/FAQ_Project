from modeltranslation.translator import translator, TranslationOptions
from .models import FAQ

class FAQTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')  # Add the fields that should be translatable

translator.register(FAQ, FAQTranslationOptions)
