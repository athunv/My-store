# Generated by Django 5.0.3 on 2024-04-16 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productbook',
            old_name='discription',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='productbook',
            old_name='prise',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='productbook',
            name='auther',
        ),
        migrations.AddField(
            model_name='productbook',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
