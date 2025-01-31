from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    def get_translated_question(self, lang_code):
        """Returns the translated question based on the language code."""
        field_name = f'question_{lang_code}'
        return getattr(self, field_name, self.question)

    def __str__(self):
        return self.question
