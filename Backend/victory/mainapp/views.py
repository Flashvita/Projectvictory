from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView,)
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import Profile, Contact, Post, Team
from .permissions import IsOwnerProfileOrReadOnly, IsOwnerPostOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView
from django.core.mail import send_mail
from .serializers import (
    ProfileSerializer,
    ContactSerializer,
    PostSerializer,
    PostListSerializer,
    PostUpdateAdminSerializer,
    PostUserUpdateSerializer,
    TeamCreateSerializer,
    TeamSerializer,
    TeamsSerializer
)


class ProfileListCreateView(ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class ProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, IsAuthenticated]


class ContactCreateView(CreateAPIView):
    """Форма обратной связи"""
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        new_message = request.data

        send_mail('Заказ обратного звонка',
                  'Здраствуйте меня зовут {} '
                  'Сообщение: {}'
                  'мой номер телефона"{}"  '
                  'мой email"{}"'.
                  format(new_message['name'], new_message['message'], new_message['phone'], new_message['email']),
                  'DjangoTestemail2022@gmail.com', ['DjangoTestemail2022@gmail.com', 'Flashvita@yandex.ru'],
                  fail_silently=False
                  )
        return Response(status=200)


class PostCreateView(CreateAPIView):
    """Создать статью(и отправить на редактирование админу)"""
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class PostListView(ListCreateAPIView):
    """Все статьи"""
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [IsAuthenticated]


class PostDetailAdminView(RetrieveUpdateDestroyAPIView):
    """Отредактировать и опубликовать статью(доступно только админам)"""
    queryset = Post.objects.all()
    serializer_class = PostUpdateAdminSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class PostDetailView(RetrieveUpdateDestroyAPIView):
    """Статья"""
    queryset = Post.objects.all()
    serializer_class = PostUserUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerPostOrReadOnly]


class TeamCreateView(CreateAPIView):
    """Создание команды(только админ)"""
    serializer_class = TeamCreateSerializer
    permission_classes = [IsAdminUser]


class TeamsView(ListCreateAPIView):
    """Команды"""
    queryset = Team.objects.all()
    serializer_class = TeamsSerializer
    permission_classes = [IsAuthenticated]


class TeamDetailView(RetrieveUpdateDestroyAPIView):
    """Комада"""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAdminUser]


