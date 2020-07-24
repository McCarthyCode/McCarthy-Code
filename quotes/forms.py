from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from .models import QuoteRequest
from mwd.settings import PHONE_REGEX

class QuoteRequestForm(forms.ModelForm):
    first_name = forms.CharField(
        label='',
        max_length=35,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name',
        }),
    )
    last_name = forms.CharField(
        label='',
        max_length=70,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name',
        }),
    )
    phone = forms.CharField(
        label='',
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone',
        }),
        validators=[RegexValidator(PHONE_REGEX, 'Enter a valid phone number.')],
    )
    email = forms.EmailField(
        label='',
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email',
        }),
    )
    description = forms.CharField(
        label='',
        max_length=500,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Summary of Site Contents (please be detailed)\nE.g. an attractive home page, an about page, a quote request form, and a portfolio with private submission form and management page.',
            'rows': 6,
        }),
    )

    def clean(self):
        super().clean()
        cleaned_data = self.cleaned_data

        try:
            cleaned_data['phone'] = PHONE_REGEX.sub(
                r'\2\3\4', cleaned_data['phone']
            )
        except KeyError:
            # phone not in cleaned_data
            # error handled in field verification
            pass

        return cleaned_data

    class Meta:
        model = QuoteRequest
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'description',
        ]
