from django.contrib import admin
from .models import Contact, Message
from django.contrib.auth.models import User, Group

class MessageAdmin(admin.ModelAdmin):
    # Faqat ko'rsatish uchun xususiyatlar
    readonly_fields = [field.name for field in Message._meta.get_fields()]
    
    # Tahrirlash imkoniyatlarini o'chirish
    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


# Contact modelini ro'yxatga olish
admin.site.register(Contact)

# Message modelini faqat ko'rsatish rejimida ro'yxatga olish
admin.site.register(Message, MessageAdmin)


# User va Group modellardan admin paneldan ro'yxatdan chiqarish
admin.site.unregister([User, Group])
