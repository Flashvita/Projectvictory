from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
    ListAPIView,
)
from customers.serializers import CustomerCreateSirializer, CustomersListSerializer
from rest_framework.permissions import IsAdminUser
from customers.models import Customer


class CustomeCreateView(CreateAPIView):
    """Создание клиента(доступно только админам)"""
    serializer_class = CustomerCreateSirializer
    permission_classes = [IsAdminUser]


class CustomersListView(ListAPIView):
    serializer_class = CustomersListSerializer
    permission_classe = [IsAdminUser]
    queryset = Customer.objects.all()