# Ce fichier sert à ajouter des conditions de robustesse sur les mdp entrés par les Users
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class PasswordValidator:
    def validate(self, password, user=None):
        if not re.findall(r'\d', password):
            raise ValidationError(
                _("Le mot de passe doit contenir au moins un chiffre."),
                code='password_no_number',
            )
        if not re.findall(r'[A-Z]', password):
            raise ValidationError(
                _("Le mot de passe doit contenir au moins une lettre majuscule."),
                code='password_no_upper',
            )
        if not re.findall(r'[a-z]', password):
            raise ValidationError(
                _("Le mot de passe doit contenir au moins une lettre minuscule."),
                code='password_no_lower',
            )
        if not re.findall(r'[^a-zA-Z0-9]', password):
            raise ValidationError(
                _("Le mot de passe doit contenir au moins un caractère spécial."),
                code='password_no_special',
            )

    def get_help_text(self):
        return _(
            "Votre mot de passe doit contenir au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial."
        )
