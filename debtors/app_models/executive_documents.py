from django.contrib.auth.models import User
from django.db import models


class Executive_Documents(models.Model):
    type_ed = models.CharField(max_length=50, blank=True, verbose_name='Тип ИД')
    number = models.CharField(max_length=50, blank=True, verbose_name='Номер ИД')
    date = models.DateField(verbose_name='Дата ИД')
    case_number = models.CharField(max_length=100, blank=True, verbose_name='Номер дела')
    date_of_receipt_ed = models.DateField(null=True, blank=True, verbose_name='Дата выдачи ИД')
    date_decision = models.DateField(verbose_name='Дата принятия решения')
    status_ed = models.CharField(max_length=50, blank=True, verbose_name='Статус ИД')
    credit = models.ForeignKey('Credits', blank=True, on_delete=models.PROTECT, verbose_name='Кредитный договор')
    user = models.ForeignKey(User, blank=True, on_delete=models.PROTECT, verbose_name='Пользователь')
    comment = models.CharField(max_length=200, blank=True, verbose_name='Комментарий')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Испольнительный документ'
        verbose_name_plural = 'Исполнительные документы'
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'number',
                    'date',
                    'case_number',
                ],
                name="unique_ed")
        ]