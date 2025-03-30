from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
import requests

class DPMSService:
    @classmethod
    def _get_config(cls):
        try:
            config = getattr(settings, 'DPMS_CONFIG')
            if not all(key in config for key in ('API_URL', 'API_KEY')):
                raise ImproperlyConfigured("DPMS_CONFIG missing required keys")
            return config
        except AttributeError:
            raise ImproperlyConfigured("DPMS_CONFIG not defined in settings")

    @classmethod
    def verify_plan(cls, plan_number):
        config = cls._get_config()
        try:
            response = requests.post(
                f"{config['API_URL']}/verify",
                json={"plan_number": plan_number},
                headers={"Authorization": f"Bearer {config['API_KEY']}"},
                timeout=config.get('TIMEOUT', 10)
            )
            response.raise_for_status()
            return response.json().get('is_valid', False)
        except requests.exceptions.RequestException as e:
            # Log error here
            return False