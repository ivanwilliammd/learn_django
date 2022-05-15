from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

def clean_email(value):
    email = value
    if "edu" in email:
        raise ValidationError("Use another email address not .edu")


CATEGORIES = ['Indonesian', 'Genshin', 'Japanese', 'Korean', 'Thai', 'Chinese']

def validate_category(value):
    if not value.lower() in (map(lambda x: x.lower(), CATEGORIES)):
        raise ValidationError(f"{value} not a valid category. Please select from {CATEGORIES}")