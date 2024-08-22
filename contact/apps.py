from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ContactConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact'
    verbose_name = _("contact")
    verbose_name_plural = _("contact")
