# Generated by Django 4.2.5 on 2023-12-06 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NFTapp', '0009_alter_user_avatar_alter_user_cover_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='/static/images/avatars/avatar2.svg', upload_to='avatars/%Y/%m/%d/'),
        ),
    ]
