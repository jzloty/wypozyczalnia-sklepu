from django.contrib import admin

from .models import NazwaGry


class NazwaGryAdmin(admin.ModelAdmin):
    list_display = ('Tytul', 'Data_orientacyjny_zwrot',
                    'Data_wypozyczenie','DostepnySklep')
    search_fields = ['Tytul']

    actions = ['Ustaw_niedostepne',
               'Ustaw_dostepne']

    def Ustaw_niedostepne(self, request, queryset):
        queryset.update(DostepnySklep=False)

    def Ustaw_dostepne(self, request, queryset):
        queryset.update(DostepnySklep=True)


admin.site.register(NazwaGry, NazwaGryAdmin)
