# Generated by Django 4.2.3 on 2023-07-19 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_basket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'категорию', 'verbose_name_plural': 'Категории'},
        ),
    ]