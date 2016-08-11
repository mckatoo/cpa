# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Anoref, Avalprof, Semref, \
    Curso, SemestreCurso, OpcaoProf
# from .form import AvalprofForm


def index(request):
    data = {}
    data['tela'] = 1
    data['lista_anos'] = Anoref.objects.all()
    data['lista_aval'] = Avalprof.objects.all()
    data['lista_semref'] = Semref.objects.all()
    data['lista_curso'] = Curso.objects.all()
    data['lista_semestre'] = SemestreCurso.objects.all()
    data['opcao'] = OpcaoProf.objects.all()
    return render(request, 'aval.html', data)
    # aval = Avalprof.objects.all()
    # form = AvalprofForm(request.POST or None, instance=aval)
    # if form.is_valid():
    #     form.save()
    #     return redirect('home')
    # return render(request, 'aval.html', {'object': aval, 'form': form})


# def index2(request, id):
#     data = {}
#     data['tela'] = 2
#     data['professor'] = Avalprof.objects.get()
#     data['lista_semref'] = Semref.objects.all()
#     data['lista_curso'] = Curso.objects.all()
#     data['lista_semestre'] = SemestreCurso.objects.all()
#     return render(request, 'aval.html', data)


def visualizar_coord(request, anoref, semref, curso, semestre):
    return HttpResponse(
        "visualizar = %d" %
        int(anoref) %
        int(semref) %
        int(curso) %
        int(semestre)
    )


def visualizar_prof(request, anoref, semref, curso, semestre):
    data = {}
    data['tela'] = 2
    data['lista_anos'] = Anoref.objects.all()
    data['lista_aval'] = Avalprof.objects.all()
    data['lista_semref'] = Semref.objects.all()
    data['lista_curso'] = Curso.objects.all()
    data['lista_semestre'] = SemestreCurso.objects.all()
    return render(request, 'aval.html', data)


def resultado(request, id):
    return HttpResponse("resultado = %d" % int(id))


def votar(request, id):
    return HttpResponse("votar = %d" % int(id))
