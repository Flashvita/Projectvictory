from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Post


class PostFilter(filters.FilterSet):
    """Фильтрация для всех Постов"""

    class Meta:
        model = Post
        fields = ('is_active', 'is_private', 'category')

class PostsFiltersBackends(DjangoFilterBackend):

    def get_filterset(self, request, queryset, view):
        filterset_class = self.get_filterset_class(view, queryset)
        if filterset_class is None:
            return None

    def get_filterset_class(self, view, queryset=None):
        """
        Return the `FilterSet` class used to filter the queryset.
        """
        filterset_class = getattr(view, 'filterset_class', None)
        filterset_fields = getattr(view, 'filterset_fields', None)
        