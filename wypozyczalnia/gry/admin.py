from django.contrib import admin

from .models import NazwaGry


class NazwaGryAdmin(admin.ModelAdmin):
    list_display = ('Tytul', 'Data_orientacyjny_zwrot',
                    'Dostepnosc', 'Data_wypozyczenie')


admin.site.register(NazwaGry, NazwaGryAdmin)
