from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Profile(models.Model):
    """Профиль пользователя"""

    ROLE_CHOICES = (
        ('Backcend developer', 'Backcend developer'),
        ('Frontend developer', 'Frontend developer'),
        ('Fullstack developer', 'Fullstack developer'),
        ('Designer', 'Designer'),
        ('Seo', 'Seo'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='пользователь', related_name='profile')
    slug = models.SlugField(max_length=255, unique=False)
    phone = models.CharField(max_length=11, default='8xxxxxxxxxx', null=True, blank=True, verbose_name='номер телефона')
    avatar = models.ImageField(upload_to='images/users/%Y/%m/%d/', null=True, blank=True, verbose_name='Ваше фото')
    created = models.DateTimeField(auto_now=True, db_index=True)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, verbose_name='Роль')
    scrum_master = models.BooleanField(default=False, verbose_name='Скрам мастер')

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


class Contact(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    phone = models.CharField(max_length=11, verbose_name='Номер телефона', null=True, blank=True)
    message = models.TextField(max_length=500, verbose_name='Сообщение')
    email = models.EmailField(max_length=200)
    created = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Время отправления')

    def __str__(self):
        return self.name


class Post(models.Model):
    """Статьи"""
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    content = models.TextField(max_length=5000, verbose_name='Содержимое')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Время публикации')
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Team(models.Model):
    title = models.CharField(max_length=100)
    members = models.ManyToManyField(Profile, verbose_name='Команда', null=True, blank=True)
    created = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'



