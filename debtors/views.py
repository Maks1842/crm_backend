from django.shortcuts import render
from django.apps import apps
from .app_models import *
from django.template.loader import render_to_string
from weasyprint import HTML


def index(request):
    x = Debtors
    model = x._meta.local_fields

    # Запись в одну строку, совмещает цикл for и добавление значений в список (аналог append)
    data = {'x': Credits._meta.get_fields()} # Данные о модели и полях (типы, наименования)
    data = {'x': Credits._meta.get_field('debtor').get_internal_type()} # Тип поля
    data = {'x': Debtors._meta.model_name}  # Имя модели
    data = {'x': Debtors._meta.verbose_name}  # Имя модели verbose_name
    field_names = [f.name for f in model] # Имена полей
    # data = {'x': field_names}
    return render(request, 'debtors/index.html', data)


