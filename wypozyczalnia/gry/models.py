from django.db import models
from django.contrib import admin


class NazwaGry(models.Model):
    class Meta:
        verbose_name_plural = "Nazwy Gier"
        ordering=['Tytul']
    Tytul = models.CharField(max_length=200)
    DostepnySklep = models.BooleanField(default=False)
    Data_wypozyczenie = models.DateField(null=True, blank=True)
    Data_orientacyjny_zwrot = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.Data_orientacyjny_zwrot is not None:
            self.DostepnySklep = False
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Tytul


'''
class Wybor(models.Model):
    pytanie = models.ForeignKey(NazwaGry, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.pytanie
'''
