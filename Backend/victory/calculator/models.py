from random import choices
from tabnanny import verbose
from django.db import models

class Calculator(models.Model):


    Shop = '25000.0'
    Catalog = '20000.0'
    Lenging = '10000.0'
    Corporate = '30000.0'
    Education = '40000.0'
    
    TYPE_PRODUCT_COST_CHOICES = (
        (Shop, 'Интернет магазин'),
        (Catalog, 'Сайт каталог товаров'),
        (Lenging, 'Лендинг'),
        (Corporate, 'Корпаративный сайт'),
        (Education, 'Образовательная платформа'),
    )


    type_product = models.FloatField(choices=TYPE_PRODUCT_COST_CHOICES)

    Development = '1.2'
    Not_develompent = '1.0'

    DESINGER_CHOICES = (
        (Development, 'Pазработка дизайна'),
        (Not_develompent, 'Дизайн готов'),
    )

    desinger = models.FloatField(
                                        
                                        choices=DESINGER_CHOICES, verbose_name='Дизайн'
                                        )
    Standart = '1.2'
    Expanded = '1.4'
    
    CSM_TYPE_CHOICES = (
        (Standart, 'Стандартная CMS'),
        (Expanded, 'Расширенная CMS'),
    )

    cms = models.FloatField(choices=CSM_TYPE_CHOICES, verbose_name='Тип CMS'
                                        )

    Content_full = '1.1'
    Content_not = '1.0'
    CONTENT_FILLING_TYPE_CHOICES = (
        (Content_not,'Наполняется заказчиком'),
        (Content_full, 'Наполняется нами'),

    )
    content = models.FloatField(
                                       
                                        choices=CONTENT_FILLING_TYPE_CHOICES, verbose_name='Наполнение контентом'
                                        )

    

    class Meta:
        verbose_name = 'Калькулятор'
        verbose_name_plural = 'Калькуляторы'

    
                                        
