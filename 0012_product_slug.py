# Generated by Django 5.0.6 on 2024-06-22 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0011_alter_product_off_alter_product_short_descript'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=100, null=True, verbose_name='عنوان در آدرس'),
        ),
    ]
