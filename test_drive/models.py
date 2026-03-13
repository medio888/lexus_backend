from django.db import models
from api.models import Products
from dealer.models import Dealer

class TestDrive(models.Model):
    id = models.AutoField(primary_key=True)
    
    product = models.ForeignKey(
        Products, 
        on_delete=models.CASCADE, 
        related_name="test_drives",
        verbose_name="Продукт (ID)",
        null=True

    )
    dealer = models.ForeignKey(
        Dealer,
        on_delete=models.CASCADE,
        related_name="test_drives",
        verbose_name="Дилер (ID)",
        null=True
    )
    
    name = models.CharField(verbose_name="Имя пользователя", max_length=100)
    email = models.EmailField(verbose_name="Почта", blank=True)
    
    phone = models.CharField(
        verbose_name="Номер телефона",
        max_length=13,
        help_text="Номер должен начинаться с +996",
    )
    
    date = models.DateTimeField(verbose_name="Дата заявки")
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.phone.startswith("+996"):
            self.phone = "+996" + self.phone.lstrip("0")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.product} - {self.dealer} - {self.phone}"