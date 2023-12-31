# Generated by Django 4.2.5 on 2023-12-06 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NFTapp', '0007_alter_user_avatar_alter_user_cover_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='/static/images/avatar/avatar6.svg', upload_to='avatars/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='cover_photo',
            field=models.ImageField(default='/static/images/generic/Acer_Wallpaper_04_3840x2400.jpg', upload_to='cover_photos/%Y/%m/%d/'),
        ),
    ]
