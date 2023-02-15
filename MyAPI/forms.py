from django import forms

class ApprovalForm(forms.Form):
    descripcion = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Ingrese descripcion'}))
    material = forms.ChoiceField(choices=[('Plastico', 'Plastico'),('Vidrio', 'Vidrio'),('Ceramica', 'Ceramica')])
