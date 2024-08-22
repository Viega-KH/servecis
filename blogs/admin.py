from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from modeltranslation.translator import TranslationOptions, translator
from .models import News, Category


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'body') 


translator.register(News, NewsTranslationOptions)

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)  


translator.register(Category, CategoryTranslationOptions)


@admin.register(News)
class NewsAdmin(TranslationAdmin):
    fieldsets = (
        ('General Information', {
            'fields': ('status', 'categories', 'image', 'publish'),
            'classes': ('collapse',),
        }),
        ('Uzbek Content', {
            'fields': ('title_uz', 'body_uz'),
            'classes': ('collapse',),
        }),
        ('English Content', {
            'fields': ('title_en', 'body_en'),
            'classes': ('collapse',),
        }),
        ('Russian Content', {
            'fields': ('title_ru', 'body_ru'),
            'classes': ('collapse',),
        }),
    )
    
    list_display = ('title_uz', 'title_en', 'title_ru', 'status', 'publish', 'created')
    search_fields = ('title_uz', 'title_en', 'title_ru', 'body_uz', 'body_en', 'body_ru')


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    pass