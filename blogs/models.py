from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Category")

    def __str__(self):
        return self.name


class News(models.Model):
    STATUS_CHOICES = (
        ('draft', _('Draft')),
        ('published', _('Published')),
    )

    title = models.CharField(max_length=200, verbose_name=_('Title'))
    body = RichTextUploadingField(verbose_name=_('Body'))
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name=_('Status'))
    categories = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='news_posts', verbose_name=_('Category'))
    image = models.ImageField(upload_to='news/%Y/%m/%d/', verbose_name=_('Image'))
    publish = models.DateTimeField(default=timezone.now, verbose_name=_('Publish Date'))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_('Created'))
    updated = models.DateTimeField(auto_now=True, verbose_name=_('Updated'))

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blog")

    def __str__(self):
        return self.title

