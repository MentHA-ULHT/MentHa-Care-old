# Generated by Django 4.0.3 on 2022-07-15 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0045_alter_notagrupo_grupo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notagrupo',
            old_name='descricao',
            new_name='nota',
        ),
    ]
