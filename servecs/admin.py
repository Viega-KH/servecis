from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from modeltranslation.translator import TranslationOptions, translator
from .models import Service


class ServiceTranslationOptions(TranslationOptions):
    fields = ('name', 'description') 


translator.register(Service, ServiceTranslationOptions)



@admin.register(Service)
class ServiceAdmin(TranslationAdmin):
    fieldsets = (
        ('General Information', {
            'fields': ('active',),
            'classes': ('collapse',),
        }),
        ('Uzbek Content', {
            'fields': ('name_uz', 'description_uz'),
            'classes': ('collapse',),
        }),
        ('English Content', {
            'fields': ('name_en', 'description_en'),
            'classes': ('collapse',),
        }),
        ('Russian Content', {
            'fields': ('name_ru', 'description_ru'),
            'classes': ('collapse',),
        }),
    )
    
    list_display = ('name_en', 'name_ru', 'name_uz', 'active',)
    search_fields = ('name_uz', 'name_en', 'name_ru', 'description_uz', 'description_en', 'description_ru')

