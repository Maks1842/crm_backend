from django.db import models

class Departments(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name='Подразделение')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "name",
                ],
                name="unique_departments")
        ]