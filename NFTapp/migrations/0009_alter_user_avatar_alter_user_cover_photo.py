# Generated by Django 4.2.5 on 2023-12-06 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NFTapp', '0008_alter_user_avatar_alter_user_cover_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='/static/images/avatars/avatar1.svg', upload_to='avatars/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='cover_photo',
            field=models.ImageField(default='/static/images/generic/Acer_Wallpaper_05_3840x2400.jpg', upload_to='cover_photos/%Y/%m/%d/'),
        ),
    ]
