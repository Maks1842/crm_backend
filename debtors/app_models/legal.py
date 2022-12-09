from django.contrib.auth.models import User
from django.db import models


class Legal(models.Model):
    debtor = models.ForeignKey('Debtors', blank=True, on_delete=models.PROTECT, verbose_name='Должник')
    executive_document = models.ForeignKey('Executive_Documents', blank=True, on_delete=models.PROTECT, verbose_name='Исполнительный документ')
    user = models.ForeignKey(User, blank=True, on_delete=models.PROTECT, verbose_name='Пользователь')
    status = models.CharField(max_length=50, blank=True, verbose_name='Статус юрист')
    comment = models.CharField(max_length=200, blank=True, verbose_name='Комментарий')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    class Meta:
        verbose_name = 'Судебный раздел'
        verbose_name_plural = 'Судебный раздел'