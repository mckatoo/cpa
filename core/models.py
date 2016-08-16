# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Professor(models.Model):
    professor = models.CharField(max_length=70)

    def __unicode__(self):
        return unicode(self.professor)


class Curso(models.Model):
    curso = models.CharField(max_length=70)

    def __unicode__(self):
        return unicode(self.curso)


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


class Coordenador(models.Model):
    curso = models.ForeignKey(Curso)
    coordenador = models.ForeignKey(Professor)
    semestre = models.ForeignKey(SemestreCurso)

    def __unicode__(self):
        return unicode(self.coordenador)


class lstQuestao(models.Model):
    lstquestao = models.CharField(max_length=200)

    def __unicode__(self):
        return unicode(self.lstquestao)


class Questao(models.Model):
    questao = models.ForeignKey(lstQuestao)
    data_publicacao = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return unicode(self.questao)


class Aval(models.Model):
    anoref = models.ForeignKey(Anoref)
    semref = models.ForeignKey(Semref)
    curso = models.ForeignKey(Curso)
    semestre = models.ForeignKey(SemestreCurso)
    coordenador = models.ForeignKey(Coordenador)
    professor = models.ForeignKey(Professor)
    questao = models.ForeignKey(Questao)

    def __unicode__(self):
        return unicode(self.id)


class Opcao(models.Model):
    opcao = models.CharField(max_length=50)
    votos = models.IntegerField(default=0)
    questao = models.ForeignKey(Questao)
