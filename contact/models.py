from django.db import models
from django.utils.translation import gettext_lazy as _

class Contact(models.Model):
    location = models.CharField(max_length=200, null=True, verbose_name=_("Location"))
    email = models.EmailField(max_length=200, null=True, verbose_name=_("Email"))
    telegram = models.URLField(max_length=200, null=True, verbose_name=_("Telegram"))
    twitter = models.URLField(max_length=200, null=True, verbose_name=_("Twitter"))
    instagram = models.URLField(max_length=200, null=True, verbose_name=_("Instagram"))
    facebook = models.URLField(max_length=200, null=True, verbose_name=_("Facebook"))
    call = models.CharField(max_length=15, null=True, verbose_name=_("Call"))

    class Meta:
        verbose_name = _("Link")
        verbose_name_plural = _("Link")

class Message(models.Model):
    company = models.CharField(max_length=100, verbose_name=_("Company"))
    full_name = models.CharField(max_length=100, verbose_name=_("Full Name"))
    type_project = models.CharField(max_length=100, verbose_name=_("Type of Project"))
    phone = models.CharField(max_length=13, verbose_name=_("Phone"))
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name=_("Date"))
    changes = models.TextField(verbose_name=_("Message"))

    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Message")

    def __str__(self):
        return self.company
