from django.shortcuts import render
from django.apps import apps
from .app_models import *


def index(request):
    # model = {'x': apps.all_models['debtors']}
    model = {'x': Debtors._meta.get_fields()}
    return render(request, 'debtors/index.html', model)


