from django.contrib.auth.models import User
from django.db import models


class Mail_Out(models.Model):
    sequence_num = models.IntegerField(verbose_name='Порядковый номер')
    executive_document = models.ForeignKey('Executive_Documents', blank=True, on_delete=models.PROTECT, verbose_name='Испольнительный документ')
    date = models.DateField(verbose_name='Дата корреспонденции')
    name_doc = models.CharField(max_length=100, verbose_name='Наименование документа')
    addresser = models.CharField(max_length=100, verbose_name='Адресат')
    recipient_organisation = models.CharField(max_length=200, verbose_name='Компания получателя получателя')
    recipient_address = models.CharField(max_length=200, verbose_name='Адрес получателя')
    recipient_index = models.CharField(max_length=200, verbose_name='Индекс получателя')
    mass = models.FloatField(null=True, blank=True, verbose_name='Масса отправления')
    gov_toll = models.FloatField(null=True, blank=True, verbose_name='Госпошлина')
    trek = models.CharField(max_length=20, blank=True, verbose_name='Трек номер')
    type_mail = models.CharField(max_length=20, verbose_name='Тип отправления')
    type_package = models.CharField(max_length=20, verbose_name='Тип конверта')
    type_mark = models.CharField(max_length=20, verbose_name='Тип марки')
    num_symbol = models.IntegerField(null=True, blank=True, verbose_name='Количество символов')
    debtor = models.ForeignKey('Debtors', blank=True, on_delete=models.PROTECT, verbose_name='Должник')
    user = models.ForeignKey(User, blank=True, on_delete=models.PROTECT, verbose_name='Пользователь')
    comment = models.CharField(max_length=200, blank=True, verbose_name='Комментарий')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    class Meta:
        verbose_name = 'Исходящая корреспонденция'
        verbose_name_plural = 'Исходящая корреспонденция'
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'sequence_num',
                ],
                name="unique_mail_out")
        ]