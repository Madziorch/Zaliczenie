from django.urls import path
from .views import (
	ZadanieListaWidok,
    ZadanieSzczegolyWidok,
    ZadanieDodajWidok,
    ZadanieEdytujWidok,
    ZadanieUsunWidok
    )

app_name = 'harmonogram'
urlpatterns = [
	path('', ZadanieListaWidok.as_view(), name='zadanie-lista'),
    path('dodaj', ZadanieDodajWidok.as_view(), name='zadanie-dodaj'),
    path('<int:id>/', ZadanieSzczegolyWidok.as_view(), name='zadanie-szczegoly'),
    path('<int:id>/edytuj/', ZadanieEdytujWidok.as_view(), name='zadanie-edytuj'),
    path('<int:id>/usun/', ZadanieUsunWidok.as_view(), name='zadanie-usun'),
]