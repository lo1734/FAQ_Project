from django.contrib import admin
from .models import FAQ
from modeltranslation.admin import TranslationAdmin

@admin.register(FAQ)
class FAQAdmin(TranslationAdmin):
    list_display = ('question',)
