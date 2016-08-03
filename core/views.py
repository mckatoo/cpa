# -*- coding: utf-8 -*-
# from django.shortcuts import render
from django.http import HttpResponse
from .models import Avalprof


def index(request):
    aval = Avalprof.objects.all().order_by("id")
    output = ', '.join([p.questao for p in aval])
    return HttpResponse(output)


def visualizar(request, id):
    return HttpResponse("visualizar = %d" % int(id))


def resultado(request, id):
    return HttpResponse("resultado = %d" % int(id))


def votar(request, id):
    return HttpResponse("votar = %d" % int(id))
