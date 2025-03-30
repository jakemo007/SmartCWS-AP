from functools import wraps
from django.utils import timezone
from django.apps import apps
from django.conf import settings

def log_api_action(action_name=None):
    """
    Safe decorator that handles app registry not ready state
    """
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(request, *args, **kwargs):
            # Skip if logging disabled
            if getattr(settings, 'DISABLE_AUDIT_LOGGING', False):
                return view_func(request, *args, **kwargs)
            
            response = view_func(request, *args, **kwargs)
            
            try:
                # Lazy load model to avoid AppRegistryNotReady
                AuditLog = apps.get_model('audit.AuditLog')
                
                action = action_name or f"{view_func.__name__}_{request.method.lower()}"
                
                AuditLog.objects.create(
                    user=request.user if request.user.is_authenticated else None,
                    action=action,
                    path=request.path,
                    status_code=response.status_code,
                    request_data=getattr(request, 'data', None),
                    ip_address=get_client_ip(request),
                    response_data=getattr(response, 'data', None)
                )
            except Exception as e:
                if settings.DEBUG:
                    import logging
                    logger = logging.getLogger(__name__)
                    logger.warning(f"Audit log failed: {str(e)}")
            
            return response
        return wrapped_view
    return decorator

def get_client_ip(request):
    """Safe IP address extraction"""
    xff = request.META.get('HTTP_X_FORWARDED_FOR')
    return xff.split(',')[0].strip() if xff else request.META.get('REMOTE_ADDR', '')