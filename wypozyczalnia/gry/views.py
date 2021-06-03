from django.shortcuts import render
from gry.models import NazwaGry
import json
from django.http import JsonResponse


def index(request):
    Lista_gier = NazwaGry.objects.all().order_by('Tytul')
    context = {'Lista_gier': Lista_gier}
    return render(request, 'gry/index.html', context)


def szukaj(request):
    if request.method == 'POST':
        szukane = json.loads(request.body).get('szukanyText')

        wynik = NazwaGry.objects.filter(Tytul__icontains=szukane) | \
            NazwaGry.objects.filter(
                Data_orientacyjny_zwrot__stars_with=szukane)
        dane = wynik.values()

        return JsonResponse(list(dane), safe=False)
