# Generated by Django 5.0.1 on 2024-01-13 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_item_item_desc_item_item_price_alter_item_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://theme-assets.getbento.com/sensei/86430ac.sensei/assets/images/catering-item-placeholder-704x520.png', max_length=500),
        ),
    ]
