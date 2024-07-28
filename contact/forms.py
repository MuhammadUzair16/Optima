from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control bg-light border-0 px-4', 'placeholder': 'Your Name', 'style': 'height: 55px;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control bg-light border-0 px-4', 'placeholder': 'Your Email', 'style': 'height: 55px;'}),
            'subject': forms.TextInput(attrs={'class': 'form-control bg-light border-0 px-4', 'placeholder': 'Subject', 'style': 'height: 55px;'}),
            'message': forms.Textarea(attrs={'class': 'form-control bg-light border-0 px-4 py-3', 'rows': 4, 'placeholder': 'Message'}),
        }
