# Generated by Django 3.2.4 on 2021-06-24 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_product_forme'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='designation',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Prix_Vente',
            new_name='pph',
        ),
        migrations.AddField(
            model_name='product',
            name='ppv',
            field=models.FloatField(null=True),
        ),
    ]
