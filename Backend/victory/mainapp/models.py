from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse




class Profile(models.Model):
    """Профиль пользователя"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='пользователь', related_name='profile')
    slug = models.SlugField(max_length=255, unique=False)
    phone = models.CharField(max_length=11, default='8xxxxxxxxxx', null=True, blank=True, verbose_name='номер телефона')
    avatar = models.ImageField(upload_to='images/users/%Y/%m/%d/', null=True, blank=True, verbose_name='Ваше фото')
    created = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'
