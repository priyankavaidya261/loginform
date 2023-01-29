from django import forms


class MyForm(forms.Form):
	name = forms.CharField(label="name",max_length=100)