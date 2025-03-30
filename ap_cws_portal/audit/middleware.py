# audit/middleware.py
from django.apps import apps
from django.conf import settings
from .decorators import get_client_ip

class AuditMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        if request.method in ('POST', 'PUT', 'PATCH', 'DELETE'):
            try:
                AuditLog = apps.get_model('audit.AuditLog')
                AuditLog.objects.create(
                    user=request.user if request.user.is_authenticated else None,
                    action=request.method,
                    path=request.path,
                    status_code=response.status_code,
                    request_data=getattr(request, 'data', None),
                    ip_address=get_client_ip(request)
                )
            except Exception as e:
                if settings.DEBUG:
                    import logging
                    logging.getLogger(__name__).warning(f"Middleware audit failed: {e}")
        
        return response