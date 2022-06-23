# Generated by Django 4.0.3 on 2022-06-23 23:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diario', '0027_alter_respostas_pergunta'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformacoesGrupo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('informacoesGrupo', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True, null=True)),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diario.grupocare')),
            ],
        ),
    ]