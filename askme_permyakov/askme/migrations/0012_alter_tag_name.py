# Generated by Django 4.2 on 2023-07-08 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askme', '0011_answertoresponselikes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
