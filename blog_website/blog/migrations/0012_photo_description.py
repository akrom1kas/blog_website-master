# Generated by Django 4.0.4 on 2022-05-11 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_post_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='description',
            field=models.TextField(null=True, verbose_name='Description'),
        ),
    ]