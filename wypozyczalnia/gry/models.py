from django.db import models


class NazwaGry(models.Model):
    class Meta:
        verbose_name_plural = "Nazwy Gier"
    Tytul = models.CharField(max_length=200)
    Data_wypozyczenie = models.DateTimeField('data wypozyczenia', null=True)
    Dostepnosc = models.BooleanField(default=True)
    Data_orientacyjny_zwrot = models.DateTimeField('data orientacyjnego'
                                                   ' zwrotu', null=True)

    def __str__(self):
        return self.Tytyl


'''
class Wybor(models.Model):
    pytanie = models.ForeignKey(NazwaGry, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.pytanie
'''
