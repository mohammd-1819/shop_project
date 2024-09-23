from django import forms
from .models import ContactUs


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={
                'id': "name",
                'class': 'form-control',
                'placeholder': 'your name'
            }),

            'email': forms.EmailInput(attrs={
                'id': "email",
                'class': 'form-control',
                'placeholder': 'your email'
            }),

            'subject': forms.TextInput(attrs={
                'id': "subject",
                'class': 'form-control',
                'placeholder': 'your subject'
            }),

            'text': forms.Textarea(attrs={
                'id': "message",
                'class': 'form-control w-100',
                'placeholder': 'your message'
            })
        }

