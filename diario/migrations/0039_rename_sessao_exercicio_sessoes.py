# Generated by Django 4.0.3 on 2022-07-12 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0038_remove_exercicio_atividade_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercicio',
            old_name='sessao',
            new_name='sessoes',
        ),
    ]
