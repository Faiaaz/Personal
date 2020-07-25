from django import forms
from .models import PersonInfo


class NewUserForm(forms.ModelForm):
    class Meta:
        model = PersonInfo
        fields = '__all__'
