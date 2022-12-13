from django.db import models


'''Регулярные запросы в РОСП о статусе исполнительного производства.
   Сохраняются последние два запроса. Все предыдущие автоматичесви удаляются.'''


class Data_from_ROSP_Execut_Product(models.Model):
    number = models.CharField(max_length=50, verbose_name='Номер исполнительного производства')
    debtor = models.CharField(max_length=100, blank=True, verbose_name='Должник')
    date_on = models.DateField(verbose_name='Дата возбуждения ИП')
    date_end = models.DateField(null=True, blank=True, verbose_name='Дата окончания ИП')
    reason_end = models.CharField(max_length=50, blank=True, verbose_name='Причина окончания')
    curent_debt = models.FloatField(null=True, blank=True, verbose_name='Текущая задолженность')
    summa_debt = models.FloatField(null=True, blank=True, verbose_name='Основной долг')
    gov_toll = models.FloatField(null=True, blank=True, verbose_name='Исполниетельский сбор')
    repay = models.FloatField(null=True, blank=True, verbose_name='Погашеная часть')
    object_ep = models.CharField(max_length=100, blank=True, verbose_name='Предмет исполнительного производства')
    executive_document = models.CharField(max_length=100, blank=True, verbose_name='Испольнительный документ')
    rosp = models.CharField(max_length=50, blank=True, verbose_name='РОСП')
    address_rosp = models.CharField(max_length=200, blank=True, verbose_name='Адрес РОСП')
    pristav = models.CharField(max_length=50, blank=True, verbose_name='Пристав')
    pristav_phone = models.CharField(max_length=50, blank=True, verbose_name='Телефон пристава')
    date_request = models.DateField(verbose_name='Дата получения данных из РОСП')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Данные из РОСП об ИП'
        verbose_name_plural = 'Данные из РОСП об ИП'