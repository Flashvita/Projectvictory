from turtle import reset
from unicodedata import decimal
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from requests import Response
from calculator.serializers import CalculatorSerializer
from rest_framework.permissions import AllowAny
from rest_framework import generics
from fastnumbers import fast_real


class CalculatorView(generics.CreateAPIView):
    """"Api для калькулятора цен"""

    serializer_class = CalculatorSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        type_product = request.data.get('type_product')
        desinger = request.data.get('desinger')
        cms = request.data.get('cms')
        content = request.data.get('content')
       
       
        res = fast_real(float(type_product))*(fast_real(float(desinger)))*(fast_real(float(cms)))*(fast_real(float(content)))
        print(res)
        return HttpResponseRedirect('/server/api/v1/calculator/', res)


