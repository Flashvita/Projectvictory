from django.db import models
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post
from django_filters import CharFilter


class PostFilter(filters.FilterSet, filters.CharFilter ):
    """Фильтрация для всех Постов с переопределением
     filter_overrides для category__road
     (при запросе постов категории в queryset добавляются в посты потомков этой категории) """

    class Meta:
        model = Post
        fields = ('category', 'category__road')
        filter_overrides = {
             models.CharField: {
                 'filter_class': CharFilter,
                 'extra': lambda f: {
                     'lookup_expr': 'icontains',
                 },
             },
        }
