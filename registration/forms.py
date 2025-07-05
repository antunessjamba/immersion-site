from django import forms
from .models import Registration

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'municipality', 'phone', 'gender']

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Nome"
        self.fields['municipality'].label = "Município"
        self.fields['phone'].label = "Telefone"
        self.fields['gender'].label = "Gênero"