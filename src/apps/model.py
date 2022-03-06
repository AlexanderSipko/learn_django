from django.db import models
from datetime import datetime



class Role(models.Model):
    title = models.ManyToManyRel
    description = models.CharField(max_length=255)


class Emploeyy(models.Model):

    SEX_COICES = (
        ('M' , 'man'),
        ('W' , 'women')
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    sex = models.CharField(max_length=1, choice=SEX_COICES)
    telephone = models.CharField(max_length=12)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


class Order(models.Model):
    employee = models.ForeignKey(Emploeyy, on_delete=models.CASCADE)
    description = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(default=datetime.now)


class Product(models.Model):
    CHOICE_CURRENCY = (
        ('RUB', 'рубли'),
        ('EUR', 'евро'),
        ('USD', 'доллар')
    )

    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    photo = models.CharField('Фото', max_length=255)
    quantity = models.IntegerField(blank=False)
    price = models.DecimalField('Цена', max_digits=15, decimal_places=2)
    currency = models.CharField('Валюта', max_length=32, choices=CHOICE_CURRENCY)


    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"