from email import message_from_binary_file
from unicodedata import name
from django.forms import EmailField, ValidationError
from rest_framework import serializers
from .models import Profile, Contact, Post, Team, Category, User, Project
from djoser.serializers import UserSerializer
from django.core.mail import send_mail
from rest_framework.response import Response
from django.conf import settings



class ProfileSerializer(serializers.ModelSerializer):
    """Сериализатор для модели профиля(члена команды)"""

    user = serializers.StringRelatedField(read_only=True)
    scrum_master = serializers.BooleanField()
    role = serializers.ChoiceField(choices=Profile.ROLE_CHOICES)
    phone = serializers.IntegerField()
    avatar = serializers.ImageField()

    def validate(self, data):
        phone = data.get('phone')
        len_phone = str(phone)
        print(type(phone))
        if type(phone)!=int:
            message = 'Номер телефон должен быть числом'
            raise serializers.ValidationError(message)
        elif len(len_phone) != 11:
            message = 'Номер телефона должен быть 11 цифр'
            raise serializers.ValidationError(message)
    

    class Meta:
        model = Profile
        fields = ('user' , 'phone', 'avatar', 'role', 'id', 'scrum_master')


class SpecialUserSerializer(serializers.ModelSerializer):
    """Переопределение сериализатора для модели User"""

    is_admin = serializers.BooleanField(read_only=True, source='is_staff')
    avatar = serializers.CharField(source='profile.avatar')
    email = serializers.EmailField()
    username = serializers.CharField()



    class Meta:
        model = User
        fields = ('username', 'email', 'id', 'is_admin', 'avatar',)


class ContactSerializer(serializers.Serializer):
    """Сериалайзер для формы обратной связи на главной странице
     с последующей отправкой на почту менеджерам"""

    phone = serializers.IntegerField()
    email = serializers.EmailField()
    message = serializers.CharField()
    name = serializers.CharField(max_length=50)
    type_product = serializers.ChoiceField(choices=Contact.TYPE_PRODUCT_CHOICES)


    def validate(self, data):
        phone = data.get('phone')
        len_phone = str(phone)
        print(type(phone))
        if type(phone)!=int:
            message = 'Номер телефон должен быть числом'
            raise serializers.ValidationError(message)
        elif len(len_phone) != 11:
            message = 'Номер телефона должен быть 11 цифр'
            raise serializers.ValidationError(message)
        return data
    
    def create(self, validated_data):
        new_contact = Contact.objects.create(
            phone=validated_data['phone'],
            email=validated_data['email'],
            message=validated_data['message'],
            name=validated_data['name'],
            type_product=validated_data['type_product']
            )
        new_contact.save()
        send_mail('Заказ обратного звонка',
                  'Здраствуйте меня зовут {} ' 
                  ' я хотел бы узнать у вас подробнее об услуге по разработке продукта {}'
                  ' подробности в сообщении: {}'
                  ' для связи мой номер телефона"{}"  '
                  ' и мой email"{}"'.
                  format(validated_data['name'], validated_data['type_product'], validated_data['message'], validated_data['phone'], validated_data['email']),
                  settings.EMAIL_SERVER, settings.EMAIL_HOST_MANAGERS,
                  fail_silently=False
                  )
        return new_contact

    
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone', 'type_site', 'message')
        validators = []


class CategoryCreateSerializers(serializers.ModelSerializer):
    """Сериалайзер для создания категории"""

    parent_road = serializers.CharField(read_only=True, source='parent.road')


    class Meta:
        model = Category
        fields = ('title', 'parent', 'parent_road', 'id')


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
    is_active = serializers.BooleanField()
    is_private = serializers.BooleanField()


    class Meta:
        model = Post
        fields = (
                'title', 'content', 'id', 'owner', 'owner_avatar',
                'category', 'road', 'is_active', 'is_private'
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
        fields = (
            'title', 'category', 'category_title', 'owner', 'avatar',
             'road', 'id', 'slug', 'is_active', 'is_private'
             )



class ProjectSerializers(serializers.ModelSerializer):
        """Сериалайзер для создания проекта"""
        

        class Meta:
            model = Project
            fields = ('__all__')


class ProjectsListSerializers(serializers.ModelSerializer):
        """Сериалайзер для получения списка проектов"""

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




