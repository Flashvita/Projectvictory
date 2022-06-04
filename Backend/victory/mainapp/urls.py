from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    ProfileListCreateView,
    ProfileDetailView,
    ContactCreateView,
    PostCreateView,
    PostListView,
    PostDetailAdminView,
    PostDetailView,
)

urlpatterns = [
    path('', ContactCreateView.as_view()),
    path('post/create/', PostCreateView.as_view()),
    path('posts/', PostListView.as_view()),
    path('posts/detail/<int:pk>/', PostDetailView.as_view()),
    path('posts/detail_admin/<int:pk>/', PostDetailAdminView.as_view()),
    path('all-profiles/', ProfileListCreateView.as_view(), name="all-profiles"),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name="profile"),
]
