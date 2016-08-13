# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-13 16:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anoref',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anoref', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Avalcoord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anoref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Anoref')),
            ],
        ),
        migrations.CreateModel(
            name='Avalprof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anoref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Anoref')),
            ],
        ),
        migrations.CreateModel(
            name='Coordenador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='lstQuestao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lstquestao', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Opcao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcao', models.CharField(max_length=50)),
                ('votos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Questao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_publicacao', models.DateTimeField(auto_now=True)),
                ('questao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.lstQuestao')),
            ],
        ),
        migrations.CreateModel(
            name='SemestreCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semestre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Semref',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semref', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='opcao',
            name='questao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Questao'),
        ),
        migrations.AddField(
            model_name='coordenador',
            name='coordenador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Professor'),
        ),
        migrations.AddField(
            model_name='coordenador',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Curso'),
        ),
        migrations.AddField(
            model_name='avalprof',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Curso'),
        ),
        migrations.AddField(
            model_name='avalprof',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Professor'),
        ),
        migrations.AddField(
            model_name='avalprof',
            name='questao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Questao'),
        ),
        migrations.AddField(
            model_name='avalprof',
            name='semestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.SemestreCurso'),
        ),
        migrations.AddField(
            model_name='avalprof',
            name='semref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Semref'),
        ),
        migrations.AddField(
            model_name='avalcoord',
            name='coordenador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Coordenador'),
        ),
        migrations.AddField(
            model_name='avalcoord',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Curso'),
        ),
        migrations.AddField(
            model_name='avalcoord',
            name='questao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Questao'),
        ),
        migrations.AddField(
            model_name='avalcoord',
            name='semestre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.SemestreCurso'),
        ),
        migrations.AddField(
            model_name='avalcoord',
            name='semref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Semref'),
        ),
    ]
