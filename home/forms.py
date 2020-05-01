from django import forms

from .models import Site

class SiteForm(forms.ModelForm):
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
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )

    def clean(self):
        super().clean()
        return self.cleaned_data

    class Meta:
        model = Site
        fields = ['name', 'url', 'description']
