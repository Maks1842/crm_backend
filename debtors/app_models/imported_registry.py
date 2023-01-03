from django.db import models


class Imported_Registry(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование импортируемого реестра')
    date = models.DateField(null=True, verbose_name='Дата импорта')
    registry = models.JSONField(verbose_name='Реестр')
    comment = models.CharField(max_length=100, blank=True, verbose_name='Комментарий')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Импортируемый реестр'
        verbose_name_plural = 'Импортируемые реестры'
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "name",
                ],
                name="unique_imported_registry")
        ]