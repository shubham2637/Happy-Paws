from django import forms
from .models import dog
class dogs_view(forms.ModelForm):
    class Meta:
        model = dog
        fields ="__all__"
