from django.db import models


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Category', max_length=255)

    def __str__(self):
        return self.name    


class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')
    name = models.CharField(verbose_name='SubCategory', max_length=255)
    fuel_info = models.CharField(verbose_name='Fuel_info', max_length=255)
    info = models.CharField(verbose_name='Info', max_length=1000)
    icon = models.ImageField(upload_to='subcategory_icons/', null=True, blank=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='products', null=True) 
    model = models.CharField(verbose_name='Model', max_length=255)
    price = models.CharField(verbose_name='Price', max_length=255, null=True, blank=True)  
    fuel = models.CharField(verbose_name='Fuel', max_length=255)
    gearbox = models.CharField(verbose_name='Gearbox', max_length=255)
    car_body = models.CharField(verbose_name='Car Body', max_length=255)
    drive = models.CharField(verbose_name='Drive', max_length=255)
    volume = models.CharField(verbose_name='Volume', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model





