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


class PymentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'debtor', 'executive_document', 'date', 'summa', 'payment_doc_num', 'comment', 'is_deleted')
    search_fields = ('debtor', 'executive_document', 'date', 'summa', 'payment_doc_num', 'comment', 'is_deleted')
    list_editable = ('debtor', 'executive_document', 'date', 'summa', 'payment_doc_num', 'comment', 'is_deleted')
    list_filter = ('debtor', 'executive_document', 'date', 'summa', 'payment_doc_num', 'comment', 'is_deleted')


class LegalAdmin(admin.ModelAdmin):
    list_display = ('id', 'debtor', 'executive_document', 'user', 'status', 'comment', 'is_deleted')
    search_fields = ('debtor', 'executive_document', 'user', 'status', 'comment', 'is_deleted')
    list_editable = ('debtor', 'executive_document', 'user', 'status', 'comment', 'is_deleted')
    list_filter = ('debtor', 'executive_document', 'user', 'status', 'comment', 'is_deleted')


class Mail_InAdmin(admin.ModelAdmin):
    list_display = ('id', 'sequence_num', 'debtor', 'status_ed', 'date', 'addresser', 'name_doc', 'legal', 'comment', 'is_deleted')
    search_fields = ('sequence_num', 'debtor', 'status_ed', 'date', 'addresser', 'name_doc', 'legal', 'comment', 'is_deleted')
    list_editable = ('sequence_num', 'debtor', 'status_ed', 'date', 'addresser', 'name_doc', 'legal', 'comment', 'is_deleted')
    list_filter = ('sequence_num', 'debtor', 'status_ed', 'date', 'addresser', 'name_doc', 'legal', 'comment', 'is_deleted')


class Mail_OutAdmin(admin.ModelAdmin):
    list_display = ('id', 'sequence_num', 'executive_document', 'date', 'name_doc', 'addresser', 'recipient_organisation',
                    'recipient_address', 'recipient_index', 'mass', 'gov_toll', 'trek', 'type_mail', 'type_package',
                    'type_mark', 'num_symbol', 'debtor', 'user', 'comment', 'is_deleted')
    search_fields = ('sequence_num', 'executive_document', 'date', 'name_doc', 'addresser', 'recipient_organisation',
                     'recipient_address', 'recipient_index', 'mass', 'gov_toll', 'trek', 'type_mail', 'type_package',
                     'type_mark', 'num_symbol', 'debtor', 'user', 'comment', 'is_deleted')
    list_editable = ('sequence_num', 'executive_document', 'date', 'name_doc', 'addresser', 'recipient_organisation',
                     'recipient_address', 'recipient_index', 'mass', 'gov_toll', 'trek', 'type_mail', 'type_package',
                     'type_mark', 'num_symbol', 'debtor', 'user', 'comment', 'is_deleted')
    list_filter = ('sequence_num', 'executive_document', 'date', 'name_doc', 'addresser', 'recipient_organisation',
                   'recipient_address', 'recipient_index', 'mass', 'gov_toll', 'trek', 'type_mail', 'type_package',
                   'type_mark', 'num_symbol', 'debtor', 'user', 'comment', 'is_deleted')


class Transaction_ExchangeAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'field', 'old_data', 'new_data', 'date_exchange', 'user')
    search_fields = ('model', 'field', 'old_data', 'new_data', 'user')
    list_editable = ('model', 'field', 'old_data', 'new_data', 'user')
    list_filter = ('model', 'field', 'old_data', 'new_data', 'user')


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
admin.site.register(Pyments, PymentsAdmin)
admin.site.register(Legal, LegalAdmin)
admin.site.register(Mail_In, Mail_InAdmin)
admin.site.register(Mail_Out, Mail_OutAdmin)
admin.site.register(Transaction_Exchange, Transaction_ExchangeAdmin)
