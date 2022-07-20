from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
import json 
from django.http import JsonResponse
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.core.mail import send_mail
from django.db.models import Q
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    GenericAPIView,
)
from .models import Profile, Contact, Post, Team, Category, Project
from .permissions import IsOwnerProfileOrReadOnly, IsOwnerOrAdminOrReadOnly
from .utils import category_tree, get_childrens_id
from .filters import PostFilter
from .serializers import (
    ProfileSerializer,
    ContactSerializer,
    PostSerializer,
    PostListSerializer,
    PostUserUpdateSerializer,
    TeamCreateSerializer,
    TeamSerializer,
    TeamsSerializer,
    CategoryCreateSerializers,
    CategoriesSerializers,
    ProjectSerializers,
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
    pagination_class = None


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
    serializer_class = PostListSerializer
    permission_classes = [AllowAny]
    pagination_class = LimitOffsetPagination
    limit_query_param = 'limit'
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PostFilter


    def get(self, request, *args, **kwargs,):
        #category_childrens_id = get_childrens_id()
        if request.user.is_staff:
            self.queryset = Post.objects.all()
            return self.list(request, *args, **kwargs)
        elif request.user.is_authenticated:
            self.queryset = Post.objects.filter(Q(is_active=True, is_private=True) | Q(owner=request.user) | Q(category=category_childrens_id))
            return self.list(request, *args, **kwargs)
        else:
            self.queryset = Post.objects.filter(is_active=True, is_private=False)
            return self.list(request, *args, **kwargs)


class PostDetailView(RetrieveUpdateDestroyAPIView):
    """Статья"""
    queryset = Post.objects.all()
    serializer_class = PostUserUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminOrReadOnly]

    def get(self, request, *args, **kwargs):
        if request.user:
            return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):

        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


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


class ClassAPIView(APIView):
    def get(self, request):
        data = category_tree()
        json_data = json.dumps(data)
        return JsonResponse(data, safe=False)


class ProjectCreateView(CreateAPIView):
    """Создание проекта(только админ)"""
    serializer_class = ProjectSerializers
    permission_classes = [IsAdminUser]
