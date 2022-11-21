from django.contrib.auth import get_user_model
from django.db import models


class Item(models.Model):
    """Items models"""
    name = models.CharField(max_length=50, verbose_name='Name')
    description = models.TextField(verbose_name='Descriptions')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Price')
    CURRENCY_TYPE = (
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('AMD', 'AMD'),
        ('RUB', 'RUB')
    )
    currency = models.CharField(max_length=3, default='USD', choices=CURRENCY_TYPE)

    def __str__(self) -> str:
        return self.name

    def get_price(self):
        return self.price


class Order(models.Model):
    """This model for Order in Cart"""
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='User')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Item in Cart')

    def __str__(self) -> str:
        return f'{self.user.username} - {self.item.price}'


class Discount(models.Model):
    """Discount code for create coupone"""
    item = models.OneToOneField(
        Item,
        on_delete=models.CASCADE,
        verbose_name='Discount',
        unique=True
    )
    procent = models.PositiveIntegerField(verbose_name='Procent_discount')
    code = models.CharField(max_length=10, verbose_name='Id_Coupone')


    def __str__(self) -> str:
        return f'Discount {self.procent}% for {self.item.name}'

    def get_code(self) -> str:
        return self.code
