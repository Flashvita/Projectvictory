from customers.models import Customer
from rest_framework import serializers



class CustomerCreateSirializer(serializers.ModelSerializer):
    """Сериалайзер для создания клиента"""
    name = serializers.CharField(max_length=50)
    phone = serializers.IntegerField()
    email = serializers.EmailField()

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
    
    def create(self, validated_data):
        new_contact = Customer.objects.create(
            phone=validated_data['phone'],
            email=validated_data['email'],
            name=validated_data['name']
        )
        new_contact.save()

    class Meta:
        model = Customer
        fields = ('name', 'phone', 'email')
