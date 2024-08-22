from django.db import models
from django.utils.translation import gettext_lazy as _

class WorkCategore(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title
    
class Work(models.Model):
    STATUS_CHOICES = (
        ('big', _("Big Size")),
        ('small', _("Small Size")),
    )
    size = models.CharField(max_length=20, choices=STATUS_CHOICES, default='small', verbose_name=_("Size"))
    workcategores = models.ForeignKey(WorkCategore, on_delete=models.CASCADE, verbose_name=_("Category"))
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    client = models.CharField(max_length=200, verbose_name=_("Client"))
    technology = models.CharField(max_length=200, verbose_name=_("Technology"))
    image = models.ImageField(upload_to='works/%Y/%m/%d/', verbose_name=_("Image"))
    link = models.URLField(verbose_name=_("Link"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name = _("Work")
        verbose_name_plural = _("Works")

    def __str__(self):
        return self.title
