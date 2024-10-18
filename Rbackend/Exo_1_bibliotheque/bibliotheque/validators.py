from django.core.exceptions import ValidationError
import re

class CustomPasswordValidator:
    def __init__(self, require_special_characters=True, require_uppercase=True, require_lowercase=True, require_numbers=True):
        self.require_special_characters = require_special_characters
        self.require_uppercase = require_uppercase
        self.require_lowercase = require_lowercase
        self.require_numbers = require_numbers

    def validate(self, password, user=None):
        if self.require_special_characters and not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError("The password must contain at least one special character.")
        if self.require_uppercase and not re.search(r'[A-Z]', password):
            raise ValidationError("The password must contain at least one uppercase letter.")
        if self.require_lowercase and not re.search(r'[a-z]', password):
            raise ValidationError("The password must contain at least one lowercase letter.")
        if self.require_numbers and not re.search(r'\d', password):
            raise ValidationError("The password must contain at least one digit.")

    def get_help_text(self):
        return "Your password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character."
