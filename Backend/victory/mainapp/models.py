from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from transliterate import slugify
from transliterate.utils import translit



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
    created = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата создания профиля')
    #updated = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Дата последнего редактирования профиля')
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, verbose_name='Роль', null=True, blank=True)
    scrum_master = models.BooleanField(default=False, verbose_name='Скрам мастер')

    def __str__(self):
        return f"{self.user.username}"            

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


class Contact(models.Model):
    """Модель формы обратной связи"""

    name = models.CharField(max_length=200, verbose_name='Имя')
    phone = models.CharField(max_length=11, verbose_name='Номер телефона', null=True, blank=True)
    message = models.TextField(max_length=500, verbose_name='Сообщение')
    email = models.EmailField(max_length=200)
    created = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Время отправления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'


class Category(models.Model):
    """Категория"""

    title = models.CharField(max_length=200, verbose_name='Название категории')
    parent = models.ForeignKey('Category', on_delete=models.CASCADE,
                               verbose_name='Родитель', null=True, blank=True, default=None
                               )
    level = models.IntegerField(verbose_name='Уровень')
    slug = models.SlugField(max_length=255, unique=False)
    road = models.CharField(max_length=500, verbose_name='Путь')

    def __str__(self):
        return f"{self.title}"
    

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_trunslite = translit(value=self.title, language_code='ru')
            self.slug = slugify(slug_trunslite)
            if not self.parent:
                self.level = 0
                self.road = self.slug + '/'
            else:
                self.level = self.parent.level + 1
                self.road = self.parent.road + self.slug + '/'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    """Статьи"""

    title = models.CharField(max_length=200, verbose_name='Заголовок статьи')
    slug = models.SlugField(max_length=255, unique=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    content = models.TextField(verbose_name='Содержимое')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_owner')
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True, db_index=True, verbose_name='Время публикации')
    road = models.CharField(max_length=700, verbose_name='Путь')
    is_private = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_trunslite = translit(value=self.title, language_code='ru')
            self.slug = slugify(slug_trunslite)
            if not self.road:
                self.road = self.category.road + self.slug + '/'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Team(models.Model):
    """Команда"""

    title = models.CharField(max_length=100, verbose_name='Название комады')
    members = models.ManyToManyField(Profile, verbose_name='Члены команды', null=True, blank=True)
    created = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    project = models.ForeignKey('Project', on_delete=models.SET_NULL,
                                null=True, blank=True, verbose_name='Текущий проект')
    

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'


class Project(models.Model):
        """Проект"""
        title = models.CharField(max_length=500, verbose_name='Название проекта')
        description = models.TextField(verbose_name='Описание проекта')


        def __str__(self):
            return f'{self.id}'
            
        class Meta:
            verbose_name = 'Проект'
            verbose_name_plural = 'Проекты'



