# Generated by Django 4.2.5 on 2023-10-28 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NFTapp', '0003_remove_cart_created_at_remove_cart_updated_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='owner',
            new_name='user',
        ),
    ]