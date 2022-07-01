from rest_framework import serializers
from .models import Profile, Contact, Post, Team, Category, User
from djoser.serializers import UserSerializer


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'


class SpecialUserSerializer(serializers.ModelSerializer):

    is_admin = serializers.CharField(read_only=True, source='is_staff')

    class Meta:
        model = User
        fields = ('username', 'email', 'id', 'is_admin')

class ContactSerializer(serializers.ModelSerializer):
    """Сериалайзер для формы обратной связи"""

    def validate(self, data):
       phone = data.get('phone')
       if len(phone) != 11:
           message = 'Номер телефона должен быть 11 цифр'
           raise serializers.ValidationError(message)
       return data

    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'message')
        validators = []


class CategoryCreateSerializers(serializers.ModelSerializer):
    """Сериалайзер для создания категории"""

    class Meta:
        model = Category
        fields = ('title', 'parent')


class CategoriesSerializers(serializers.ModelSerializer):
    """Сериалайзер для всех категорий"""

    class Meta:
        model = Category
        fields = '__all__'


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
        fields = ('title', 'content', 'owner', 'category')
        validators = []


class PostUserUpdateSerializer(serializers.ModelSerializer):
    """Сериалайзер для редактирования статьи владельцем и админом"""



    class Meta:
        model = Post
        fields = ('title', 'content', 'category', 'is_active', 'is_private')


class PostListSerializer(serializers.ModelSerializer):
    """Сериалайзер для всех статей"""

    owner = serializers.CharField(read_only=True, source='owner.username')
    avatar = serializers.CharField(read_only=True, source='owner.profile.avatar')

    class Meta:
        model = Post
        fields = ('title', 'category', 'owner', 'avatar', 'road', 'id', 'slug',)


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
