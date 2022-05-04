# Generated by Django 4.0.3 on 2022-04-07 23:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0002_alter_participante_grupocog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuidador',
            name='grupoCare',
            field=models.ManyToManyField(blank=True, null=True, related_name='cuidadores', to='diario.grupocare'),
        ),
        migrations.AlterField(
            model_name='facilitador',
            name='grupoCog',
            field=models.ManyToManyField(blank=True, null=True, related_name='facilitadores', to='diario.grupocog'),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='grupoCare',
            field=models.ManyToManyField(blank=True, null=True, related_name='mentores', to='diario.grupocare'),
        ),
        migrations.AlterField(
            model_name='participante',
            name='grupoCog',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='diario.grupocog'),
        ),
    ]
