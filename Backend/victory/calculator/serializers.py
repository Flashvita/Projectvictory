
from rest_framework import serializers
from calculator.models import Calculator


class CalculatorSerializer(serializers.ModelSerializer):
    """Сериализатор калькулятора цен для рассчёта стоимости проекта"""

    type_product = serializers.ChoiceField(choices=Calculator.TYPE_PRODUCT_COST_CHOICES)
    desinger = serializers.ChoiceField(choices=Calculator.DESINGER_CHOICES)
    cms = serializers.ChoiceField(choices=Calculator.CSM_TYPE_CHOICES)
    content = serializers.ChoiceField(choices=Calculator.CONTENT_FILLING_TYPE_CHOICES)


    class Meta:
        model = Calculator
        fields = ('__all__')

    