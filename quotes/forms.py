from django import forms
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

from .models import Contact, QuoteRequest
from home.widgets import CustomSelect
from mwd.settings import PHONE_REGEX

class QuoteRequestForm(forms.ModelForm):
    title = forms.TypedChoiceField(
        coerce=int,
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
    surname_first = forms.BooleanField(
        required=False,
        label='Surname Is First',
        widget=forms.CheckboxInput(),
    )
    phone = forms.CharField(
        label='',
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone',
        }),
        validators=[RegexValidator(PHONE_REGEX, 'Enter a valid U.S. phone number.')],
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
        required=False,
        max_length=500,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Summary of Site Contents (optional)\nBe as detailed or as general as you like.',
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
            # 'phone' not in cleaned_data.
            # Error handled in RegexValidator.
            return cleaned_data

        # Retrieve contact first by email, then by phone number.
        # If successful, update. Otherwise, create new.
        kwargs = {
            'title': cleaned_data['title'],
            'first_name': cleaned_data['first_name'],
            'last_name': cleaned_data['last_name'],
            'surname_first': cleaned_data['surname_first'],
        }

        try:
            contact = Contact.objects.get(email=cleaned_data['email'])

            kwargs['phone'] = cleaned_data['phone']
            for key, value in kwargs.items():
                setattr(contact, key, value)

            contact.save()
        except Contact.DoesNotExist:
            try:
                contact = Contact.objects.get(phone=cleaned_data['phone'])

                kwargs['email'] = cleaned_data['email']
                for key, value in kwargs.items():
                    setattr(contact, key, value)

                contact.save()
            except Contact.DoesNotExist:
                contact = Contact.objects.create(
                    phone=cleaned_data['phone'],
                    email=cleaned_data['email'],
                    **kwargs
                )

        cleaned_data['contact'] = contact

        return cleaned_data

    class Meta:
        model = QuoteRequest
        fields = [
            'title', 'first_name', 'last_name', 'surname_first',
            'phone', 'email', 'description',
        ]
