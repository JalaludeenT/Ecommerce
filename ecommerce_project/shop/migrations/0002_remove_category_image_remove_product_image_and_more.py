# Generated by Django 4.2.8 on 2023-12-23 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='Category_Images'),
        ),
        migrations.AddField(
            model_name='product',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='Product_Images'),
        ),
    ]
