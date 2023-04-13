from django import forms
from django.forms import ModelForm, TextInput, Textarea, Select, HiddenInput, Form, ModelChoiceField, CharField, \
    PasswordInput
# from django.forms import *
from user.models import User

class UserForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['first_name'].widget.attrs['autofocus'] = True

    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'username', 'password', 'image'
        widgets = {
            'first_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese nombre'
                }
            ),
            'last_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese apellido'
                }
            ),
            'email': TextInput(
                attrs={
                    'placeholder': 'Ingrese correo electrónico'
                }
            ),
            'user_name': TextInput(
                attrs={
                    'placeholder': 'Ingrese usuario'
                }
            ),
            'password': PasswordInput(render_value=True,
                attrs={
                    'placeholder': 'Ingrese contraseña'
                }
            ),
        }
        exclude = ['groups', 'user_permissions', 'last_login', 'date_joined']

    def save(self, commit=True):
        data = {}
        form = super() # Recuperar el objeto formulario
        try:
            if form.is_valid():
                pwd = self.cleaned_data['password']
                u = form.save(commit=False) # commit permite hacer una pausa a la creación del objeto
                if u.pk is None:
                    u.set_password(pwd)
                else:
                    user = User.objects.get(pk=u.pk)
                    if user.password != pwd:
                        u.set_password(pwd)
                u.save()
            else:
                data['error'] = form.errors
        except Exception as e:
                data['error'] = str(e)
        return data

    # def clean(self):
    #     cleaned = super().clean()
    #     if len(cleaned['description']) <=10:
    #         raise forms.ValidationError('Validación xx')
    #         # self.add_error('description', 'Le faltan caracteres')
    #     return cleaned