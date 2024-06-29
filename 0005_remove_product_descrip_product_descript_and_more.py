# Generated by Django 5.0.6 on 2024-06-14 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0004_rename_poduct_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='descrip',
        ),
        migrations.AddField(
            model_name='product',
            name='descript',
            field=models.TextField(max_length=1000, null=True, verbose_name='توضیحات بیشتر'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='فعال/غیر فعال'),
        ),
        migrations.AddField(
            model_name='product',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='حذف شده/حذف نشده'),
        ),
        migrations.AddField(
            model_name='product',
            name='short_descript',
            field=models.TextField(max_length=500, null=True, verbose_name='توضیحات مختصر'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(null=True, verbose_name='قیمت'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100, null=True, verbose_name='عنوان'),
        ),
    ]
