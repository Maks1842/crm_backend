from django.db import models


class Positions(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name='Должность')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "name",
                ],
                name="unique_positions")
        ]