from django.db import models


class Registry_Headers(models.Model):
    headers = models.CharField(max_length=100, verbose_name='Заголовок столбца в таблице frontend')
    headers_key = models.CharField(max_length=100, verbose_name='Ключ заголовка столбца')
    model = models.CharField(max_length=50, verbose_name='Наименование модели БД')
    name_field = models.CharField(max_length=50, verbose_name='Наименование поля в Модели')
    turn = models.IntegerField(null=True, verbose_name='Номер очередности')
    width_field = models.IntegerField(null=True, blank=True, verbose_name='Ширина столбца')
    redactor = models.CharField(max_length=20, default='1', verbose_name='Кто может редактировать')

    def __str__(self):
        return self.headers

    class Meta:
        verbose_name = 'Заголовок столбцов реестра'
        verbose_name_plural = 'Заголовки столбцов реестра'
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "headers",
                    "headers_key",
                    "turn"
                ],
                name="unique_registry_headers")
        ]