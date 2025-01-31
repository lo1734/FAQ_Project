from django.core.cache import cache
from rest_framework.response import Response


class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get_queryset(self):
        lang_code = self.request.query_params.get('lang', 'en')
        cache_key = f"faqs_{lang_code}"

        # Try fetching from cache
        faqs = cache.get(cache_key)
        if not faqs:
            faqs = FAQ.objects.all()  # Adjust this for translation fetching
            cache.set(cache_key, faqs, timeout=60 * 15)  # Cache for 15 minutes
        return faqs
