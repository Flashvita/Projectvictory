from email import message_from_binary_file
from django.forms import EmailField, ValidationError
from rest_framework import serializers
from .models import Profile, Contact, Post, Team, Category, User, Project
from djoser.serializers import UserSerializer
from django.core.mail import send_mail
from rest_framework.response import Response



class ProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для модели профиля(члена команды)"""
    user = serializers.StringRelatedField(read_only=True)
    scrum_master = serializers.BooleanField()
    role = serializers.CharField()
    avatar = serializers.ImageField()

    class Meta:
        model = Profile
        fields = ('user' , 'phone', 'avatar', 'role', 'id', 'scrum_master')


class SpecialUserSerializer(serializers.ModelSerializer):
    """Переопределение сериализатора для модели User"""

    is_admin = serializers.BooleanField(read_only=True, source='is_staff')
    avatar = serializers.CharField(read_only=True, source='profile.avatar')


    class Meta:
        model = User
        fields = ('username', 'email', 'id', 'is_admin', 'avatar',)

class ContactSerializer(serializers.Serializer):
    """Сериалайзер для формы обратной связи на главной странице"""
    phone = serializers.IntegerField()

    def validate(self, data):
        phone = data.get('phone')
        len_phone = str(phone)
        if type(phone) is not int:
            message = 'Номер телефон должен быть числом'
            raise serializers.ValidationError(message)
        elif len(len_phone) != 11:
            message = 'Номер телефона должен быть 11 цифр'
            raise serializers.ValidationError(message)
        return data

    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'message')
        validators = []      


class CategoryCreateSerializers(serializers.ModelSerializer):
    """Сериалайзер для создания категории"""
    parent_title = serializers.CharField(read_only=True, source='parent.title')


    class Meta:
        model = Category
        fields = ('title', 'parent', 'parent_title', 'id')


class CategoriesSerializers(serializers.ModelSerializer):
    """Сериалайзер для отображения всех категорий"""

    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    """Сериалайзер для создания статьи"""

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    category_title = serializers.CharField(read_only=True, source='category.title')



    def validate(self, data):
       content = data.get('content')
       title = data.get('title')
       if len(title) < 5:
           message = 'Название статьи должно быть больше 5 символов'
           raise serializers.ValidationError(message)
       if len(content) < 500:
           message = 'Статья должна быть больше 500 символов'
           raise serializers.ValidationError(message)
       return data

    class Meta:
        model = Post
        fields = ('title', 'content', 'id', 'owner', 'category', 'category_title')
        validators = []


class PostUserUpdateSerializer(serializers.ModelSerializer):
    """Сериалайзер для редактирования статьи владельцем и админом"""

    owner = serializers.CharField(read_only=True, source='owner.username')
    owner_avatar = serializers.CharField(read_only=True, source='owner.profile.avatar')
    category_title = serializers.CharField(read_only=True, source='category.title')
    is_active = serializers.BooleanField()
    is_private = serializers.BooleanField()

    

    class Meta:
        model = Post
        fields = ('title', 'content', 'id', 'owner', 'owner_avatar',
                 'category', 'category_title', 'is_active', 'is_private'
                 )


class PostListSerializer(serializers.ModelSerializer):
    """Сериалайзер для отображения всех статей"""


    owner = serializers.CharField(read_only=True, source='owner.username')
    avatar = serializers.CharField(read_only=True, source='owner.profile.avatar')
    category_title = serializers.CharField(read_only=True, source='category.title')
    is_active = serializers.BooleanField(read_only=True)
    is_private = serializers.BooleanField(read_only=True)


    class Meta:
        model = Post
        fields = ('title', 'category', 'category_title', 'owner', 'avatar', 'road', 'id', 'slug', 'is_active', 'is_private')



class ProjectSerializers(serializers.ModelSerializer):
        """Сериалайзер для создания проекта"""

        class Meta:
            model = Project
            fields = ('__all__')

class TeamCreateSerializer(serializers.ModelSerializer):
    """Сериалайзер для создания команды"""


    class Meta:
        model = Team
        fields = ('title', 'members',)


class TeamsSerializer(serializers.ModelSerializer):
    """Сериалайзер для всех команд"""
    members = ProfileSerializer(read_only=True, many=True)
    project = ProjectSerializers()


    class Meta:
        model = Team
        fields = ('__all__')


class TeamSerializer(serializers.ModelSerializer):
    """Сериалайзер для одной команды"""


    class Meta:
        model = Team
        fields = '__all__'


