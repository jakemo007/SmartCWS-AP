# audit/apps.py
from django.apps import AppConfig

class AuditConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'audit'
    
    def ready(self):
        pass  # No signals needed