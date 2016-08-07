# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Professor(models.Model):
    professor = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.professor)


class Curso(models.Model):
    curso = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.curso)


class Coordenador(models.Model):
    curso = models.ForeignKey(Curso)
    coordenador = models.ForeignKey(Professor)

    def __unicode__(self):
        return unicode(self.coordenador)


class Anoref(models.Model):
    anoref = models.IntegerField()

    def __str__(self):
        return str(self.anoref)


class Semref(models.Model):
    semref = models.CharField(max_length=15)

    def __unicode__(self):
        return unicode(self.semref)


class SemestreCurso(models.Model):
    semestre = models.CharField(max_length=20)

    def __unicode__(self):
        return unicode(self.semestre)


class Questao(models.Model):
    questao = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.questao)


class Avalcoord(models.Model):
    anoref = models.ForeignKey(Anoref)
    semref = models.ForeignKey(Semref)
    curso = models.ForeignKey(Curso)
    semestre = models.ForeignKey(SemestreCurso)
    coordenador = models.ForeignKey(Coordenador)
    questao = models.ForeignKey(Questao)


class OpcaoCoord(models.Model):
    opcao = models.CharField(max_length=50)
    votos = models.IntegerField()
    avalcoord = models.ForeignKey(Avalcoord)


class Avalprof(models.Model):
    anoref = models.ForeignKey(Anoref)
    semref = models.ForeignKey(Semref)
    curso = models.ForeignKey(Curso)
    semestre = models.ForeignKey(SemestreCurso)
    professor = models.ForeignKey(Professor)
    questao = models.ForeignKey(Questao)


class OpcaoProf(models.Model):
    opcao = models.CharField(max_length=50)
    votos = models.IntegerField()
    avalprof = models.ForeignKey(Avalprof)
