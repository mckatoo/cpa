# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Anoref
# from .form import AvalprofForm


def index(request):
    data = {}
    data['lista_anos'] = Anoref.objects.all()
    return render(request, 'aval.html', data)
    # aval = Avalprof.objects.all()
    # form = AvalprofForm(request.POST or None, instance=aval)
    # if form.is_valid():
    #     form.save()
    #     return redirect('home')
    # return render(request, 'aval.html', {'object': aval, 'form': form})


def visualizar(request, id):
    return HttpResponse("visualizar = %d" % int(id))


def resultado(request, id):
    return HttpResponse("resultado = %d" % int(id))


def votar(request, id):
    return HttpResponse("votar = %d" % int(id))
