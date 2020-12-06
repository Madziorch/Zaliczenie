from django import forms

from .models import Zadanie

class ZadanieForm(forms.ModelForm):
	temat = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Wpisz temat"}))
	opis = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Dodaj opis", "rows": 20, "cols": 60}))
	uwagi = forms.CharField(required=False, widget=forms.Textarea(attrs={"placeholder": "Dodaj uwagi", "rows": 15, "cols": 50}))
	class Meta:
		model = Zadanie
		fields = [
		'temat',
		'opis',
		'uwagi',
		'zrealizowany',
		]

