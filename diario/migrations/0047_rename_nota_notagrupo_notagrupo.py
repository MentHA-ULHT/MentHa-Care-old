# Generated by Django 4.0.3 on 2022-07-15 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0046_rename_descricao_notagrupo_nota'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notagrupo',
            old_name='nota',
            new_name='notaGrupo',
        ),
    ]
