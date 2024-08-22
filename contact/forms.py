# myapp/forms.py

from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['company', 'full_name', 'type_project', 'phone', 'changes']
        widgets = {
            'changes': forms.Textarea(attrs={'rows': 4}),
        }
