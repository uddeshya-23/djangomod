# Generated by Django 3.2.2 on 2021-05-11 06:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_student_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True, validators=[django.core.validators.EmailValidator('Email address is not valid')]),
        ),
    ]
