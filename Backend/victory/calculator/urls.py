from django.urls import path
from calculator.views import CalculatorView


urlpatterns = [
    path('calculator/', CalculatorView.as_view(), name='calculator')
]