from django.db import models
from mainapp.models import Project


class Customer(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50)
    phone = models.IntegerField(verbose_name='номер телефона')
    email = models.EmailField(verbose_name='Почта')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, verbose_name='Проект', null=True, blank=True)
    created = models.DateField(auto_now_add=True, verbose_name='Дата заключения договора')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

