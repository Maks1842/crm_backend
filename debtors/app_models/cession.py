from django.db import models


class Cession(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name='Наименование цессии')
    number = models.CharField(max_length=50, blank=True, verbose_name='Номер цессии')
    date = models.DateField(null=True, blank=True, verbose_name='Дата цессии')
    summa = models.FloatField(null=True, blank=True, verbose_name='Сумма цессии')
    cedent = models.CharField(max_length=100, blank=True, verbose_name='Цедент')
    cessionari = models.CharField(max_length=100, blank=True, verbose_name='Цессионарий')
    date_old_cession = models.CharField(max_length=100, blank=True, verbose_name='Даты предыдущих цессий')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цессия'
        verbose_name_plural = 'Цессии'
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'name',
                    'number'
                ],
                name="unique_cession")
        ]