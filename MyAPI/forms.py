from django import forms
from django.forms import ModelForm, TextInput, Textarea, Select, HiddenInput, Form, ModelChoiceField, CharField
# from django.forms import *
from MyAPI.models import Chapter, Classification, Position
"""
Creamos un archivo form para utilizar ModelForm y crear de forma automática los formularios con django
"""

class ApprovalForm(forms.Form):
    descripcion = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Ingrese descripcion'}))
    material = forms.ChoiceField(choices=[('Plastico', 'Plastico'),('Vidrio', 'Vidrio'),('Ceramica', 'Ceramica')])

class ChapterForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['chapter'].widget.attrs['autofocus'] = True

    class Meta:
        model = Chapter
        fields = '__all__'
        widgets = {
            'chapter': TextInput(
                attrs={
                    'placeholder': 'Ingrese un capítulo'
                }
            ),
            'description': TextInput(
                attrs={
                    'placeholder': 'Ingrese una descripción'
                }
            ),
        }
        exclude = ['user_updated', 'user_creation']

    def save(self, commit=True):
        data = {}
        form = super() # Recuperar el objeto formulario
        try:
            if form.is_valid():
                form.save()
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

class ClassificationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'

        # # forma 1
        # self.fields['classify'].widget.attrs['autofocus'] = True
        # # self.fields['classify'].widget.attrs['class'] = 'form-control select2'
        # self.fields['classify'].widget.attrs['style'] = 'width:100%'
        #
        # # forma
        # self.fields['classify'].widget.attrs = {
        #     'autofocus': True,
        #     'class': 'form-contro select2',
        #     'style': 'width:100%'
        # }

        # prueba
        # self.fields['classify'].widget.attrs['is_hidden'] = False

        self.fields['description'].widget.attrs['autofocus'] = True

    class Meta:
        model = Classification
        fields = '__all__'
        widgets = {
            'description': TextInput(
                attrs={
                    'placeholder': 'Ingrese una descripción'
                }
            ),
            'material': Select(
                attrs={
                    'placeholder': 'Seleccione un material'
                }
            ),
            'classify': TextInput(
                attrs={
                    'placeholder': 'Clasificación arancelaria sugerida'
                }
            ),

        }
        # exclude = ['user_updated', 'user_creation']

    def save(self, commit=True):
        data = {}
        form = super() # Recuperar el objeto formulario
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
                data['error'] = str(e)
        return data

    def clean(self):
        cleaned = super().clean()
        if len(cleaned['description']) <=10:
            raise forms.ValidationError('Validación xx')
            # self.add_error('description', 'Le faltan caracteres')
        return cleaned

class TestForm(Form):
    chapters = ModelChoiceField(queryset=Chapter.objects.all(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

    search = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese descripcion del capítulo'
    }))

    classify_search = CharField(widget=TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingrese descripcion de la mercadería'
    }))

class PositionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['position'].widget.attrs['autofocus'] = True

    class Meta:
        model = Position
        fields = '__all__'
        widgets = {
            'position': TextInput(
                attrs={
                    'placeholder': 'Ingrese una posición arancelaria'
                }
            ),
            'description': TextInput(
                attrs={
                    'placeholder': 'Ingrese una descripción'
                }
            ),
        }
        exclude = ['user_updated', 'user_creation']

    def save(self, commit=True):
        data = {}
        form = super() # Recuperar el objeto formulario
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
                data['error'] = str(e)
        return data