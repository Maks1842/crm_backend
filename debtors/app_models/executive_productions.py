from django.db import models


'''Первичный запрос в РОСП об исполнительном производстве.
   Данные хранятся до окончания взыскания долга'''


class Executive_Productions(models.Model):
    number = models.CharField(max_length=50, blank=True, verbose_name='Номер исполнительного производства')
    date_on = models.DateField(blank=True, verbose_name='Дата начала ИП')
    date_end = models.DateField(blank=True, verbose_name='Дата окончания ИП')
    reason_end = models.CharField(max_length=50, blank=True, verbose_name='Причина окончания')
    curent_debt = models.FloatField(null=True, blank=True, verbose_name='Текущая задолженность')
    summa_debt = models.FloatField(null=True, blank=True, verbose_name='Основной долг')
    date_request = models.DateField(blank=True, verbose_name='Дата получения данных из РОСП')
    executive_document = models.ForeignKey('Executive_Documents', blank=True, on_delete=models.PROTECT, verbose_name='Испольнительный документ')
    comment = models.CharField(max_length=200, blank=True, verbose_name='Комментарий')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Испольнительное производство'
        verbose_name_plural = 'Исполнительные производства'
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'number',
                ],
                name="unique_ep")
        ]