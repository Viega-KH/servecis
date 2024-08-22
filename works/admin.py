from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from modeltranslation.translator import TranslationOptions, translator
from .models import Work, WorkCategore


class WorkTranslationOptions(TranslationOptions):
    fields = ('title', 'client') 


translator.register(Work, WorkTranslationOptions)

class WorkCategoreTranslationOptions(TranslationOptions):
    fields = ('title',)  


translator.register(WorkCategore, WorkCategoreTranslationOptions)


@admin.register(Work)
class WorkAdmin(TranslationAdmin):
    fieldsets = (
        ('General Information', {
            'fields': ('workcategores', 'image', 'technology', 'link', 'size',),
            'classes': ('collapse',),
        }),
        ('Uzbek Content', {
            'fields': ('title_uz', 'client_uz'),
            'classes': ('collapse',),
        }),
        ('English Content', {
            'fields': ('title_en', 'client_en'),
            'classes': ('collapse',),
        }),
        ('Russian Content', {
            'fields': ('title_ru', 'client_ru'),
            'classes': ('collapse',),
        }),
    )
    
    list_display = ('title_uz', 'title_en', 'title_ru',)
    search_fields = ('title_uz', 'title_en', 'title_ru', 'client_uz', 'client_en', 'client_ru')


@admin.register(WorkCategore)
class WorkCategoreAdmin(TranslationAdmin):
    pass