import re

from rest_framework.permissions import IsAdminUser

from ..app_models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action
from drf_yasg2.utils import swagger_auto_schema

'''Извлекаю данные для реестра должников'''

"""ОГРАНИЧЕНИЯ ДОСТУПА:
Дефолтные permissions:
AllowAny - полный доступ;
IsAdminUser - только для Администраторов;
IsAuthenticated - только для авторизованных пользователей;
IsAuthenticatedOrReadOnly - только для авторизованных или всем, но для чтения.

Кастомные permissions:
IsAdminOrReadOnly - запись может просматривать любой, а удалять только Администратор;
IsOwnerAndAdminOrReadOnly - запись может менять только пользователь который её создал и Админ, просматривать может любой.
"""


class GetDebtorsRegistryAPIView(APIView):
    @swagger_auto_schema(
        method='get',
        tags=['Реестр должников'],
        operation_description="Получить список должников", )
    @action(detail=False, methods=['get'])
    def get(self, request):
        executiv_document = Executive_Documents.objects.values()

        registry_debtors = []
        for ed in executiv_document:
            credit = Credits.objects.values().get(pk=ed['credit_id'])
            cession = Cession.objects.values().get(pk=credit['cession_id'])
            debtor = Debtors.objects.values().get(pk=credit['debtor_id'])

            try:
                ep = Executive_Productions.objects.values().get(executive_document=ed['id'])
            except Exception:
                ep = {'number': '',
                      'date_on': '',
                      'date_end': '',
                      'reason_end': '',
                      'curent_debt': '',
                      'summa_debt': '',
                      'rosp': '',
                      'address_rosp': '',
                      'pristav': '',
                      'pristav_phone': '',
                      'date_request': '',
                      'comment': '',}

            if debtor['last_name_2'] == None:
                fio = f"{debtor['last_name_1']} {debtor['first_name_1']} {debtor['second_name_1'] or ''}"
            else:
                fio = f"{debtor['last_name_1']} {debtor['first_name_1']} {debtor['second_name_1'] or ''} " \
                      f"({debtor['last_name_2']} {debtor['first_name_2']} {debtor['second_name_2'] or ''})"

            passport = f"{debtor['passport_series']} {debtor['passport_num']} от {debtor['passport_date'] or ''}"

            registry_debtors.append({'type_ed': ed['type_ed'],
                                     'number_ed': ed['number'],
                                     'date_ed': ed['date'],
                                     'case_number_ed': ed['case_number'],
                                     'date_of_receipt_ed': ed['date_of_receipt_ed'],
                                     'date_decision_ed': ed['date_decision'],
                                     'status_ed': ed['status_ed'],
                                     'comment_ed': ed['comment'],
                                     'creditor': credit['creditor'],
                                     'number_credit': credit['number'],
                                     'date_start_credit': credit['date_start'],
                                     'date_end_credit': credit['date_end'],
                                     'summa_credit': credit['summa'],
                                     'interest_rate_credit': credit['interest_rate'],
                                     'overdue_od_credit': credit['overdue_od'],
                                     'overdue_percent_credit': credit['overdue_percent'],
                                     'penalty_credit': credit['penalty'],
                                     'percent_of_od_credit': credit['percent_of_od'],
                                     'gov_toll_credit': credit['gov_toll'],
                                     'comment_credit': credit['comment'],
                                     'date_cessii': cession['date'],
                                     'number_cessii': cession['number'],
                                     'cedent': cession['cedent'],
                                     'date_old_cession': cession['date_old_cession'],
                                     'name_cessii': cession['name'],
                                     'cessionari': cession['cessionari'],
                                     'summa_cessii': cession['summa'],
                                     'fio_debtor': fio,
                                     'pol': debtor['pol'],
                                     'birthday': debtor['birthday'],
                                     'place_of_birth': debtor['place_of_birth'],
                                     'passport': passport,
                                     'inn': debtor['inn'],
                                     'snils': debtor['snils'],
                                     'address_registry': debtor['address_1'],
                                     'address_resident': debtor['address_2'],
                                     'index_add_registry': debtor['index_add_1'],
                                     'index_add_resident': debtor['index_add_2'],
                                     'comment_debtors': debtor['comment'],
                                     'number_ep': ep['number'],
                                     'date_on_ep': ep['date_on'],
                                     'date_end_ep': ep['date_end'],
                                     'reason_end_ep': ep['reason_end'],
                                     'curent_debt_ep': ep['curent_debt'],
                                     'summa_debt_ep': ep['summa_debt'],
                                     'rosp_ep': ep['rosp'],
                                     'address_rosp_ep': ep['address_rosp'],
                                     'pristav_ep': ep['pristav'],
                                     'pristav_phone_ep': ep['pristav_phone'],
                                     'date_request_ep': ep['date_request'],
                                     'comment_ep': ep['comment'],
                                     })

        return Response(registry_debtors)