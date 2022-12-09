from django.contrib.auth.models import User
from django.db import models


class Transaction_Exchange(models.Model):
    model = models.CharField(max_length=50, verbose_name='Модель')
    field = models.CharField(max_length=50, verbose_name='Поле')
    old_data = models.CharField(max_length=2000, verbose_name='Старые данные')
    new_data = models.CharField(max_length=2000, verbose_name='Новые данные')
    date_exchange = models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения данных')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Регистрация изменения данных'
        verbose_name_plural = 'Регистрация изменения данных'