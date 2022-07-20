from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    ProfileListCreateView,
    ProfileDetailView,
    ContactCreateView,
    PostCreateView,
    PostListView,
    PostDetailView,
    TeamCreateView,
    TeamsView,
    TeamDetailView,
    CategoryCreateView,
    CategoriesView,
    ClassAPIView,
    ProjectCreateView,
)

urlpatterns = [
    path('', ContactCreateView.as_view()),
    path('post/create/', PostCreateView.as_view()),
    path('posts/', PostListView.as_view()),
    path('posts/detail/<int:pk>/', PostDetailView.as_view()),
    path('team/create/', TeamCreateView.as_view()),
    path('category/create/', CategoryCreateView.as_view()),
    path('categories/', CategoriesView.as_view()),
    path('childrens/', ClassAPIView.as_view()),
    path('teams/', TeamsView.as_view()),
    path('teams/detail/<int:pk>/', TeamDetailView.as_view()),
    path('all-profiles/', ProfileListCreateView.as_view(), name="all-profiles"),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name="profile"),
    path('project/create/', ProjectCreateView.as_view()),
]
