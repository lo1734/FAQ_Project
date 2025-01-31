from django.test import TestCase
from .models import FAQ

class FAQModelTest(TestCase):
    def test_faq_creation(self):
        faq = FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")
        self.assertEqual(faq.question, "What is Django?")
        self.assertEqual(faq.answer, "Django is a web framework.")
from django.test import TestCase

# Create your tests here.
