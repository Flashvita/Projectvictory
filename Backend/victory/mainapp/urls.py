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
    TeamCreateView,
    TeamsView,
    TeamDetailView,
)

urlpatterns = [
    path('', ContactCreateView.as_view()),
    path('post/create/', PostCreateView.as_view()),
    path('posts/', PostListView.as_view()),
    path('posts/detail/<int:pk>/', PostDetailView.as_view()),
    path('team/create/', TeamCreateView.as_view()),
    path('teams/', TeamsView.as_view()),
    path('team/detail/<int:pk>/', TeamDetailView.as_view()),
    path('posts/detail_admin/<int:pk>/', PostDetailAdminView.as_view()),
    path('all-profiles/', ProfileListCreateView.as_view(), name="all-profiles"),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name="profile"),
]
