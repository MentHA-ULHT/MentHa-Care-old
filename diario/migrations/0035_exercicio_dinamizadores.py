# Generated by Django 4.0.3 on 2022-07-12 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0034_alter_exercicio_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercicio',
            name='dinamizadores',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
