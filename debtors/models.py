from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name='Пользователь')
    department = models.ForeignKey('Departments', blank=True, on_delete=models.PROTECT, verbose_name='Подразделение')
    position = models.ForeignKey('Positions', blank=True, on_delete=models.PROTECT, verbose_name='Должность')
    birthday = models.DateField(null=True, blank=True, verbose_name='День рождения')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'


class Departments(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name='Подразделение')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class Positions(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name='Должность')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Library(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование списка')
    list = models.JSONField(verbose_name='список')
    comment = models.CharField(max_length=100, blank=True, verbose_name='Комментарий')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Библиотека'
        verbose_name_plural = 'Библиотека'


class Cession(models.Model):
    name = models.CharField(max_length=50, blank=True, verbose_name='Наименование цессии')
    number = models.CharField(max_length=50, blank=True, verbose_name='Номер цессии')
    date = models.DateField(verbose_name='Дата цессии')
    summa = models.FloatField(null=True, blank=True, verbose_name='Сумма цессии')
    cedent = models.CharField(max_length=100, blank=True, verbose_name='Цедент')
    cessionari = models.CharField(max_length=100, blank=True, verbose_name='Цессионарий')
    date_old_cession = models.DateField(max_length=100, blank=True, verbose_name='Даты предыдущих цессий')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Цессия'
        verbose_name_plural = 'Цессии'


class Debtors(models.Model):
    name_1 = models.CharField(max_length=100, verbose_name='Имя должника (по договору)')
    name_2 = models.CharField(max_length=100, blank=True, verbose_name='Имя должника (изменения)')
    pol = models.CharField(max_length=20, blank=True, verbose_name='Пол')
    birthday = models.DateField(blank=True, verbose_name='Дата рождения')
    place_of_birth = models.CharField(max_length=200, blank=True, verbose_name='Место рождения')
    passport_series = models.IntegerField(null=True, blank=True, verbose_name='Серия паспорта')
    passport_num = models.IntegerField(null=True, blank=True, verbose_name='Номер паспорта')
    passport_date = models.DateField(blank=True, verbose_name='Дата выдачи паспорта')
    passport_department = models.CharField(max_length=100, blank=True, verbose_name='Кем выдан паспорт')
    inn = models.CharField(max_length=12, blank=True, verbose_name='ИНН')
    snils = models.CharField(max_length=14, blank=True, verbose_name='СНИЛС')
    address_1 = models.CharField(max_length=200, blank=True, verbose_name='Адрес прописки')
    address_2 = models.CharField(max_length=200, blank=True, verbose_name='Адрес проживания')
    index_add_1 = models.CharField(max_length=6, blank=True, verbose_name='Индекс прописки')
    index_add_2 = models.CharField(max_length=6, blank=True, verbose_name='Индекс проживания')
    comment = models.CharField(max_length=200, blank=True, verbose_name='Комментарий')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    def __str__(self):
        return self.name_1

    class Meta:
        verbose_name = 'Должник'
        verbose_name_plural = 'Должники'


class Credits(models.Model):
    creditor = models.CharField(max_length=100, verbose_name='Кредитор')
    number = models.CharField(max_length=50, blank=True, verbose_name='Номер кредитного договора')
    date_start = models.DateField(verbose_name='Дата выдычи КД')
    date_ent = models.CharField(max_length=100, blank=True, verbose_name='Срок КД')
    summa = models.FloatField(null=True, blank=True, verbose_name='Сумма КД')
    interest_rate = models.FloatField(null=True, blank=True, verbose_name='Процентная ставка по КД')
    overdue_od = models.FloatField(null=True, blank=True, verbose_name='Просроченный ОД')
    overdue_percent = models.FloatField(null=True, blank=True, verbose_name='Просроченные проценты')
    penalty = models.FloatField(null=True, blank=True, verbose_name='Штрафы, пени')
    percent_of_od = models.FloatField(null=True, blank=True, verbose_name='Проценты на ОД')
    gov_toll = models.FloatField(null=True, blank=True, verbose_name='Госпошлина')
    debtor = models.ForeignKey('Debtors', blank=True, on_delete=models.PROTECT, verbose_name='Должник')
    cession = models.ForeignKey('Cession', blank=True, on_delete=models.PROTECT, verbose_name='Цессия')
    comment = models.CharField(max_length=200, blank=True, verbose_name='Комментарий')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Кредит'
        verbose_name_plural = 'Кредиты'


class Executive_Documents(models.Model):
    type_ed = models.CharField(max_length=50, blank=True, verbose_name='Тип ИД')
    number = models.CharField(max_length=50, blank=True, verbose_name='Номер ИД')
    date = models.DateField(verbose_name='Дата ИД')
    case_number = models.CharField(max_length=100, blank=True, verbose_name='Номер дела')
    date_of_receipt_ed = models.DateField(verbose_name='Дата выдачи ИД')
    date_decision = models.DateField(verbose_name='Дата принятия решения')
    status_ed = models.CharField(max_length=50, blank=True, verbose_name='Статус ИД')
    credit = models.ForeignKey('Credits', blank=True, on_delete=models.PROTECT, verbose_name='Кредитный договор')
    user = models.ForeignKey(User, blank=True, on_delete=models.PROTECT, verbose_name='Пользователь')
    comment = models.CharField(max_length=200, blank=True, verbose_name='Комментарий')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    def __str__(self):
        return self.type_ed

    class Meta:
        verbose_name = 'Испольнительный документ'
        verbose_name_plural = 'Исполнительные документы'


'''Первичный запрос в РОСП об исполнительном производстве.
   Данные хранятся до окончания взыскания долга'''
class Executive_Productions(models.Model):
    number = models.CharField(max_length=50, blank=True, verbose_name='Номер исполнительного производства')
    date_on = models.DateField(blank=True, verbose_name='Дата начала ИП')
    date_end = models.DateField(blank=True, verbose_name='Дата окончания ИП')
    reason_end = models.CharField(max_length=50, blank=True, verbose_name='Причина окончания')
    curent_debt = models.FloatField(null=True, blank=True, verbose_name='Текущая задолженность')
    summa_debt = models.FloatField(null=True, blank=True, verbose_name='Основной долг')
    date_request = models.DateField(blank=True, verbose_name='Дата получения данных из РОСП')
    executive_document = models.ForeignKey('Executive_Documents', blank=True, on_delete=models.PROTECT, verbose_name='Испольнительный документ')
    comment = models.CharField(max_length=200, blank=True, verbose_name='Комментарий')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Испольнительное производство'
        verbose_name_plural = 'Исполнительные производства'


'''Информация о движении исполнительного документа'''
class Collection_Debt(models.Model):
    department_of_presentation = models.CharField(max_length=50, blank=True, verbose_name='Тип учреждение предъявления')
    name_department = models.CharField(max_length=50, blank=True, verbose_name='Наименование учреждение предъявления')
    address_department = models.CharField(max_length=200, blank=True, verbose_name='Адрес учреждение предъявления')
    executive_document = models.ForeignKey('Executive_Documents', blank=True, on_delete=models.PROTECT, verbose_name='Испольнительный документ')
    date_presentation = models.DateField(blank=True, verbose_name='Дата предъявления ИД')
    date_return = models.DateField(blank=True, verbose_name='Дата возврата ИД')
    reason_end = models.CharField(max_length=50, blank=True, verbose_name='Причина возврата ИД')
    comment = models.CharField(max_length=200, blank=True, verbose_name='Комментарий')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    class Meta:
        verbose_name = 'Взыскание долга'
        verbose_name_plural = 'Взыскание долга'


'''Регулярные запросы в РОСП о статусе исполнительного производства.
   Сохраняются последние два запроса. Все предыдущие автоматичесви удаляются.'''
class Data_from_ROSP_Execut_Product(models.Model):
    number = models.CharField(max_length=50, verbose_name='Номер исполнительного производства')
    debtor = models.CharField(max_length=100, blank=True, verbose_name='Должник')
    date_on = models.DateField(verbose_name='Дата начала ИП')
    date_end = models.DateField(blank=True, verbose_name='Дата окончания ИП')
    reason_end = models.CharField(max_length=50, blank=True, verbose_name='Причина окончания')
    curent_debt = models.FloatField(null=True, blank=True, verbose_name='Текущая задолженность')
    summa_debt = models.FloatField(null=True, blank=True, verbose_name='Основной долг')
    gov_toll = models.FloatField(null=True, blank=True, verbose_name='Исполниетельский сбор')
    repay = models.FloatField(null=True, blank=True, verbose_name='Погашеная часть')
    object_ep = models.CharField(max_length=100, blank=True, verbose_name='Предмет исполнительного производства')
    executive_document = models.CharField(max_length=100, blank=True, verbose_name='Испольнительный документ')
    rosp = models.CharField(max_length=50, blank=True, verbose_name='РОСП')
    address_rosp = models.CharField(max_length=200, blank=True, verbose_name='Адрес РОСП')
    pristav = models.CharField(max_length=50, blank=True, verbose_name='Пристав')
    pristav_phone = models.CharField(max_length=50, blank=True, verbose_name='Телефон пристава')
    date_request = models.DateField(verbose_name='Дата получения данных из РОСП')

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Данные из РОСП об ИП'
        verbose_name_plural = 'Данные из РОСП об ИП'


class Pyments(models.Model):
    debtor = models.ForeignKey('Debtors', blank=True, on_delete=models.PROTECT, verbose_name='Должник')
    executive_document = models.ForeignKey('Executive_Documents', blank=True, on_delete=models.PROTECT, verbose_name='Испольнительный документ')
    date = models.DateField(verbose_name='Дата платежа')
    summa = models.FloatField(null=True, blank=True, verbose_name='Сумма платежа')
    payment_doc_num = models.CharField(max_length=50, blank=True, verbose_name='Номер платежного документа')
    comment = models.CharField(max_length=200, blank=True, verbose_name='Комментарий')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    class Meta:
        verbose_name = 'Платежи'
        verbose_name_plural = 'Платежи'


class Legal(models.Model):
    debtor = models.ForeignKey('Debtors', blank=True, on_delete=models.PROTECT, verbose_name='Должник')
    executive_document = models.ForeignKey('Executive_Documents', blank=True, on_delete=models.PROTECT, verbose_name='Испольнительный документ')
    user = models.ForeignKey(User, blank=True, on_delete=models.PROTECT, verbose_name='Пользователь')
    status = models.CharField(max_length=50, blank=True, verbose_name='Статус юрист')
    comment = models.CharField(max_length=200, blank=True, verbose_name='Комментарий')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    class Meta:
        verbose_name = 'Судебный раздел'
        verbose_name_plural = 'Судебный раздел'


class Mail_In(models.Model):
    sequence_num = models.IntegerField(verbose_name='Порядковый номер')
    debtor = models.ForeignKey('Debtors', blank=True, on_delete=models.PROTECT, verbose_name='Должник')
    status_ed = models.CharField(max_length=50, blank=True, verbose_name='Статус ИД')
    date = models.DateField(verbose_name='Дата корреспонденции')
    addresser = models.CharField(max_length=100, verbose_name='От кого')
    name_doc = models.CharField(max_length=100, verbose_name='Наименование документа')
    legal = models.ForeignKey('Legal', blank=True, on_delete=models.PROTECT, verbose_name='Судебка')
    comment = models.CharField(max_length=200, blank=True, verbose_name='Комментарий')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    class Meta:
        verbose_name = 'Входящая корреспонденция'
        verbose_name_plural = 'Входящая корреспонденция'


class Mail_Out(models.Model):
    sequence_num = models.IntegerField(verbose_name='Порядковый номер')
    executive_document = models.ForeignKey('Executive_Documents', blank=True, on_delete=models.PROTECT, verbose_name='Испольнительный документ')
    date = models.DateField(verbose_name='Дата корреспонденции')
    name_doc = models.CharField(max_length=100, verbose_name='Наименование документа')
    addresser = models.CharField(max_length=100, verbose_name='Адресат')
    recipient_organisation = models.CharField(max_length=200, verbose_name='Компания получателя получателя')
    recipient_address = models.CharField(max_length=200, verbose_name='Адрес получателя')
    recipient_index = models.CharField(max_length=200, verbose_name='Индекс получателя')
    mass = models.FloatField(null=True, blank=True, verbose_name='Масса отправления')
    gov_toll = models.FloatField(null=True, blank=True, verbose_name='Госпошлина')
    trek = models.CharField(max_length=20, blank=True, verbose_name='Трек номер')
    type_mail = models.CharField(max_length=20, verbose_name='Тип отправления')
    type_package = models.CharField(max_length=20, verbose_name='Тип конверта')
    type_mark = models.CharField(max_length=20, verbose_name='Тип марки')
    num_symbol = models.IntegerField(null=True, blank=True, verbose_name='Количество символов')
    debtor = models.ForeignKey('Debtors', blank=True, on_delete=models.PROTECT, verbose_name='Должник')
    user = models.ForeignKey(User, blank=True, on_delete=models.PROTECT, verbose_name='Пользователь')
    comment = models.CharField(max_length=200, blank=True, verbose_name='Комментарий')
    is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')

    class Meta:
        verbose_name = 'Исходящая корреспонденция'
        verbose_name_plural = 'Исходящая корреспонденция'


class Transaction_Exchange(models.Model):
    model = models.CharField(max_length=50, verbose_name='Модель')
    field = models.CharField(max_length=50, verbose_name='Поле')
    old_data = models.CharField(max_length=2000, verbose_name='Старые данные')
    new_data = models.CharField(max_length=2000, verbose_name='Новые данные')
    date_exchange = models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения данных')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')

    class Meta:
        verbose_name = 'Регистрация изменения данных'
        verbose_name_plural = 'Регистрация изменения данных'




