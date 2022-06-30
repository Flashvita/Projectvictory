from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .models import Profile, Contact, Post, Team, Category
from .permissions import IsOwnerProfileOrReadOnly, IsOwnerPostOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    GenericAPIView,
)

from .serializers import (
    ProfileSerializer,
    ContactSerializer,
    PostSerializer,
    PostListSerializer,
    PostUpdateAdminSerializer,
    PostUserUpdateSerializer,
    TeamCreateSerializer,
    TeamSerializer,
    TeamsSerializer,
    CategoryCreateSerializers,
    CategoriesSerializers,
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


class CategoryCreateView(CreateAPIView):
    """Создание категории"""
    serializer_class = CategoryCreateSerializers
    queryset = Category.objects.all()


class CategoriesView(ListCreateAPIView):
    """Все категории"""
    serializer_class = CategoriesSerializers
    queryset = Category.objects.all()


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
                  'DjangoServer2022@yandex.ru', ['DjangoServer2022@yandex.ru', 'Flashvita@yandex.ru'],
                  fail_silently=False
                  )
        Contact.objects.create(
            message=new_message['message'],
            phone=new_message['phone'],
            email=new_message['email'],
            name=new_message['name'],
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


