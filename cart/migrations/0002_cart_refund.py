# Generated by Django 4.2.3 on 2023-07-11 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('refund', '0002_remove_refund_cart'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='refund',
            field=models.ForeignKey(default=255, on_delete=django.db.models.deletion.CASCADE, to='refund.refund'),
            preserve_default=False,
        ),
    ]
