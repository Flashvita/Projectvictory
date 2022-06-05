from rest_framework import serializers
from .models import Profile, Contact, Post


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Profile
        fields = ('avatar', 'phone')


class ContactSerializer(serializers.ModelSerializer):
    """Сериалайзер для формы обратной связи"""

    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'message')


class PostSerializer(serializers.ModelSerializer):
    """Сериалайзер для создания статьи"""

    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('title', 'content', 'owner')


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
        fields = ('title', 'content', 'is_active', 'is_private')
