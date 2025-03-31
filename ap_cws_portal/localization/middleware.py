from django.utils import translation

class LocalizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language = request.META.get('HTTP_ACCEPT_LANGUAGE', 'en')[:2]
        if language not in ('en', 'te'):  # English, Telugu
            language = 'en'
        translation.activate(language)
        request.LANGUAGE_CODE = language
        response = self.get_response(request)
        return response