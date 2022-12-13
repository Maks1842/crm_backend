from django.db import models


class Debtors(models.Model):
    last_name_1 = models.CharField(max_length=20, null=True,  verbose_name='Фамилия должника (по договору)')
    first_name_1 = models.CharField(max_length=20, null=True,  verbose_name='Имя должника (по договору)')
    second_name_1 = models.CharField(max_length=20, null=True,  verbose_name='Отчество должника (по договору)')
    last_name_2 = models.CharField(max_length=20, null=True,  blank=True, verbose_name='Фамилия должника (изменения)')
    first_name_2 = models.CharField(max_length=20, null=True,  blank=True, verbose_name='Имя должника (изменения)')
    second_name_2 = models.CharField(max_length=20, null=True,  blank=True, verbose_name='Отчество должника (изменения)')
    pol = models.CharField(max_length=20, blank=True, verbose_name='Пол')
    birthday = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    place_of_birth = models.CharField(max_length=200, blank=True, verbose_name='Место рождения')
    passport_series = models.IntegerField(null=True, blank=True, verbose_name='Серия паспорта')
    passport_num = models.IntegerField(null=True, blank=True, verbose_name='Номер паспорта')
    passport_date = models.DateField(null=True, blank=True, verbose_name='Дата выдачи паспорта')
    passport_department = models.CharField(max_length=100, null=True,  blank=True, verbose_name='Кем выдан паспорт')
    inn = models.CharField(max_length=12, null=True,  blank=True, verbose_name='ИНН')
    snils = models.CharField(max_length=14, null=True,  blank=True, verbose_name='СНИЛС')
    address_1 = models.CharField(max_length=200, null=True, blank=True, verbose_name='Адрес прописки')
    address_2 = models.CharField(max_length=200, null=True, blank=True, verbose_name='Адрес проживания')
    index_add_1 = models.CharField(max_length=6, null=True, blank=True, verbose_name='Индекс прописки')
    index_add_2 = models.CharField(max_length=6, null=True, blank=True, verbose_name='Индекс проживания')
    comment = models.CharField(max_length=200, null=True, blank=True, verbose_name='Комментарий')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    def __str__(self):
        return f"{self.last_name_1} {self.first_name_1} {self.second_name_1 or ''}"

    class Meta:
        verbose_name = 'Должник'
        verbose_name_plural = 'Должники'
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'last_name_1',
                    'first_name_1',
                    'second_name_1',
                    'birthday',
                ],
                name="unique_debtors")
        ]