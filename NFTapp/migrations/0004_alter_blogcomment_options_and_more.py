# Generated by Django 4.2.5 on 2023-11-10 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('NFTapp', '0003_alter_user_cover_photo_alter_user_property'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcomment',
            options={'ordering': ['-added_at']},
        ),
        migrations.AlterModelOptions(
            name='productcomment',
            options={'ordering': ['-added_at']},
        ),
        migrations.AlterField(
            model_name='user',
            name='cover_photo',
            field=models.ImageField(default='/static/images/generic/Acer_Wallpaper_05_3840x2400.jpg', upload_to='avatar/%Y/%m/%d/'),
        ),
        migrations.CreateModel(
            name='TradeHistory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('price_at_purchase', models.DecimalField(decimal_places=4, max_digits=6)),
                ('quantity_at_purchase', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer_trades', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NFTapp.nftproduct')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_trades', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
