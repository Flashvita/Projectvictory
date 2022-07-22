from django.shortcuts import render
from rest_framework.generics import (
    ListCreateAPIView,
    CreateAPIView,
)
from customers.serializers import CustomerCreateSirializer
from rest_framework.permissions import IsAdminUser


class CustomeCreateView(CreateAPIView):
    serializer_class = CustomerCreateSirializer
    permission_classes = [IsAdminUser]
    