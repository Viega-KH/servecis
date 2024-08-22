from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class ServecsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'servecs'
    verbose_name = _("Service")
    verbose_name_plural = _("Service")
