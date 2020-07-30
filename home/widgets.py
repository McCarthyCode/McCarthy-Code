from django import forms

class CustomSelect(forms.widgets.Select):
    template_name = 'widgets/custom_select.html'
