# Generated by Django 4.2 on 2023-05-03 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('askme', '0002_author_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='avatar',
            field=models.ImageField(default='https://i.pinimg.com/originals/64/94/0c/64940cfc8514d44598287ab290905cf8.jpg', upload_to=''),
        ),
    ]
