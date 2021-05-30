from django.contrib import admin

from .models import NazwaGry


class NazwaGryAdmin(admin.ModelAdmin):
    list_display = ('Tytul', 'Data_orientacyjny_zwrot',
                    'Data_wypozyczenie')
    search_fields = ['Tytul']


admin.site.register(NazwaGry, NazwaGryAdmin)
