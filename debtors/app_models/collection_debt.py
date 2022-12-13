from django.db import models


'''Информация о движении исполнительного документа'''


class Collection_Debt(models.Model):
    department_of_presentation = models.CharField(max_length=50, blank=True, verbose_name='Тип учреждение предъявления')
    name_department = models.CharField(max_length=50, blank=True, verbose_name='Наименование учреждение предъявления')
    address_department = models.CharField(max_length=200, blank=True, verbose_name='Адрес учреждение предъявления')
    executive_document = models.ForeignKey('Executive_Documents', blank=True, on_delete=models.PROTECT, verbose_name='Испольнительный документ')
    date_presentation = models.DateField(null=True, blank=True, verbose_name='Дата предъявления ИД')
    date_return = models.DateField(null=True, blank=True, verbose_name='Дата возврата ИД')
    reason_end = models.CharField(max_length=50, blank=True, verbose_name='Причина возврата ИД')
    comment = models.CharField(max_length=200, blank=True, verbose_name='Комментарий')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    class Meta:
        verbose_name = 'Взыскание долга'
        verbose_name_plural = 'Взыскание долга'