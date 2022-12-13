from django.db import models


class Pyments(models.Model):
    debtor = models.ForeignKey('Debtors', blank=True, on_delete=models.PROTECT, verbose_name='Должник')
    executive_document = models.ForeignKey('Executive_Documents', blank=True, on_delete=models.PROTECT, verbose_name='Испольнительный документ')
    date = models.DateField(verbose_name='Дата платежа')
    summa = models.FloatField(verbose_name='Сумма платежа')
    payment_doc_num = models.CharField(max_length=50, blank=True, verbose_name='Номер платежного документа')
    comment = models.CharField(max_length=200, blank=True, verbose_name='Комментарий')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    class Meta:
        verbose_name = 'Платежи'
        verbose_name_plural = 'Платежи'