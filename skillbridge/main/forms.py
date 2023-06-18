from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class RegistroUsuariosForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistroUsuariosForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Nombre de Usuario'
        self.fields['password1'].label = 'Contraseña'
        self.fields['password2'].label = 'Confirmar Contraseña'
        self.fields['first_name'].label = 'Nombre'
        self.fields['last_name'].label = 'Apellido'
        self.fields['email'].label = 'Correo electrónico'
        
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'

    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()

class RegistroStaffForm(forms.Form):
    def __init__(self, *args, **kwargs):
            super(RegistroStaffForm, self).__init__(*args, **kwargs)
            self.fields['groups'].label = 'Elija un grupo para el usuario'
            self.fields['groups'].widget.attrs['class'] = 'form-select'
    groups = forms.ModelChoiceField(queryset=Group.objects.all(), empty_label=None)

class RegistroUsuarioStaffForm(RegistroUsuariosForm, RegistroStaffForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email','groups')
        labels = {
            'groups': 'Elija un grupo para el usuario'
        }