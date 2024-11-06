# Generated by Django 5.1.1 on 2024-10-31 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.FloatField(max_length=4),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
