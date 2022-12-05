from django import forms
from .models import Contact, Sharing


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class SharingForm(forms.ModelForm):
    class Meta:
        model = Sharing
        fields = '__all__'
