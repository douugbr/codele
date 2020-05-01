# Generated by Django 3.0.5 on 2020-05-01 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200501_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='badge',
            field=models.CharField(choices=[('ESTUDANTE', 'Estudante'), ('PROFESSOR', 'Professor'), ('MODERADOR', 'Moderador'), ('ADMIN', 'Admin'), ('FUNDADOR', 'Fundador')], default='STUDENT', max_length=10),
        ),
    ]
