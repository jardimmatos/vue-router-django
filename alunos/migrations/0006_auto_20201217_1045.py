# Generated by Django 3.1.4 on 2020-12-17 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0005_auto_20201217_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='matricula',
            field=models.CharField(max_length=10, null=True, unique=True, verbose_name='Nome'),
        ),
    ]