from customers.models import Customer
from rest_framework import serializers
from mainapp.serializers import ProjectSerializers



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
        new_customer = Customer.objects.create(
            phone=validated_data['phone'],
            email=validated_data['email'],
            name=validated_data['name'],
            project=validated_data['project']
        )
        new_customer.save()

        return new_customer

    class Meta:
        model = Customer
        fields = ('__all__')


class CustomersListSerializer(serializers.ModelSerializer):
    """Сериалайзер для выода всех клиентов"""

    project = ProjectSerializers()

    class Meta:
        model = Customer
        fields = ('__all__')
    
    