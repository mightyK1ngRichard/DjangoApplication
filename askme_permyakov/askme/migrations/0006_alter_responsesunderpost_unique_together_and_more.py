# Generated by Django 4.2 on 2023-06-20 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askme', '0005_alter_responsesunderpost_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='responsesunderpost',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='author',
            name='avatar',
            field=models.ImageField(default='static/img/default.webp', upload_to='static/img'),
        ),
    ]
