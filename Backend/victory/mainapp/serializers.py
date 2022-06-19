from rest_framework import serializers
from .models import Profile, Contact, Post, Team
from djoser.serializers import UserCreateSerializer





class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    """Сериалайзер для формы обратной связи"""



    def validate(self, data):
       phone = data.get('phone')
       if len(phone)!=11:
           message = 'Номер телефона должен быть 11 цифр'
           raise serializers.ValidationError(message)
       return data


    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'message')
        validators = []



class PostSerializer(serializers.ModelSerializer):
    """Сериалайзер для создания статьи"""

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

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
        fields = ('title', 'content', 'owner', 'subcategory')
        validators = []



class PostUserUpdateSerializer(serializers.ModelSerializer):
    """Сериалайзер для редактирования статьи владельцем"""

    class Meta:
        model = Post
        fields = ('title', 'content')


class PostListSerializer(serializers.ModelSerializer):
    """Сериалайзер для всех статей"""

    class Meta:
        model = Post
        fields = '__all__'


class PostUpdateAdminSerializer(serializers.ModelSerializer):
    """Сериалайзер для редактирования  статей админом"""

    class Meta:
        model = Post
        fields = ('title', 'content', 'is_active', 'is_private', 'subcategory')


class TeamCreateSerializer(serializers.ModelSerializer):
    """Сериалайзер для создания команды"""

    class Meta:
        model = Team
        fields = ('title', 'members')


class TeamsSerializer(serializers.ModelSerializer):
    """Сериалайзер для всех команд"""

    class Meta:
        model = Team
        fields = ('title', 'id')


class TeamSerializer(serializers.ModelSerializer):
    """Сериалайзер для одной команд"""

    class Meta:
        model = Team
        fields = '__all__'
