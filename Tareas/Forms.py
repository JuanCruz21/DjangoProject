from django import forms

class createnewtask(forms.Form):
    name = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(label="Descripción de tarea", widget=forms.Textarea)
    