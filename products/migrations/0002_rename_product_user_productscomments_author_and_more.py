# Generated by Django 4.2 on 2023-04-28 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productscomments',
            old_name='product_user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='productscomments',
            old_name='product_comment',
            new_name='comment',
        ),
    ]