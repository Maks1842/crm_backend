from django.contrib import admin
from .models import *


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'department', 'position', 'birthday', 'is_deleted')
    search_fields = ('user', 'department', 'position', 'birthday', 'is_deleted')
    list_editable = ('user', 'department', 'position', 'birthday', 'is_deleted')
    list_filter = ('user', 'department', 'position', 'birthday', 'is_deleted')


class DepartmentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_deleted')
    search_fields = ('name', 'is_deleted')
    list_editable = ('name', 'is_deleted')
    list_filter = ('name', 'is_deleted')


class PositionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_deleted')
    search_fields = ('name', 'is_deleted')
    list_editable = ('name', 'is_deleted')
    list_filter = ('name', 'is_deleted')


class LibraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'list', 'comment', 'is_deleted')
    search_fields = ('name', 'list', 'comment', 'is_deleted')
    list_editable = ('name', 'list', 'comment', 'is_deleted')
    list_filter = ('name', 'list', 'comment', 'is_deleted')


class CessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number', 'date', 'summa', 'cedent', 'cessionari', 'date_old_cession', 'is_deleted')
    search_fields = ('name', 'number', 'date', 'summa', 'cedent', 'cessionari', 'date_old_cession', 'is_deleted')
    list_editable = ('name', 'number', 'date', 'summa', 'cedent', 'cessionari', 'date_old_cession', 'is_deleted')
    list_filter = ('name', 'number', 'date', 'summa', 'cedent', 'cessionari', 'date_old_cession', 'is_deleted')


class DebtorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_1', 'name_2', 'pol', 'birthday', 'place_of_birth', 'passport_series', 'passport_num',
                    'passport_date', 'passport_department', 'inn', 'snils', 'address_1', 'address_2', 'index_add_1',
                    'index_add_2', 'comment', 'is_deleted')
    search_fields = ('name_1', 'name_2', 'pol', 'birthday', 'place_of_birth', 'passport_series', 'passport_num',
                     'passport_date', 'passport_department', 'inn', 'snils', 'address_1', 'address_2', 'index_add_1',
                     'index_add_2', 'comment', 'is_deleted')
    list_editable = ('name_1', 'name_2', 'pol', 'birthday', 'place_of_birth', 'passport_series', 'passport_num',
                     'passport_date', 'passport_department', 'inn', 'snils', 'address_1', 'address_2', 'index_add_1',
                     'index_add_2', 'comment', 'is_deleted')
    list_filter = ('name_1', 'name_2', 'pol', 'birthday', 'place_of_birth', 'passport_series', 'passport_num',
                   'passport_date', 'passport_department', 'inn', 'snils', 'address_1', 'address_2', 'index_add_1',
                   'index_add_2', 'comment', 'is_deleted')


class CreditsAdmin(admin.ModelAdmin):
    list_display = ('id', 'creditor', 'number', 'date_start', 'date_ent', 'summa', 'interest_rate', 'overdue_od',
                    'overdue_percent', 'penalty', 'percent_of_od', 'gov_toll', 'debtor', 'cession', 'comment',
                    'is_deleted')
    search_fields = ('creditor', 'number', 'date_start', 'date_ent', 'summa', 'interest_rate', 'overdue_od',
                     'overdue_percent', 'penalty', 'percent_of_od', 'gov_toll', 'debtor', 'cession', 'comment',
                     'is_deleted')
    list_editable = ('creditor', 'number', 'date_start', 'date_ent', 'summa', 'interest_rate', 'overdue_od',
                     'overdue_percent', 'penalty', 'percent_of_od', 'gov_toll', 'debtor', 'cession', 'comment',
                     'is_deleted')
    list_filter = ('creditor', 'number', 'date_start', 'date_ent', 'summa', 'interest_rate', 'overdue_od',
                   'overdue_percent', 'penalty', 'percent_of_od', 'gov_toll', 'debtor', 'cession', 'comment',
                   'is_deleted')


class Executive_DocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_ed', 'number', 'date', 'case_number', 'date_of_receipt_ed', 'date_decision',
                    'status_ed', 'credit', 'user', 'comment', 'is_deleted')
    search_fields = ('type_ed', 'number', 'date', 'case_number', 'date_of_receipt_ed', 'date_decision',
                     'status_ed', 'credit', 'user', 'comment', 'is_deleted')
    list_editable = ('type_ed', 'number', 'date', 'case_number', 'date_of_receipt_ed', 'date_decision',
                     'status_ed', 'credit', 'user', 'comment', 'is_deleted')
    list_filter = ('type_ed', 'number', 'date', 'case_number', 'date_of_receipt_ed', 'date_decision',
                   'status_ed', 'credit', 'user', 'comment', 'is_deleted')


class Executive_ProductionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'date_on', 'date_end', 'reason_end', 'curent_debt',
                    'summa_debt', 'date_request', 'executive_document', 'comment', 'is_deleted')
    search_fields = ('number', 'date_on', 'date_end', 'reason_end', 'curent_debt',
                     'summa_debt', 'date_request', 'executive_document', 'comment', 'is_deleted')
    list_editable = ('number', 'date_on', 'date_end', 'reason_end', 'curent_debt',
                     'summa_debt', 'date_request', 'executive_document', 'comment', 'is_deleted')
    list_filter = ('number', 'date_on', 'date_end', 'reason_end', 'curent_debt',
                   'summa_debt', 'date_request', 'executive_document', 'comment', 'is_deleted')


class Collection_DebtAdmin(admin.ModelAdmin):
    list_display = ('id', 'department_of_presentation', 'name_department', 'address_department', 'executive_document',
                    'date_presentation', 'date_return', 'reason_end', 'comment', 'is_deleted')
    search_fields = ('department_of_presentation', 'name_department', 'address_department', 'executive_document',
                     'date_presentation', 'date_return', 'reason_end', 'comment', 'is_deleted')
    list_editable = ('department_of_presentation', 'name_department', 'address_department', 'executive_document',
                     'date_presentation', 'date_return', 'reason_end', 'comment', 'is_deleted')
    list_filter = ('department_of_presentation', 'name_department', 'address_department', 'executive_document',
                   'date_presentation', 'date_return', 'reason_end', 'comment', 'is_deleted')


class Data_from_ROSP_Execut_ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'debtor', 'date_on', 'date_end', 'reason_end', 'curent_debt', 'summa_debt',
                    'gov_toll', 'repay', 'object_ep', 'executive_document', 'rosp', 'address_rosp', 'pristav',
                    'pristav_phone', 'date_request')
    search_fields = ('number', 'debtor', 'date_on', 'date_end', 'reason_end', 'curent_debt', 'summa_debt',
                     'gov_toll', 'repay', 'object_ep', 'executive_document', 'rosp', 'address_rosp', 'pristav',
                     'pristav_phone', 'date_request')
    list_editable = ('number', 'debtor', 'date_on', 'date_end', 'reason_end', 'curent_debt', 'summa_debt',
                     'gov_toll', 'repay', 'object_ep', 'executive_document', 'rosp', 'address_rosp', 'pristav',
                     'pristav_phone', 'date_request')
    list_filter = ('number', 'debtor', 'date_on', 'date_end', 'reason_end', 'curent_debt', 'summa_debt',
                   'gov_toll', 'repay', 'object_ep', 'executive_document', 'rosp', 'address_rosp', 'pristav',
                   'pristav_phone', 'date_request')


# class PymentsAdmin(admin.ModelAdmin):
#     list_display = ('id', 'creditor', 'number', 'date_start', 'date_ent', 'summa', 'interest_rate', 'overdue_od',
#                     'overdue_percent', 'penalty', 'percent_of_od', 'gov_toll', 'debtor', 'cession', 'comment',
#                     'is_deleted')
#     search_fields = ()
#     list_editable = ()
#     list_filter = ()
#     debtor = models.ForeignKey('Debtors', blank=True, on_delete=models.PROTECT, verbose_name='Должник')
#     executive_document = models.ForeignKey('Executive_Documents', blank=True, on_delete=models.PROTECT, verbose_name='Испольнительный документ')
#     date = models.DateField(verbose_name='Дата платежа')
#     summa = models.FloatField(null=True, blank=True, verbose_name='Сумма платежа')
#     payment_doc_num = models.CharField(max_length=50, blank=True, verbose_name='Номер платежного документа')
#     comment = models.CharField(max_length=200, blank=True, verbose_name='Комментарий')
#     is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')
#
#     class Meta:
#         verbose_name = 'Платежи'
#
#
# class LegalAdmin(admin.ModelAdmin):
#     list_display = ('id', 'creditor', 'number', 'date_start', 'date_ent', 'summa', 'interest_rate', 'overdue_od',
#                     'overdue_percent', 'penalty', 'percent_of_od', 'gov_toll', 'debtor', 'cession', 'comment',
#                     'is_deleted')
#     search_fields = ()
#     list_editable = ()
#     list_filter = ()
#     debtor = models.ForeignKey('Debtors', blank=True, on_delete=models.PROTECT, verbose_name='Должник')
#     executive_document = models.ForeignKey('Executive_Documents', blank=True, on_delete=models.PROTECT, verbose_name='Испольнительный документ')
#     user = models.ForeignKey(User, blank=True, on_delete=models.PROTECT, verbose_name='Пользователь')
#     status = models.CharField(max_length=50, blank=True, verbose_name='Статус юрист')
#     comment = models.CharField(max_length=200, blank=True, verbose_name='Комментарий')
#     is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')
#
#     class Meta:
#         verbose_name = 'Судебный раздел'
#
#
# class Mail_InAdmin(admin.ModelAdmin):
#     list_display = ('id', )
#     search_fields = ()
#     list_editable = ()
#     list_filter = ()
#     sequence_num = models.IntegerField(verbose_name='Порядковый номер')
#     debtor = models.ForeignKey('Debtors', blank=True, on_delete=models.PROTECT, verbose_name='Должник')
#     status_ed = models.CharField(max_length=50, blank=True, verbose_name='Статус ИД')
#     date = models.DateField(verbose_name='Дата корреспонденции')
#     addresser = models.CharField(max_length=100, verbose_name='От кого')
#     name_doc = models.CharField(max_length=100, verbose_name='Наименование документа')
#     legal = models.ForeignKey('Legal', blank=True, on_delete=models.PROTECT, verbose_name='Судебка')
#     comment = models.CharField(max_length=200, blank=True, verbose_name='Комментарий')
#     is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')
#
#     class Meta:
#         verbose_name = 'Входящая корреспонденция'
#
#
# class Mail_OutAdmin(admin.ModelAdmin):
#     list_display = ('id', )
#     search_fields = ()
#     list_editable = ()
#     list_filter = ()
#     sequence_num = models.IntegerField(verbose_name='Порядковый номер')
#     executive_document = models.ForeignKey('Executive_Documents', blank=True, on_delete=models.PROTECT, verbose_name='Испольнительный документ')
#     date = models.DateField(verbose_name='Дата корреспонденции')
#     name_doc = models.CharField(max_length=100, verbose_name='Наименование документа')
#     addresser = models.CharField(max_length=100, verbose_name='Адресат')
#     recipient_organisation = models.CharField(max_length=200, verbose_name='Компания получателя получателя')
#     recipient_address = models.CharField(max_length=200, verbose_name='Адрес получателя')
#     recipient_index = models.CharField(max_length=200, verbose_name='Индекс получателя')
#     mass = models.FloatField(null=True, blank=True, verbose_name='Масса отправления')
#     gov_toll = models.FloatField(null=True, blank=True, verbose_name='Госпошлина')
#     trek = models.CharField(max_length=20, blank=True, verbose_name='Трек номер')
#     type_mail = models.CharField(max_length=20, verbose_name='Тип отправления')
#     type_package = models.CharField(max_length=20, verbose_name='Тип конверта')
#     type_mark = models.CharField(max_length=20, verbose_name='Тип марки')
#     num_symbol = models.IntegerField(null=True, blank=True, verbose_name='Количество символов')
#     debtor = models.ForeignKey('Debtors', blank=True, on_delete=models.PROTECT, verbose_name='Должник')
#     user = models.ForeignKey(User, blank=True, on_delete=models.PROTECT, verbose_name='Пользователь')
#     comment = models.CharField(max_length=200, blank=True, verbose_name='Комментарий')
#     is_deleted = models.BooleanField(default=False, verbose_name='Признак удаления')
#
#     class Meta:
#         verbose_name = 'Исходящая корреспонденция'
#
#
# class Transaction_ExchangeAdmin(admin.ModelAdmin):
#     list_display = ('id', )
#     search_fields = ()
#     list_editable = ()
#     list_filter = ()
#     model = models.CharField(max_length=50, verbose_name='Модель')
#     field = models.CharField(max_length=50, verbose_name='Поле')
#     old_data = models.CharField(max_length=2000, verbose_name='Старые данные')
#     new_data = models.CharField(max_length=2000, verbose_name='Новые данные')
#     date_exchange = models.DateTimeField(auto_now_add=True, verbose_name='Дата изменения данных')
#     user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Пользователь')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Departments, DepartmentsAdmin)
admin.site.register(Positions, PositionsAdmin)
admin.site.register(Library, LibraryAdmin)
admin.site.register(Cession, CessionAdmin)
admin.site.register(Debtors, DebtorsAdmin)
admin.site.register(Credits, CreditsAdmin)
admin.site.register(Executive_Documents, Executive_DocumentsAdmin)
admin.site.register(Executive_Productions, Executive_ProductionsAdmin)
admin.site.register(Collection_Debt, Collection_DebtAdmin)
admin.site.register(Data_from_ROSP_Execut_Product, Data_from_ROSP_Execut_ProductAdmin)
