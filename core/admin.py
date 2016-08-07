# -*- coding: utf8 -*-
from django.contrib import admin
from core.models import Professor, \
    Coordenador, Curso, Avalprof, \
    Avalcoord, OpcaoProf, OpcaoCoord, \
    Anoref, Semref, SemestreCurso, \
    Questao


class OpcaoProfAdmin(admin.TabularInline):
    model = OpcaoProf
    extra = 5
    list_display = (
        'opcao',
        'votos',
        'avalprof',
    )


class OpcaoCoordAdmin(admin.TabularInline):
    model = OpcaoCoord
    extra = 5
    list_display = (
        'opcao',
        'votos',
        'avalcoord',
    )


class OpcaoProfAdm(admin.ModelAdmin):
    list_display = (
        'opcao',
        'votos',
        'avalprof_id',
    )


class OpcaoCoordAdm(admin.ModelAdmin):
    list_display = (
        'opcao',
        'votos',
        'avalcoord_id',
    )


class AvalprofAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['questao']}),
        ('Ano', {'fields': ['anoref']}),
        ('Semestre', {'fields': ['semref']}),
        ('Curso', {'fields': ['curso']}),
        ('Semestre do Curso', {'fields': ['semestre']}),
        ('Professor', {'fields': ['professor']}),
    ]
    inlines = [OpcaoProfAdmin]
    list_display = (
        'anoref',
        'semref',
        'curso',
        'semestre',
        'professor',
        'questao',
        )
    list_filter = [
        'anoref',
        'semref',
        'curso',
        'questao',
        'professor',
    ]


class AvalcoordAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['questao']}),
        ('Ano', {'fields': ['anoref']}),
        ('Semestre', {'fields': ['semref']}),
        ('Curso', {'fields': ['curso']}),
        ('Semestre do Curso', {'fields': ['semestre']}),
        ('Coordenador', {'fields': ['coordenador']}),
    ]
    inlines = [OpcaoCoordAdmin]
    list_display = (
        'anoref',
        'semref',
        'curso',
        'semestre',
        'coordenador',
        'questao',
        )
    list_filter = [
        'anoref',
        'semref',
        'curso',
        'questao',
        'coordenador',
    ]


class QuestaoAdmin(admin.ModelAdmin):
    list_display = ('questao',)


class CoordAdmin(admin.ModelAdmin):
    list_display = ('curso', 'coordenador')
    search_field = ('curso', 'coordenador')


class CursoAdmin(admin.ModelAdmin):
    list_display = ('curso',)


class AnorefAdmin(admin.ModelAdmin):
    list_display = ('anoref',)


class SemrefAdmin(admin.ModelAdmin):
    list_display = ('semref',)


class SemestreCursoAdmin(admin.ModelAdmin):
    list_display = ('semestre',)


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('professor',)


admin.site.register(Curso, CursoAdmin)
admin.site.register(Anoref, AnorefAdmin)
admin.site.register(Semref, SemrefAdmin)
admin.site.register(SemestreCurso, SemestreCursoAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Coordenador, CoordAdmin)
admin.site.register(Avalprof, AvalprofAdmin)
admin.site.register(Avalcoord, AvalcoordAdmin)
admin.site.register(OpcaoProf, OpcaoProfAdm)
admin.site.register(OpcaoCoord, OpcaoCoordAdm)
admin.site.register(Questao, QuestaoAdmin)
