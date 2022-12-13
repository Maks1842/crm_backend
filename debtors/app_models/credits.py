from django.db import models


class Credits(models.Model):
    creditor = models.CharField(max_length=100, verbose_name='Кредитор')
    number = models.CharField(max_length=50, blank=True, verbose_name='Номер кредитного договора')
    date_start = models.DateField(verbose_name='Дата выдычи КД')
    date_end = models.CharField(max_length=100, blank=True, verbose_name='Срок КД')
    summa = models.FloatField(null=True, blank=True, verbose_name='Сумма КД')
    interest_rate = models.FloatField(null=True, blank=True, verbose_name='Процентная ставка по КД')
    overdue_od = models.FloatField(null=True, blank=True, verbose_name='Просроченный ОД')
    overdue_percent = models.FloatField(null=True, blank=True, verbose_name='Просроченные проценты')
    penalty = models.FloatField(null=True, blank=True, verbose_name='Штрафы, пени')
    percent_of_od = models.FloatField(null=True, blank=True, verbose_name='Проценты на ОД')
    gov_toll = models.FloatField(null=True, blank=True, verbose_name='Госпошлина')
    debtor = models.ForeignKey('Debtors', blank=True, on_delete=models.PROTECT, verbose_name='Должник')
    cession = models.ForeignKey('Cession', blank=True, on_delete=models.PROTECT, verbose_name='Цессия')
    comment = models.CharField(max_length=200, blank=True, verbose_name='Комментарий')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'creditor',
                    'number',
                ],
                name="unique_credits")
        ]