from django.db import models
from django.urls import reverse

class Zadanie(models.Model):
	temat = models.CharField(max_length=150)
	opis = models.TextField(blank=False, null=False)
	uwagi = models.TextField(blank=True, null=True)
	zrealizowany = models.BooleanField(default=False)

	def get_absolute_url(self):
		return reverse("harmonogram:zadanie-szczegoly", kwargs={"id": self.id}) 