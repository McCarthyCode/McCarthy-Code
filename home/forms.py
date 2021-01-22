from django import forms

from .models import Site

class BaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  # globally override the Django >=1.6 default of ':'
        super(BaseForm, self).__init__(*args, **kwargs)

class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')  # globally override the Django >=1.6 default of ':'
        super(BaseModelForm, self).__init__(*args, **kwargs)

class SiteForm(BaseModelForm):
    name = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Site Name',
        }),
    )
    url = forms.CharField(
        label='',
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'URL',
        }),
    )
    github = forms.CharField(
        label='',
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'value': 'https://github.com/McCarthyCode/',
            'placeholder': 'GitHub URL',
        }),
    )
    active = forms.BooleanField(
        initial=True,
        required=False,
        label='Website Is Active',
        widget=forms.CheckboxInput()
    )
    description = forms.CharField(
        label='',
        max_length=200,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Description',
            'rows': 5,
        }),
    )
    screenshots = forms.ImageField(
        label='Screenshots',
        required=False,
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )

    def clean(self):
        super().clean()
        return self.cleaned_data

    class Meta:
        model = Site
        fields = ['name', 'url', 'github', 'active', 'description']
