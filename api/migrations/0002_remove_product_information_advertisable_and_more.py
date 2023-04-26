# Generated by Django 4.2 on 2023-04-26 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_information',
            name='advertisable',
        ),
        migrations.RemoveField(
            model_name='product_information',
            name='corona_prod',
        ),
        migrations.AddField(
            model_name='product_information',
            name='is_adv',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product_information',
            name='is_corona_prod',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Advertisable',
        ),
        migrations.DeleteModel(
            name='Corona_Prod',
        ),
    ]
