from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render


# def index(request):
#     message = "Salut tout le monde !"
#     return HttpResponse(message)

def index(request):
    """view return home page"""
    return render(request, 'app_inventory_fk/index.html')

