from django import forms
from visitas_granada.models import Visita, Comentario

class VisitaForm(forms.ModelForm):
	class Meta:
		model = Visita
		fields = ['nombre', 'descripcion', 'foto']
		widgets = {
			'nombre': forms.TextInput(attrs={'size': 50}),
			'descripcion': forms.Textarea(attrs={'rows': 3, 'cols': 100}),
			'foto': forms.FileInput()
		}

	def clean(self):
		data = self.cleaned_data

		if not data["descripcion"][0].isupper():
			raise forms.ValidationError("La descripción debe empezar por mayúscula")

		print(data["foto"])

		if data["foto"] is None:
			raise forms.ValidationError("Debes elegir una fotografía.")
