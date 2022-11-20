from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    department = models.ForeignKey('Departments', blank=True, on_delete=models.PROTECT, verbose_name='Подразделение')
    position = models.ForeignKey('Positions', blank=True, on_delete=models.PROTECT, verbose_name='Должность')
    birthday = models.DateField(null=True, blank=True, verbose_name='День рождения')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Departments(models.Model):
    name = models.TextField(max_length=50, blank=True, verbose_name='Подразделение')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class Positions(models.Model):
    name = models.TextField(max_length=50, blank=True, verbose_name='Должность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'
