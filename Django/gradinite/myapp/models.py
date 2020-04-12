from django.db import models

# Create your models here.


class gradinitaModel(models.Model):

    class Meta:
        ordering = ['-nume']

    nume = models.CharField(max_length=30, help_text="Numele gradinitei", primary_key=True)
    adresa = models.CharField(max_length=50, help_text="Adresa")
    telefon = models.CharField(max_length=15, help_text="Telefon")
    email = models.EmailField(max_length=15, help_text="Email")
    website = models.CharField(max_length=30, help_text="Website")
    capacitate = models.IntegerField(help_text="Capacitate copii")
    tip = models.CharField(max_length=10, help_text="Gradinita privata sau de stat", default=None)
    sector = models.CharField(max_length=15, help_text="Sectorul gradinitei", default=None)

    list_filter = ('nume', 'adresa', 'email')

    def __str__(self):
        return self.nume
