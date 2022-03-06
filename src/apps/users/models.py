
from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    
    def __str__(self):
        return f'{self.description[:20]} >> {self.title}'


# learn this class
class Employee(AbstractUser):

    SEX_COICES = (
        ('M' , 'man'),
        ('W' , 'women')
    )

    sex = models.CharField(max_length=1, choices=SEX_COICES)
    telephone = models.CharField(max_length=12)
    role = models.ForeignKey(Role, null=True, on_delete=models.CASCADE)
