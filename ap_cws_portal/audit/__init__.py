# audit/__init__.py
from .decorators import log_api_action

__all__ = ['log_api_action']

default_app_config = 'audit.apps.AuditConfig'