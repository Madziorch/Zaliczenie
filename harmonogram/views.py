from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from django.views.generic import (
	CreateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView
	)

from .forms import ZadanieForm
from .models import Zadanie

class ZadanieDodajWidok(CreateView):
	template_name = 'harmonogram/zadanie_dodaj.html'
	form_class = ZadanieForm
	queryset = Zadanie.objects.all()

	def form_valid(self, form):
		return super().form_valid(form)

class ZadanieEdytujWidok(UpdateView):
	template_name = 'harmonogram/zadanie_edytuj.html'
	form_class = ZadanieForm

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Zadanie, id=id_)

	def form_valid(self, form):
		print(form.cleaned_data)
		return super().form_valid(form)

class ZadanieUsunWidok(DeleteView):
	template_name = 'harmonogram/zadanie_usun.html'

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Zadanie, id=id_)

	def get_success_url(self):
		return reverse('harmonogram:zadanie-lista')

class ZadanieListaWidok(ListView):
	template_name = 'harmonogram/zadanie_lista.html'
	queryset = Zadanie.objects.all()

class ZadanieSzczegolyWidok(DetailView):
	template_name = 'harmonogram/zadanie_szczegoly.html'
	queryset = Zadanie.objects.all()

	def get_object(self):
		id_ = self.kwargs.get("id")
		return get_object_or_404(Zadanie, id=id_)