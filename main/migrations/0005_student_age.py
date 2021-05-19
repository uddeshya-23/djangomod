# Generated by Django 3.2.2 on 2021-05-11 06:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_student_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(10)]),
        ),
    ]
