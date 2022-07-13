# Generated by Django 4.0.3 on 2022-07-12 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0039_rename_sessao_exercicio_sessoes'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercicio',
            name='atividade',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='exercicio',
            name='objetivo',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='sessao',
            name='componentes',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='sessao',
            name='dinamizadores',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='sessao',
            name='instrucoes',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='sessao',
            name='introducao',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='sessao',
            name='tema',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
