from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from .models import Contact, QuoteRequest
from home.widgets import CustomSelect
from mwd.settings import PHONE_REGEX

class QuoteRequestForm(forms.ModelForm):
    title = forms.MultipleChoiceField(
        label='',
        choices=Contact.title_choices,
        widget=CustomSelect(
            attrs={
                'class': 'form-control',
                'data-label': 'Title',
            },
        ),
    )
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
    family_first = forms.BooleanField(
        required=False,
        label='Family Name Is First',
        widget=forms.CheckboxInput(),
    )
    phone = forms.CharField(
        label='',
        max_length=20,
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

        contact = Contact.objects.create(
            first_name=cleaned_data['first_name'],
            last_name=cleaned_data['last_name'],
            email=cleaned_data['email'],
            phone=cleaned_data['phone'],
        )

        cleaned_data['contact']

        del cleaned_data['title'], cleaned_data['first_name'], cleaned_data['last_name'], cleaned_data['email'], cleaned_data['phone']

        return cleaned_data

    class Meta:
        model = QuoteRequest
        fields = [
            'title', 'first_name', 'last_name', 'family_first',
            'email', 'phone', 'description',
        ]
