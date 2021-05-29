from django.shortcuts import render
from gry.models import NazwaGry


def index(request):
    Lista_gier = NazwaGry.objects.all()
    context = {'Lista_gier': Lista_gier}
    return render(request, 'gry/index.html', context)
