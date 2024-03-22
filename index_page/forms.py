from django import forms
from .models import *


class ContactForm(forms.Form):
    name = forms.CharField(max_length=64, min_length=2, widget=forms.TextInput(
        attrs={
            "placeholder": "Ім'я",
            "class": "form-control",
            }
        )
    )
    sender = forms.EmailField(max_length=128,  min_length=7, widget=forms.EmailInput(
        attrs={
            "placeholder": "Email",
            "class": "form-control",
            }
        )
    )
    message = forms.CharField(max_length=1024, min_length=10, widget=forms.Textarea(
        attrs={
            "placeholder": "Повідомлення",
            "class": "form-control",
            "rows": 2,
            }
        )
    )
    cc_myself = forms.CharField(required=False)


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = ['mail',]
        widgets = {
            'mail': forms.EmailInput(attrs={
                "placeholder": "test@email.com",
                "class": "form-control display-7",
                }
            )
        }

