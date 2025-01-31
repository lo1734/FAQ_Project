from django.db import models
from ckeditor.fields import RichTextField
from modeltranslation.translator import register, TranslationOptions

# class FAQ(models.Model):
#     question = models.TextField()
#     answer = RichTextField()
#
#     def get_translated_question(self, lang_code):
#         """Retrieve the translated question based on the language code."""
#         field_name = f'question_{lang_code}'
#         return getattr(self, field_name, self.question)
#
#     def __str__(self):
#         return self.question
#
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    def translate_question(self):
        translator = Translator()
        try:
            translations = translator.translate(self.question, dest='es')  # Spanish, for example
            self.question_es = translations.text  # Saving translation to the 'question_es' field
        except Exception as e:
            print(f"Translation failed: {e}")
