from django import forms
from .models import ContactMessageModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessageModel
        exclude = ['created_at']