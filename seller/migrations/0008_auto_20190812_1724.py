# Generated by Django 2.2.4 on 2019-08-12 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0007_auto_20190812_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='shop/catimages'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
