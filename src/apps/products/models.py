from django.db import models
from django.contrib.auth import get_user_model



class Product(models.Model):
    CHOICE_CURRENCY = (
        ('RUB', 'рубли'),
        ('EUR', 'евро'),
        ('USD', 'доллар'),
        ('USD1', 'доллар1')
    )

    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    photo = models.CharField('Фото', max_length=255)
    quantity = models.IntegerField('Количество', blank=False)
    price = models.DecimalField('Цена', max_digits=15, decimal_places=2)
    currency = models.CharField('Валюта', max_length=32, choices=CHOICE_CURRENCY)


    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.title}, {self.quantity}, {self.price}, {self.currency}"



EMPLOYEE = get_user_model()

class Order(models.Model):
    employee = models.ForeignKey(EMPLOYEE, on_delete=models.CASCADE)
    description = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.employee}, {self.description}, {self.date}"


if __name__ == '__main__':
    pass
