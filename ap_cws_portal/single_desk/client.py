# single_desk/client.py
import requests
from django.conf import settings
from requests.exceptions import RequestException
from django.core.exceptions import ImproperlyConfigured

class SingleDeskClient:
    @classmethod
    def _get_config(cls):
        try:
            config = getattr(settings, 'SINGLE_DESK_CONFIG')
            if not all(key in config for key in ('API_URL', 'API_KEY')):
                raise ImproperlyConfigured("SINGLE_DESK_CONFIG missing required keys")
            return config
        except AttributeError:
            raise ImproperlyConfigured("SINGLE_DESK_CONFIG not defined in settings")

    @classmethod
    def get_business_details(cls, registration_number):
        config = cls._get_config()
        try:
            response = requests.get(
                f"{config['API_URL']}/businesses/{registration_number}",
                headers={
                    "Authorization": f"Bearer {config['API_KEY']}",
                    "Accept": "application/json"
                },
                timeout=config.get('TIMEOUT', 10)
            )
            response.raise_for_status()
            return response.json()
        except RequestException as e:
            raise Exception(f"Single Desk API error: {str(e)}")