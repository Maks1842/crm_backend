from django.db import models


class Library(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование списка')
    list = models.JSONField(verbose_name='Список')
    comment = models.CharField(max_length=100, blank=True, verbose_name='Комментарий')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Библиотека'
        verbose_name_plural = 'Библиотека'
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "name",
                ],
                name="unique_library")
        ]