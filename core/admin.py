# -*- coding: utf8 -*-
from django.contrib import admin
from core.models import Professor, \
    Coordenador, Curso, Aval, \
    Opcao, Anoref, Semref, \
    SemestreCurso, Questao, lstQuestao


class AvalAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Ano', {'fields': ['anoref']}),
        ('Semestre', {'fields': ['semref']}),
        ('Curso', {'fields': ['curso']}),
        ('Semestre do Curso', {'fields': ['semestre']}),
        ('Professor', {'fields': ['professor']}),
    ]
    list_display = (
        'anoref',
        'semref',
        'curso',
        'semestre',
        'professor',
        )
    list_filter = [
        'anoref',
        'semref',
        'curso',
        'professor',
    ]


class AvalcoordAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Ano', {'fields': ['anoref']}),
        ('Semestre', {'fields': ['semref']}),
        ('Curso', {'fields': ['curso']}),
        ('Semestre do Curso', {'fields': ['semestre']}),
        ('Coordenador', {'fields': ['coordenador']}),
    ]
    list_display = (
        'anoref',
        'semref',
        'curso',
        'semestre',
        'coordenador',
        )
    list_filter = [
        'anoref',
        'semref',
        'curso',
        'coordenador',
    ]


class OpcaoTab(admin.TabularInline):
    model = Opcao
    extra = 5
    list_display = (
        'opcao',
        'votos',
        'avalcoord',
    )


class OpcaoAdmin(admin.ModelAdmin):
    list_display = (
        'opcao',
        'votos',
        'questao_id',
    )


class AvalTab(admin.TabularInline):
    model = Aval
    extra = 4


class QuestaoAdmin(admin.ModelAdmin):
    list_display = ('questao',)
    inlines = [AvalTab, OpcaoTab]


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
admin.site.register(Aval, AvalAdmin)
admin.site.register(Opcao, OpcaoAdmin)
admin.site.register(Questao, QuestaoAdmin)
admin.site.register(lstQuestao)
