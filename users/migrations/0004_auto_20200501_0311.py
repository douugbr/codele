# Generated by Django 3.0.5 on 2020-05-01 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200501_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='badge',
            field=models.CharField(choices=[('ESTUDANTE', 'Student'), ('PROFESSOR', 'Professor'), ('MODERADOR', 'Moderator'), ('ADMIN', 'Admin'), ('FUNDADOR', 'Founder')], default='STUDENT', max_length=10),
        ),
    ]
