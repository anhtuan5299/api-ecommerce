# Generated by Django 4.0.4 on 2022-04-26 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_alter_category_deleted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
