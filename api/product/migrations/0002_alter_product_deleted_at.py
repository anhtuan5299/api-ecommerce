# Generated by Django 4.0.4 on 2022-04-26 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]