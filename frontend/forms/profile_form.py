from django.core.exceptions import ValidationError

def validate_phone_number(value):
    """Validator for phone numbers"""
    if len(value) < 10:
        raise ValidationError("Phone number must be at least 10 digits.")
    
def validate_price(value):
    """Validator for price to ensure it is positive"""
    if value <= 0:
        raise ValidationError("Price must be greater than zero.")
