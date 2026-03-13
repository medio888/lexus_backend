from django.db import models


class Dealer(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, verbose_name="Имя")
    last_name = models.CharField(max_length=100, verbose_name="Фамилия")
    birth_year = models.DateTimeField(verbose_name="год рождение")
    has_driver_license = models.BooleanField(verbose_name="Есть водительские права")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
