from django.shortcuts import render
from gry.models import NazwaGry
import json
from django.http import JsonResponse


def index(request):
    Lista_gier = NazwaGry.objects.all().order_by('Tytul')
    Ilosc_gier = NazwaGry.objects.all().count()
    context = {'Lista_gier': Lista_gier,
               "Ilosc_gier": Ilosc_gier}
    return render(request, 'gry/index.html', context)


def szukajGry(request):
    if request.method == 'POST':
        szukane = json.loads(request.body).get('szukanyText')

        wynik = NazwaGry.objects.filter(Tytul__icontains=szukane) | \
            NazwaGry.objects.filter(
                Data_orientacyjny_zwrot__icontains=szukane)
        dane = wynik.values()

        return JsonResponse(list(dane), safe=False)
