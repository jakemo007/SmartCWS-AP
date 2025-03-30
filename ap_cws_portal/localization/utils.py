from django.utils.translation import gettext as _

def get_localized_error_messages():
    return {
        'required': _('This field is required'),
        'invalid': _('Enter a valid value'),
        # Add more translations as needed
    }