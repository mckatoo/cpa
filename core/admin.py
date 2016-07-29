# -*- coding: utf8 -*-
from django.contrib import admin
from core.models import Professor, \
    Coordenador, Curso, Avalprof, \
    Avalcoord, OpcaoProf, OpcaoCoord


class OpcaoProfAdmin(admin.TabularInline):
    model = OpcaoProf
    extra = 5


class AvalprofAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['questao']}),
        ('Professor', {'fields': ['professor']})
    ]
    inlines = [OpcaoProfAdmin]
    list_display = ('questao', 'professor')


admin.site.register(Curso)
admin.site.register(Professor)
admin.site.register(Coordenador)
admin.site.register(Avalprof, AvalprofAdmin)
admin.site.register(Avalcoord)
admin.site.register(OpcaoProf)
admin.site.register(OpcaoCoord)
