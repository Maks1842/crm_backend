from django.db import models


class Mail_In(models.Model):
    sequence_num = models.IntegerField(verbose_name='Порядковый номер')
    debtor = models.ForeignKey('Debtors', blank=True, on_delete=models.PROTECT, verbose_name='Должник')
    status_ed = models.CharField(max_length=50, blank=True, verbose_name='Статус ИД')
    date = models.DateField(verbose_name='Дата корреспонденции')
    addresser = models.CharField(max_length=100, verbose_name='От кого')
    name_doc = models.CharField(max_length=100, verbose_name='Наименование документа')
    legal = models.ForeignKey('Legal', blank=True, on_delete=models.PROTECT, verbose_name='Судебка')
    comment = models.CharField(max_length=200, blank=True, verbose_name='Комментарий')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    class Meta:
        verbose_name = 'Входящая корреспонденция'
        verbose_name_plural = 'Входящая корреспонденция'
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'sequence_num',
                ],
                name="unique_mail_in")
        ]