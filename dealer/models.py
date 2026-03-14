from django.db import models


class Dealer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="Название дилера", max_length=255, null=True)
    email = models.EmailField(verbose_name="Почта дилера", blank=True)
    phone = models.CharField(verbose_name="Телефон дилера", max_length=20, blank=True)
    address = models.CharField(verbose_name="Адрес дилера", max_length=255, blank=True) 
    def __str__(self):
        return str(self.name) if self.name else f"Дилер {self.id}"
