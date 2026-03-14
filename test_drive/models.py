from django.db import models
from api.models import Products
from dealer.models import Dealer


from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

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
        return f"{self.name} - {self.product} - {self.phone}"



@receiver(post_save, sender=TestDrive)
def send_test_drive_email(sender, instance, created, **kwargs):
    if created:  
        subject = f"Новая заявка на Тест-Драйв от {instance.name}"
        
        message = (
            f"Данные новой заявки:\n\n"
            f"👤 Имя: {instance.name}\n"
            f"📞 Телефон: {instance.phone}\n"
            f"📧 Email: {instance.email if instance.email else 'Не указан'}\n"
            f"🚗 Автомобиль: {instance.product}\n"
            f"📍 Дилер: {instance.dealer}\n"
            f"📅 Дата записи: {instance.date}\n"
            f"⏰ Создано: {instance.created_at}"
        )

        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['asanbekovmeder88@gmail.com'], 
                fail_silently=False,
            )
        except Exception as e:
            print(f"Ошибка отправки почты: {e}")